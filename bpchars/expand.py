import csv
import logging
import os
import sys

# Bad hack to let this work as a standalone script in a lower folder
sys.path.insert(0, os.path.abspath("."))

import bl3dump  # noqa: E402
from util import fix_dotted_object_name  # noqa: E402

"""
Converts the bpchar object names in `base.csv` into full paths in `expanded.csv`. This is a
relatively slow operation (uses a big glob), so we don't want to do it every time we update the db.

This script does spit out a few of warnings I haven't hardcoded out but it's easy enough to look
through them manually.

`base.csv` should be the "Charachter Names" sheet from this doc:
https://docs.google.com/spreadsheets/d/1mJEohWGAvhdVxq55wACFZI0eqtsoUaTAZKMVj0AlgIk/edit#gid=1336583565
"""


logging.basicConfig(level=logging.INFO)

short_bpchars = {}
header: tuple[str, ...]
with open("bpchars/base.csv") as file:
    reader = csv.reader(file)
    header = next(reader)  # type: ignore
    for idx, row in enumerate(reader):
        short_bpchars[row[0]] = (idx, row[1:])

full_bpchars = {}
found = set()
for asset in bl3dump.glob("**/BPChar_*"):
    if asset.name not in short_bpchars:
        logging.warning(f"Unknown BPChar: {asset.path}")
        continue
    full_bpchars[fix_dotted_object_name(asset.path)] = short_bpchars[asset.name]
    found.add(asset.name)

for bpchar in short_bpchars:
    if bpchar not in found:
        logging.warning(f"Couldn't find full bpchar for {bpchar}")

with open("bpchars/expanded.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for bpchar, (_, row) in sorted(full_bpchars.items(), key=lambda x: x[1][0]):
        writer.writerow((bpchar, *row))
