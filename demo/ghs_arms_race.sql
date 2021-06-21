-- This script is used by gen_hunt_sheet.py, don't edit it
select
    i.ID,
    i.Rarity,
    i.GearCategory,
    i.RequiredClass,
    s.Description,
    s.Map
from
    Items as i,
    Sources as s,
    ObtainedFrom as o
where
    i.ID = o.ItemID
    and o.SourceID = s.ID

    and s.Description = "Arms Race Chest Room"
order by
    s.Map,
    s.Description,
    i.Name
