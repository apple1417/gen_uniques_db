select
    distinct i.Name,
    i.Rarity,
    m.Manufacturer,
    i.RequiredClass,
    i.GearCategory,
    i.ItemGroup
from
    Items as i,
    ManufacturedBy as m
where
    i.ID = m.ItemID
order by
    i.ItemGroup,
    i.Name
