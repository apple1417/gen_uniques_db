import csv
import sqlite3
from dataclasses import dataclass
from typing import Optional

from util import DB_PATH, can_item_world_drop, get_all_item_names, get_item_description

OUTPUT_SHEET = "hunt.csv"

DROP_SCRIPTS: tuple[str, ...] = (
    "demo/ghs_arms_race.sql",
    "demo/ghs_main_drops.sql",
    "demo/ghs_world_drops.sql",
)

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

ROW_MARKER_OVERRIDES: dict[str, str] = {
    "Antifreeze": "M4",
    "Crader's EM-P5": "M4",
    "Good Juju": "M4",
    "Juliet's Dazzle": "M4",
    "R4kk P4k": "M4",
    "Raging Bear": "M4",
    "S3RV-80S-EXECUTE": "M4",
    "Spiritual Driver": "M4",
    "Tankman's Shield": "M4",
    "Vosk's Deathgrip": "M4",
    "Zheitsev's Eruption": "M4",

    "Backburner": "M6",
    "D.N.A.": "M6",
    "Kaoson": "M6",
    "Multi-tap": "M6",
    "Plaguebearer": "M6",
    "Reflux": "M6",
    "Sand Hawk": "M6",
    "The Monarch": "M6",

    "Polyaimourous": "L53",
    "Wedding Invitation": "L53",
}

TRUE_TRIAL_SUFFIX: str = " (True Trial)"


@dataclass
class RowData:
    item_names: str
    description: str
    source: str
    world_drops: bool


drops_by_map: dict[Optional[str], list[RowData]] = {}

con = sqlite3.connect(DB_PATH)
cur = con.cursor()
for script in DROP_SCRIPTS:
    with open(script) as file:
        cur.execute(file.read())
    for (
        item_id,
        rarity,
        gear_category,
        req_class,
        source,
        map_name,
    ) in cur.fetchall():
        if map_name not in drops_by_map:
            drops_by_map[map_name] = []
        drops_by_map[map_name].append(RowData(
            get_all_item_names(con, item_id),
            get_item_description(con, item_id, rarity, gear_category, req_class),
            source,
            can_item_world_drop(con, item_id)
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
    writer.writerow(["Item(s)", "Description", "Source", "", "Value"])

    for map_name in MAP_ORDER:
        if map_name not in drops_by_map:
            continue

        writer.writerow([
            map_name or "Misc",
            "----------------",
            "----------------",
            "----------------",
            "----------------",
        ])

        drops = drops_by_map[map_name]

        # We want the final list to be sorted by enemy first and item name second
        drops.sort(key=lambda x: x.item_names)
        # Ignore true trials, we'll strip that out into a marker in the next step
        drops.sort(key=lambda x: x.source.removesuffix(TRUE_TRIAL_SUFFIX))

        for row in drops:
            marker = ""
            if row.source.endswith(TRUE_TRIAL_SUFFIX):
                row.source = row.source.removesuffix(TRUE_TRIAL_SUFFIX)
                marker = "TT"
            # Want true trial to overwrite mayhem markers
            elif row.item_names in ROW_MARKER_OVERRIDES:
                marker = ROW_MARKER_OVERRIDES[row.item_names]
            elif row.world_drops:
                marker = "WD"

            writer.writerow([
                row.item_names,
                row.description,
                row.source,
                marker,
                5
            ])
