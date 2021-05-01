import json
import logging
import re
import sqlite3
from collections.abc import Iterator
from dataclasses import dataclass

from data.constants import GEAR_CATEGORIES, MANUFACTURERS, RARITIES
from data.items import (BALANCE_BLACKLIST, GEAR_CATEGORY_OVERRIDES, INVENTORY_SET_ITEM_GROUP,
                        ITEM_GROUP_OVERRIDES, MANUFACTURER_CONVERSIONS, NAME_OVERRIDES,
                        NON_UNIQUE_NAMES, PATCHDLC_ITEM_GROUP)

part_title_cache: dict[str, set[str]] = {}

VALID_GEAR_CATEGORIES = {x[1] for x in GEAR_CATEGORIES}
VALID_MANUFACTURERS = {x[1] for x in MANUFACTURERS}
VALID_RARITIES = {x[1] for x in RARITIES}

RE_PATCHDLC = re.compile("/Game/PatchDLC/(.+?)/")

ITEM_DUMP_PATH: str = "sdk/item_dump.json"


@dataclass
class BalanceData:
    rarity: str
    category: str
    item_group: str
    names: set[str]
    obj_name: str
    manufacturers: set[str]


def iter_balances() -> Iterator[BalanceData]:
    with open(ITEM_DUMP_PATH) as file:
        for obj_name, data in json.load(file).items():
            if obj_name in BALANCE_BLACKLIST:
                continue

            rarity = data["RarityData"]
            if rarity not in VALID_RARITIES:
                logging.info(f"Skipping due to invalid rarity: {obj_name}")
                continue

            category: str
            if obj_name in GEAR_CATEGORY_OVERRIDES:
                category = GEAR_CATEGORY_OVERRIDES[obj_name]
            else:
                category = data["GearBuilderCategory"]

            item_group = "Base Game"
            if obj_name in ITEM_GROUP_OVERRIDES:
                item_group = ITEM_GROUP_OVERRIDES[obj_name]
            elif (inv_set := data["DlcInventorySetData"]) is not None:
                item_group = INVENTORY_SET_ITEM_GROUP[inv_set]
            else:
                match = RE_PATCHDLC.match(obj_name)
                if match is not None and (patchdlc := match.group(1)) in PATCHDLC_ITEM_GROUP:
                    item_group = PATCHDLC_ITEM_GROUP[patchdlc]

            if category not in VALID_GEAR_CATEGORIES:
                logging.info(f"Skipping due to invalid gear category: {obj_name}")
                continue

            names = {x for x in data["Names"] if x not in NON_UNIQUE_NAMES}
            if obj_name in NAME_OVERRIDES:
                names = NAME_OVERRIDES[obj_name]
            elif len(names) == 0:
                logging.info(f"Skipping due to no names: {obj_name}")
                continue
            elif len(names) > 1:
                logging.info(f"Skipping unknown balance with multiple names: {obj_name}")
                continue

            all_manus = set()
            for manu in data["Manufacturers"]:
                if manu in MANUFACTURER_CONVERSIONS:
                    all_manus.add(MANUFACTURER_CONVERSIONS[manu])
                elif manu in VALID_MANUFACTURERS:
                    all_manus.add(manu)

            if len(all_manus) == 0:
                logging.info(f"Skipping due to no manufacturers: {obj_name}")
                continue

            yield BalanceData(rarity, category, item_group, names, obj_name, all_manus)


def insert_items(con: sqlite3.Connection) -> None:
    cur = con.cursor()

    for balance in iter_balances():
        base_name = balance.names.pop()

        cur.execute(
            """
            INSERT INTO Items (Rarity, GearCategory, ItemGroup, Name, ObjectName) VALUES (
                (SELECT Name FROM Rarities WHERE ObjectName = ?),
                (SELECT Name FROM GearCategories WHERE ObjectName = ?),
                ?,
                ?,
                ?
            )
            """,
            (balance.rarity, balance.category, balance.item_group, base_name, balance.obj_name)
        )
        row_id = cur.lastrowid

        for name in balance.names:
            cur.execute(
                "INSERT INTO Variants (ItemID, VariantName) VALUES (?, ?)",
                (row_id, name)
            )

        for manufacturer in balance.manufacturers:
            cur.execute(
                """
                INSERT INTO ManufacturedBy (ItemID, Manufacturer) VALUES (
                    ?,
                    (SELECT Name FROM Manufacturers WHERE ObjectName = ?)
                )
                """,
                (row_id, manufacturer)
            )

    con.commit()

    cur.execute("SELECT COUNT(*), COUNT(DISTINCT Name) FROM Items")
    total_count, distinct_count = cur.fetchone()
    if total_count != distinct_count:
        logging.error("Multiple items have the same name!")
