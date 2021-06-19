import logging
import sqlite3
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Optional

import bl3dump
from data.constants import MAPS
from data.enemies import (BPCHAR_GLOBS, BPCHAR_INHERITANCE_OVERRIDES, BPCHAR_NAMES, DROP_OVERRIDES,
                          ENEMY_DROP_EXPANSIONS, IGNORED_BPCHARS, MAP_OVERRIDES)
from data.hotfixes import HOTFIX_DOD_POOLS_REMOVE_ALL, HOTFIX_JUDGE_HIGHTOWER_PT_OVERRIDE
from itempool_handling import load_itempool_contents, load_itempool_list
from util import fix_dotted_object_name, iter_refs_from, iter_refs_to

MAP_PREFIX_TO_NAME: dict[str, str] = {
    v.removesuffix("_P"): k for k, v in MAPS
}


@dataclass
class EnemyData:
    obj_name: str
    enemy_map: Optional[str]
    description: str
    drops: set[str]


def get_enemy_map(bpchar: str) -> Optional[str]:
    if (name := bpchar.split(".")[-1]) in MAP_OVERRIDES:
        return MAP_OVERRIDES[name]

    output_map_name: Optional[str] = None

    for obj in iter_refs_to(bpchar):
        if not obj.split(".")[-1].startswith("SpawnOptions"):
            continue

        for obj2 in iter_refs_to(obj):
            name = obj2.split(".")[-1]

            for prefix, map_name in MAP_PREFIX_TO_NAME.items():
                if name.startswith(prefix):
                    if output_map_name is not None and output_map_name != map_name:
                        logging.info(
                            f"Enemy has multiple possible map names: {output_map_name} / {map_name}"
                            f" - {bpchar}"
                        )
                    output_map_name = map_name

    if output_map_name is None:
        logging.error(f"Couldn't find map for enemy: {bpchar}")
    return output_map_name


def expand_drop_on_death(dod_data: bl3dump.JSON, obj_name: Optional[str] = None) -> set[str]:
    hf_empty_itempools = False
    hf_empty_itempool_lists = False
    if obj_name is not None and obj_name in HOTFIX_DOD_POOLS_REMOVE_ALL:
        hf_empty_itempools, hf_empty_itempool_lists = HOTFIX_DOD_POOLS_REMOVE_ALL[obj_name]

    output = set()
    if not hf_empty_itempools:
        for pool in dod_data.get("ItemPools", []):
            if isinstance(pool["ItemPool"], dict):
                continue
            output.update(load_itempool_contents(pool["ItemPool"][1]))

    if not hf_empty_itempool_lists:
        for pool_list in dod_data.get("ItemPoolLists", []):
            if isinstance(pool_list, dict):
                continue
            output.update(load_itempool_list(pool_list[1]))

    return output


def iter_enemy_drop_expansions() -> Iterator[bl3dump.JSON]:
    for enemy_expansion in ENEMY_DROP_EXPANSIONS:
        asset = bl3dump.AssetFile(enemy_expansion)
        for expansion_list in asset.iter_exports_of_class("CharacterItemPoolExpansionData"):
            yield from expansion_list["CharacterExpansions"]


def iter_all_enemies() -> Iterator[tuple[str, bl3dump.AssetFile]]:
    for pattern in BPCHAR_GLOBS:
        for asset in bl3dump.glob(pattern):
            if not isinstance(asset, bl3dump.AssetFile):
                continue
            if asset.name in IGNORED_BPCHARS:
                continue

            obj_name = fix_dotted_object_name(asset.path)

            if asset.name in BPCHAR_INHERITANCE_OVERRIDES:
                asset = bl3dump.AssetFile(BPCHAR_INHERITANCE_OVERRIDES[asset.name])

            try:
                asset.get_single_export("AIBalanceStateComponent")
            except ValueError:
                possible_inherited = set()
                # Using asset path incase we got overwritten earlier
                for ref in iter_refs_from(fix_dotted_object_name(asset.path)):
                    name = ref.split(".")[-1]
                    if name.startswith("BPChar_") and name not in IGNORED_BPCHARS:
                        possible_inherited.add(ref)

                if len(possible_inherited) == 0:
                    logging.info(f"Couldn't find inherited bpchar for: {obj_name}")
                    continue
                elif len(possible_inherited) > 1:
                    logging.info(f"Multiple possible inherited bpchars for: {obj_name}")
                    continue

                asset = bl3dump.AssetFile(possible_inherited.pop())
                try:
                    asset.get_single_export("AIBalanceStateComponent")
                except (FileNotFoundError, ValueError):
                    logging.info(f"Inherited bpchar is also empty for: {obj_name}")
                    continue

            yield obj_name, asset


