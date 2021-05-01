import csv
import sqlite3
from dataclasses import dataclass
from typing import Optional

DB_PATH = "_uniques.sqlite3"
OUTPUT_SHEET = "hunt.csv"
MAIN_DROPS_SCRIPT = "demo/ghs_main_drops.sql"
WORLD_DROPS_SCROPT = "demo/ghs_world_drops.sql"

MAP_ORDER: tuple[Optional[str], ...] = (
    None,
    "Sanctuary",

    "Covenant Pass",
    "Droughts",
    "Ascension Bluff",
    "Devil's Razor",
    "Splinterlands",
    "Carnivora",
    "Guts of Carnivora",
    "Konrad's Hold",
    "Sandblast Scar",
    "Cathedral of the Twin Gods",
    "Great Vault",
    "Destroyer's Rift",
    "Slaughter Shaft",

    "Meridian Outskirts",
    "Meridian Metroplex",
    "Lectra City",
    "Skywell-27",
    "Atlas HQ",
    "Neon Arterial",
    "Forgotten Basilica",
    "Cistern of Slaughter",

    "Floodmoor Basin",
    "Anvil",
    "Jakobs Estate",
    "Voracious Canopy",
    "Ambermire",
    "Blackbarrel Cellars",
    "Floating Tomb",

    "Desolation's Edge",
    "Tazendeer Ruins",
    "Pyre of Stars",

    "Athenas",
    "Slaughterstar 3000",
    "Midnight's Cairn",
    "Minos Prime",

    "Ghostlight Beacon (Cunning)",
    "Gradient of Dawn (Survival)",
    "Precipice Anchor (Discipline)",
    "Hall Obsidian (Supremacy)",
    "Skydrowned Pulpit (Fervor)",
    "Wayward Tether (Instinct)",

    "Grand Opening",
    "Spendopticon",
    "Impound Deluxe",
    "Compactor",
    "Jack's Secret",
    "VIP Tower",

    "Skittermaw Basin",
    "Lodge",
    "Cursehaven",
    "Dustbound Archives",
    "Cankerwood",
    "Negul Neshai",
    "Heart's Desire",

    "Vestige",
    "Blastplains",
    "Ashfall Peaks",
    "Obsidian Forest",
    "Bloodsun Canyon",
    "Crater's Edge",

    "Psychoscape",
    "Castle Crimson",
    "Sapphire's Run",
    "Benediction of Pain",
    "Vaulthalla",

    "Stormblind Complex",

    "Darkthirst Dominion",
    "Eschaton Row",
    "Enoch's Grove",
    "Karass Canyon",
    "Scryer's Crypt",

    "Heck Hole",
    "Villa Ultraviolet",
)


@dataclass
class RowData:
    item_names: str
    description: str
    source: str
    world_drops: bool


con = sqlite3.connect(DB_PATH)


def get_all_item_names(item_id: int) -> str:
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


def get_item_description(item_id: int, rarity: str, gear_category: str) -> str:
    cur = con.cursor()
    cur.execute(
        "select Manufacturer from ManufacturedBy where ItemID = ?",
        (item_id,)
    )
    all_manus = [x[0] for x in cur.fetchall() if x[0] != "COM"]
    all_manus.sort()

    if len(all_manus) == 0:
        return f"{rarity} {gear_category}"
    else:
        return f"{rarity} {'/'.join(all_manus)} {gear_category}"


def can_item_world_drop(item_id: int) -> bool:
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


drops_by_map: dict[Optional[str], list[RowData]] = {
    None: []
}

main_cursor = con.cursor()
main_cursor.execute(open(MAIN_DROPS_SCRIPT).read())  # noqa: SIM115
for (
    item_id,
    rarity,
    gear_category,
    source,
    map_name,
) in main_cursor.fetchall():
    if map_name not in drops_by_map:
        drops_by_map[map_name] = []
    drops_by_map[map_name].append(RowData(
        get_all_item_names(item_id),
        get_item_description(item_id, rarity, gear_category),
        source,
        can_item_world_drop(item_id)
    ))

main_cursor.execute(open(WORLD_DROPS_SCROPT).read())  # noqa: SIM115
for (
    item_id,
    rarity,
    gear_category,
    source,
) in main_cursor.fetchall():
    drops_by_map[None].append(RowData(
        get_all_item_names(item_id),
        get_item_description(item_id, rarity, gear_category),
        source,
        can_item_world_drop(item_id)
    ))


for map_drops in drops_by_map.values():
    for i, row_data in enumerate(map_drops):
        all_sources = row_data.source.split(" / ")
        for row_data_2 in map_drops[i + 1:]:
            if row_data.item_names != row_data_2.item_names:
                continue
            all_sources.extend(row_data_2.source.split(" / "))
            map_drops.remove(row_data_2)

        all_sources.sort()
        row_data.source = " / ".join(all_sources)

with open(OUTPUT_SHEET, "w", newline="", encoding="utf8") as file:
    writer = csv.writer(file)
    writer.writerow(["Item(s)", "Description", "Source", "", "Points"])

    for map_name in MAP_ORDER:
        if map_name not in drops_by_map:
            continue

        writer.writerow([
            "- Any Map / Misc -"
            if map_name is None else
            f"- {map_name} -"
        ])
        for row in drops_by_map[map_name]:
            writer.writerow([
                row.item_names,
                row.description,
                row.source,
                "WD" if row.world_drops else "",
                10
            ])
