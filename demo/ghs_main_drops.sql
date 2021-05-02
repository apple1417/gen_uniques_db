-- This script is used by gen_hunt_sheet.py, don't edit it
select
    i.ID,
    i.Rarity,
    i.GearCategory,
    s.Description,
    s.Map
from
    Items as i,
    Sources as s,
    ObtainedFrom as o
where
    i.ID = o.ItemID
    and o.SourceID = s.ID

    and i.ItemGroup != "Booster Pack"
    and i.ItemGroup != "Butt Stallion Pack"
    and i.ItemGroup != "Toy Box Pack"
    and i.ItemGroup != "Vault Card"

    and s.SourceType != "World Drop"
    and s.SourceType != "Mission"

    and s.Description != "Bank of Vestige"
    and s.Description != "Dalton's Chest"
    and s.Description != "Diamond Chest"
    and s.Description != "Earl's Vendor"
    and s.Description != "Eridian Fabricator"
    and s.Description != "Life of the Party Pinata"
    and s.Description != "Maliwan Depot Chest"
    and s.Description != "Vincent"
order by
    s.Map,
    s.Description,
    i.Name