def iter_enemy_data() -> Iterator[EnemyData]:
    all_expansions: dict[str, set[str]] = {}
    for expansion_data in iter_enemy_drop_expansions():
        expansion_pools = {
            dod["ItemPool"][1]
            for dod in expansion_data["value"]["DropOnDeathItemPools"]
        }

        expansion_drops = set()
        for pool in expansion_pools:
            expansion_drops.update(load_itempool_contents(pool))

        all_expansions[expansion_data["key"]] = expansion_drops

    for obj_name, asset in iter_all_enemies():
        bpchar_name = obj_name.split(".")[-1]

        drops: set[str]
        if bpchar_name in DROP_OVERRIDES:
            override = DROP_OVERRIDES[bpchar_name]
            drops = expand_drop_on_death({
                "ItemPools": [
                    {"ItemPool": ["", pool]}
                    for pool in override.itempools
                ],
                "ItemPoolLists": [
                    ["", pool_list]
                    for pool_list in override.itempool_lists
                ]
            })
        else:
            balance = asset.get_single_export("AIBalanceStateComponent")
            drops = expand_drop_on_death(balance.get("DropOnDeathItemPools", {}), obj_name)

            bad_drops = False
            for pt_idx, pt in enumerate(balance.get("PlayThroughs", [])):
                if obj_name == HOTFIX_JUDGE_HIGHTOWER_PT_OVERRIDE and pt_idx == 0:
                    continue

                if not pt["bOverrideDropOnDeathItemPools"]:
                    continue
                pt_drops = expand_drop_on_death(pt["DropOnDeathItemPools"])

                if any(x not in pt_drops for x in drops):
                    bad_drops = True
                    logging.info(
                        f"Replacement pool does not contain all items from original: {obj_name}"
                    )
                    break

                drops = pt_drops
            if bad_drops:
                continue

        # Using asset name to pickup x3
        if (cls_name := asset.name.split(".")[-1] + "_C") in all_expansions:
            drops.update(all_expansions[cls_name])

        found_spawnoptions_pools: set[str] = set()
        for obj in iter_refs_to(obj_name):
            if not obj.split(".")[-1].startswith("SpawnOption"):
                continue

            for factory in bl3dump.AssetFile(obj).iter_exports_of_class("SpawnFactory_OakAI"):
                if "AIActorClass" not in factory or "ItemPoolToDropOnDeath" not in factory:
                    continue
                if factory["AIActorClass"]["asset_path_name"].split(".")[-1] != bpchar_name + "_C":
                    continue

                pool = fix_dotted_object_name(factory["ItemPoolToDropOnDeath"][1])
                if pool in found_spawnoptions_pools:
                    continue

                pool_contents: set[str]
                if pool.split(".")[-1].startswith("ItemPoolList_"):
                    pool_contents = load_itempool_list(pool)
                else:
                    pool_contents = load_itempool_contents(pool)

                if not pool_contents:
                    continue

                if found_spawnoptions_pools:
                    logging.info(f"Found multiple drop adding spawnoptions for bpchar: {obj_name}")
                found_spawnoptions_pools.add(pool)

                drops.update(pool_contents)

        if len(drops) > 0:
            enemy_name: str
            if bpchar_name in BPCHAR_NAMES:
                enemy_name = BPCHAR_NAMES[bpchar_name]
            else:
                logging.info(f"BPChar needs name: {bpchar_name}")
                enemy_name = bpchar_name
            yield EnemyData(obj_name, get_enemy_map(obj_name), enemy_name, drops)


def insert_enemies(con: sqlite3.Connection) -> None:
    cur = con.cursor()

    for enemy_data in iter_enemy_data():
        cur.execute(
            """
            INSERT INTO Sources (SourceType, Map, Description, ObjectName) VALUES (
                "Enemy",
                ?,
                ?,
                ?
            )
            """,
            (enemy_data.enemy_map, enemy_data.description, enemy_data.obj_name)
        )
        row_id = cur.lastrowid

        for balance in enemy_data.drops:
            cur.execute(
                """
                INSERT INTO ObtainedFrom (ItemID, SourceID) VALUES (
                    (SELECT ID FROM Items WHERE ObjectName = ?),
                    ?
                )
                """,
                (balance, row_id)
            )

    con.commit()
