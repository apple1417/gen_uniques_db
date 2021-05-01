import sqlite3

from data.itempools import WORLD_DROP_POOLS
from data.misc_sources import MISC_NOTABLE_BALANCES, MISC_NOTABLE_POOLS, WORLD_DROP_MAP_OVERRIDE
from itempool_handling import _ALL_DLCS, load_itempool_contents


def insert_world_drops(con: sqlite3.Connection) -> None:
    cur = con.cursor()

    for dlc in _ALL_DLCS:
        cur.execute(
            """
            INSERT INTO Sources (SourceType, Map, Description, ObjectName) VALUES (
                "World Drop",
                ?,
                ?,
                NULL
            )
            """,
            (WORLD_DROP_MAP_OVERRIDE.get(dlc, None), f"World Drop ({dlc})")
        )
        row_id = cur.lastrowid

        for pool in WORLD_DROP_POOLS[dlc]:
            for balance in load_itempool_contents(pool, {x for x in _ALL_DLCS if x != dlc}):
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


def insert_arms_race_chests(con: sqlite3.Connection) -> None:
    """
    This is kind of a hack - we know all the arms race items have a dedicated chest, so we can just
    go through the world drop pool to find all the items and add them to a chest source directly.

    It's simpler than finding chest object references for each ¯\_(ツ)_/¯
    """  # noqa: W605

    cur = con.cursor()
    cur.execute(
        """
        INSERT INTO Sources (SourceType, Map, Description, ObjectName) VALUES (
            "Misc",
            "Stormblind Complex",
            "Arms Race Chest Rooms",
            NULL
        )
        """
    )
    row_id = cur.lastrowid

    dlc_blacklist = {x for x in _ALL_DLCS if x != "Arms Race"}
    for pool in WORLD_DROP_POOLS["Arms Race"]:
        for balance in load_itempool_contents(pool, dlc_blacklist):
            cur.execute(
                """
                INSERT INTO ObtainedFrom (ItemID, SourceID) VALUES (
                    (SELECT ID FROM Items WHERE ObjectName = ?),
                    ?
                )
                """,
                (balance, row_id)
            )


def insert_misc_notable_pools(con: sqlite3.Connection) -> None:
    cur = con.cursor()

    for source, all_pools in MISC_NOTABLE_POOLS.items():
        cur.execute(
            """
            INSERT INTO Sources (SourceType, Map, Description, ObjectName) VALUES (
                "Misc",
                ?,
                ?,
                NULL
            )
            """,
            (source.map_name, source.description)
        )
        row_id = cur.lastrowid

        blacklist = set() if source.include_world_drops else _ALL_DLCS

        all_balances = set()
        for pool in all_pools:
            all_balances.update(load_itempool_contents(pool, blacklist))

        for balance in all_balances:
            cur.execute(
                """
                INSERT INTO ObtainedFrom (ItemID, SourceID) VALUES (
                    (SELECT ID FROM Items WHERE ObjectName = ?),
                    ?
                )
                """,
                (balance, row_id)
            )

    for source, all_balances in MISC_NOTABLE_BALANCES.items():
        cur.execute(
            """
            INSERT INTO Sources (SourceType, Map, Description, ObjectName) VALUES (
                "Misc",
                ?,
                ?,
                NULL
            )
            """,
            (source.map_name, source.description)
        )
        row_id = cur.lastrowid

        for balance in all_balances:
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
