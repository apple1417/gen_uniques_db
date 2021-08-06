select
    i.Name,
    i.Rarity,
    m.Manufacturer,
    i.RequiredClass,
    i.GearCategory,
    i.ItemGroup
from
    Items as i,
    (
        select
            *
        from
            ManufacturedBy
        group by
            ItemID
    ) as m
where
    i.ID = m.ItemID
order by
    i.ItemGroup,
    i.Name
