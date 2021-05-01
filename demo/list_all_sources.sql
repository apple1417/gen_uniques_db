select
    i.Name,
    i.Rarity,
    m.Manufacturer,
    i.GearCategory,
    i.ItemGroup,
    s.SourceType,
    s.Description,
    s.Map
from
    Items as i,
    ManufacturedBy as m,
    Sources as s,
    ObtainedFrom as o
where
    i.ID = m.ItemID
    and i.ID = o.ItemID
    and o.SourceID = s.ID
order by
    i.Name,
    s.Description
