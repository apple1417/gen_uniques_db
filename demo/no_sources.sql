select
    i.Name,
    i.Rarity,
    m.Manufacturer,
    i.GearCategory,
    i.ItemGroup,
    i.ObjectName
from
    Items as i,
    ManufacturedBy as m
where
    i.ID = m.ItemID
    and (
        select count(*)
        from ObtainedFrom as o
        where i.ID = o.ItemID
    ) = 0
order by
    i.Name
