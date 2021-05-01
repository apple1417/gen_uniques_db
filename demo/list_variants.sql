select
    i.Name,
    v.VariantName
from
    Items as i,
    Variants as v
where
    i.ID = v.ItemID
