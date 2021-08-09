import sqlite3
from typing import Optional

DB_PATH = "_uniques.sqlite3"


def get_all_item_names(con: sqlite3.Connection, item_id: int) -> str:
    cur = con.cursor()
    cur.execute(
        "select Name from Items where ID = ?",
        (item_id,)
    )
    all_names = [cur.fetchone()[0]]

    cur.execute(
        "select VariantName from Variants where ItemID = ?",
        (item_id,)
    )
    all_names.extend(x[0] for x in cur.fetchall())
    all_names.sort()

    return " / ".join(all_names)


def get_item_manufacturers(con: sqlite3.Connection, item_id: int) -> list[str]:
    cur = con.cursor()
    cur.execute(
        "select Manufacturer from ManufacturedBy where ItemID = ?",
        (item_id,)
    )
    return [x[0] for x in cur.fetchall()]


def get_item_description(
    con: sqlite3.Connection,
    item_id: int,
    rarity: str,
    gear_category: str,
    req_class: Optional[str]
) -> str:
    output = rarity + " "

    if (all_manus := sorted([x for x in get_item_manufacturers(con, item_id) if x != "COM"])):
        output += "/".join(all_manus) + " "

    if req_class:
        output += req_class + " "

    return output + gear_category


def can_item_world_drop(con: sqlite3.Connection, item_id: int) -> bool:
    cur = con.cursor()
    cur.execute(
        """
        select count(*) from
            ObtainedFrom as o,
            Sources as s
        where
            o.ItemID = ?
            and o.SourceID = s.ID
            and s.SourceType = "World Drop"
        """,
        (item_id,)
    )
    return bool(cur.fetchone()[0] > 0)
