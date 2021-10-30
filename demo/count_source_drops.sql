select
    count(o.ID),
    s.SourceType,
    s.Description,
    s.Map
from
    Sources as s,
    ObtainedFrom as o
where
    o.SourceID = s.ID
group by
    s.Description
order by
    count(o.ID)
    desc
