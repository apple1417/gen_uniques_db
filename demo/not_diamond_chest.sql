select distinct
    i.Name,
    i.Rarity,
    m.Manufacturer,
    i.GearCategory,
    i.ItemGroup
from
    Items as i,
    ManufacturedBy as m,
    Sources as s,
    ObtainedFrom as o
where
    i.ID = m.ItemID
    and i.ID = o.ItemID
    and o.SourceID = s.ID

    and (
        select
            count(*)
        from
            Items as i2,
            Sources as s2,
            ObtainedFrom as o2
        where
            i2.ID = i.ID
            and i2.ID = o2.ItemID
            and o2.SourceID = s2.ID

            and s2.Description == "Diamond Chest"
    ) = 0
order by
    i.ItemGroup,
    i.Name
