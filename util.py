import re
import sqlite3
from collections.abc import Iterator

REFS_CON = sqlite3.connect("bl3refs.sqlite3")

RE_OBJECT_NAME = re.compile(r"(?P<Path>/(\S+?/)+)(?P<FileName>[^.\s]+)(\.(?P<ObjectName>\S+))?")


def fix_dotted_object_name(obj_name: str) -> str:
    match = RE_OBJECT_NAME.match(obj_name)
    if match is None:
        raise ValueError(f"Invalid object name: {obj_name}")
    if match.group("ObjectName") is not None:
        return obj_name

    return (
        match.group("Path")
        + match.group("FileName")
        + "."
        + match.group("FileName")
    )


def _iter_refs(obj_name: str, to: bool) -> Iterator[str]:
    match = RE_OBJECT_NAME.match(obj_name)
    if match is None:
        raise ValueError(f"Invalid object name: {obj_name}")
    trimmed_name = match.group("Path") + match.group("FileName")

    cmd = """
        SELECT
            o.name
        FROM
            bl3object as o,
            bl3refs as r
        WHERE
    """
    if to:
        cmd += """
            r.from_obj = o.id
            AND r.to_obj = (
                SELECT id FROM bl3object WHERE name = ?
            )
        """
    else:
        cmd += """
            r.to_obj = o.id
            AND r.from_obj = (
                SELECT id FROM bl3object WHERE name = ?
            )
        """

    cur = REFS_CON.cursor()
    cur.execute(cmd, (trimmed_name,))
    for row in cur.fetchall():
        yield fix_dotted_object_name(row[0])


def iter_refs_to(obj_name: str) -> Iterator[str]:
    yield from _iter_refs(obj_name, True)


def iter_refs_from(obj_name: str) -> Iterator[str]:
    yield from _iter_refs(obj_name, False)
