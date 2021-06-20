import logging
import sqlite3
from collections.abc import Collection

import bl3dump
from data.hotfixes import (HOTFIX_BALANCEDITEMS_ADD, HOTFIX_BALANCEDITEMS_REMOVE,
                           HOTFIX_ITEMPOOLLISTS_ADD, BalancedItemsEntry)
from data.itempools import (ITEMPOOL_EXPANSIONS, ITEMPOOL_OVERRIDES, KNOWN_EMPTY_POOLS,
                            WORLD_DROP_POOLS)
from data.items import EXPANDABLE_BALANCES
from util import RE_OBJECT_NAME, fix_dotted_object_name

_known_itempools: dict[str, set[str]] = {}
_known_itempool_expansions: dict[str, set[str]] = {}

_known_balances: set[str] = set()

_ALL_DLCS = WORLD_DROP_POOLS.keys()


def load_itempool_contents(
    pool_name: str,
    world_drop_blacklist: Collection[str] = _ALL_DLCS
) -> set[str]:
    pool_name = fix_dotted_object_name(pool_name)

    for dlc in world_drop_blacklist:
        if pool_name in WORLD_DROP_POOLS[dlc]:
            return set()
    if pool_name in ITEMPOOL_OVERRIDES:
        return ITEMPOOL_OVERRIDES[pool_name]
    if pool_name in _known_itempools:
        return _known_itempools[pool_name]

    match = RE_OBJECT_NAME.match(pool_name)
    if match is None:
        raise RuntimeError("Can't parse Itempool name")
    asset = bl3dump.AssetFile(match.group("Path") + match.group("FileName"))

    if not asset.exists():
        raise RuntimeError("Itempool does not exist in assets")

    itempool_data = {}
    try:
        itempool_data = asset.get_single_export("ItemPoolData")
    except ValueError:
        pass

    all_balances = _get_balanced_items(itempool_data, world_drop_blacklist, pool_name)

    if pool_name in _known_itempool_expansions:
        all_balances.update(_known_itempool_expansions[pool_name])

    if len(all_balances) != 0 and pool_name in KNOWN_EMPTY_POOLS:
        logging.info(f"Known unused pool has contents: {pool_name}")
    elif len(all_balances) == 0 and pool_name not in KNOWN_EMPTY_POOLS:
        logging.info(f"Empty pool not known to be so: {pool_name}")

    _known_itempools[pool_name] = all_balances
    return all_balances


def load_itempool_list(
    item_pool_list: str,
    world_drop_blacklist: Collection[str] = _ALL_DLCS
) -> set[str]:
    output = set()
    export = bl3dump.AssetFile(item_pool_list).get_single_export("ItemPoolListData")
    for pool in export.get("ItemPools", []):
        output.update(load_itempool_contents(pool["ItemPool"][1], world_drop_blacklist))

    for pool in HOTFIX_ITEMPOOLLISTS_ADD.get(item_pool_list, []):
        output.update(load_itempool_contents(pool, world_drop_blacklist))

    return output


# Need to be here to avoid circular references
from insert_enemies import insert_enemies, iter_enemy_drop_expansions  # noqa: E402
from insert_misc_sources import (insert_arms_race_chests, insert_misc_notable_pools,  # noqa: E402
                                 insert_world_drops)
from insert_missions import insert_missions  # noqa: E402


def _init_known_balances(con: sqlite3.Connection) -> None:
    global _known_balances
    cur = con.cursor()
    cur.execute("SELECT DISTINCT ObjectName FROM Items")
    _known_balances = {x[0] for x in cur.fetchall()}


def _init_itempool_expansions() -> None:
    all_expansions = set(ITEMPOOL_EXPANSIONS)
    for expansion_data in iter_enemy_drop_expansions():
        all_expansions.update(
            fix_dotted_object_name(expansion["asset_path_name"])
            for expansion in expansion_data["value"]["ItemPoolExpansions"]
        )

    for expansion in all_expansions:
        asset = bl3dump.AssetFile(expansion)

        for expansion_data in asset.iter_exports_of_class("ItemPoolExpansionData"):
            try:
                expanded_pool = fix_dotted_object_name(expansion_data["ItemPoolToExpand"][1])
            except (IndexError, KeyError):
                continue
            new_items = _get_balanced_items(expansion_data, _ALL_DLCS, expansion)

            if expanded_pool not in _known_itempool_expansions:
                _known_itempool_expansions[expanded_pool] = set()
            _known_itempool_expansions[expanded_pool].update(new_items)


def _get_balanced_items(
    data: bl3dump.JSON,
    world_drop_blacklist: Collection[str],
    obj_name: str
) -> set[str]:
    remove_data = HOTFIX_BALANCEDITEMS_REMOVE.get(obj_name, BalancedItemsEntry())

    all_balances = set()
    for item in data.get("BalancedItems", []):
        if (
            "ItemPoolData" in item
            and isinstance((nested_pool := item["ItemPoolData"]), list)
            and len(nested_pool) == 2
        ):
            nested_name = fix_dotted_object_name(nested_pool[1])
            if nested_name in remove_data.pools:
                continue
            all_balances.update(load_itempool_contents(nested_name, world_drop_blacklist))

        if (
            "InventoryBalanceData" in item
            and "asset_path_name" in (bal_struct := item["InventoryBalanceData"])
            and (bal_name := bal_struct["asset_path_name"]) != "None"
        ):
            if bal_name in remove_data.balances:
                continue
            all_balances.add(fix_dotted_object_name(bal_name))

    if obj_name in HOTFIX_BALANCEDITEMS_ADD:
        add_data = HOTFIX_BALANCEDITEMS_ADD[obj_name]
        for pool in add_data.pools:
            all_balances.update(load_itempool_contents(pool, world_drop_blacklist))
        all_balances.update(add_data.balances)

    filtered_balances = set()
    for balance in all_balances:
        if balance in EXPANDABLE_BALANCES:
            filtered_balances.update(EXPANDABLE_BALANCES[balance])
            continue
        elif balance not in _known_balances:
            continue

        filtered_balances.add(balance)

    return filtered_balances


def insert_all_sources(con: sqlite3.Connection) -> None:
    _init_known_balances(con)
    _init_itempool_expansions()

    insert_enemies(con)

    insert_misc_notable_pools(con)
    insert_arms_race_chests(con)
    insert_missions(con)
    insert_world_drops(con)
