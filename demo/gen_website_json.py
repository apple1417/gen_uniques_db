import json
import sqlite3

from util import DB_PATH, get_all_item_names, get_item_description, get_item_manufacturers

OUTPUT_FILE = "uniques.json"

all_sources = []

con = sqlite3.connect(DB_PATH)
cur = con.cursor()

cur.execute("""
select
    i.ID,
    i.Rarity,
    i.GearCategory,
    i.RequiredClass,
    i.ItemGroup,
    s.Description,
    s.Map
from
    Items as i,
    Sources as s,
    ObtainedFrom as o
where
    i.ID = o.ItemID
    and o.SourceID = s.ID
""")
for (
    item_id,
    rarity,
    gear_category,
    req_class,
    item_group,
    source,
    map
) in cur.fetchall():
    all_sources.append([
        get_all_item_names(con, item_id),
        get_item_description(con, item_id, rarity, gear_category, req_class),
        source,
        map,
        rarity,
        get_item_manufacturers(con, item_id),
        req_class,
        gear_category,
        item_group,
    ])

with open(OUTPUT_FILE, "w") as file:
    json.dump({"data": all_sources}, file, separators=(",", ":"))
