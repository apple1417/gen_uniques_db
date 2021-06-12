import csv
import logging
import sqlite3
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Optional

import bl3dump
from data.constants import MAPS
from data.enemies import (BPCHAR_INHERITANCE_OVERRIDES, BPCHAR_NAME_OVERRIDES, DROP_OVERRIDES,
                          ENEMY_DROP_EXPANSIONS, IGNORED_BPCHARS, MAP_OVERRIDES)
from data.hotfixes import (HOTFIX_DOD_POOLS_REMOVE_ALL, HOTFIX_ITEMPOOLLISTS_ADD,
                           HOTFIX_JUDGE_HIGHTOWER_PT_OVERRIDE)
from itempool_handling import load_itempool_contents
from util import iter_object_refs

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
    if bpchar in MAP_OVERRIDES:
        return MAP_OVERRIDES[bpchar]

    output_map_name: Optional[str] = None

    for obj in iter_object_refs(bpchar):
        if not obj.split(".")[-1].startswith("SpawnOptions"):
            continue

        for obj2 in iter_object_refs(obj):
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


def load_itempool_list(item_pool_list: str) -> set[str]:
    output = set()
    export = bl3dump.AssetFile(item_pool_list).get_single_export("ItemPoolListData")
    for pool in export.get("ItemPools", []):
        output.update(load_itempool_contents(pool["ItemPool"][1]))

    for pool in HOTFIX_ITEMPOOLLISTS_ADD.get(item_pool_list, []):
        output.update(load_itempool_contents(pool))

    return output


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


def iter_all_enemies() -> Iterator[tuple[str, str, bl3dump.AssetFile]]:
    name_data = {}
    with open("bpchars/expanded.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            # Arbitrarily only using the first value as the name
            bpchar, name = row[0:2]
            if bpchar in IGNORED_BPCHARS:
                continue
            if bpchar in BPCHAR_NAME_OVERRIDES:
                name = BPCHAR_NAME_OVERRIDES[bpchar]
            if name == "(unknown)":
                continue
            name_data[row[0]] = name

    all_names = list(name_data.values())
    for bpchar, name in name_data.items():
        # Make duplicate names different
        # In practice, anything that makes it into the database should have it's name overwritten to
        #  something unique anyway, this is more to help when setting up the overrides
        if all_names.count(name) > 0:
            name = f"{name} ({bpchar})"

        asset: bl3dump.AssetFile
        if bpchar in BPCHAR_INHERITANCE_OVERRIDES:
            asset = bl3dump.AssetFile(BPCHAR_INHERITANCE_OVERRIDES[bpchar])
        else:
            asset = bl3dump.AssetFile(bpchar)

        yield name, bpchar, asset


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

    for enemy_name, obj_name, bpchar in iter_all_enemies():
        drops: set[str]
        if obj_name in DROP_OVERRIDES:
            override = DROP_OVERRIDES[obj_name]
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
            try:
                balance = bpchar.get_single_export("AIBalanceStateComponent")
            except ValueError:
                logging.info(f"Couldn't extract bpchar: {obj_name}")
                continue
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

        if (cls_name := bpchar.name.split(".")[-1] + "_C") in all_expansions:
            drops.update(all_expansions[cls_name])

        if len(drops) > 0:
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
