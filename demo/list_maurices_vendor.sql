select
    i.Name,
    s.Description
from
    Items as i,
    Sources as s,
    ObtainedFrom as o
where
    i.ID = o.ItemID
    and o.SourceID = s.ID

    and s.Description like "Maurice's Vendor%"
order by
    CAST(
        SUBSTR(s.Description, 23, LENGTH(s.Description) - 23)
        as int
    ),
    i.Name
