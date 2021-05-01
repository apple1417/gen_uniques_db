import logging
import os
import sqlite3

from create_tables import create_tables
from insert_items import insert_items
from itempool_handling import insert_all_sources

DB_PATH: str = "_uniques.sqlite3"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        os.remove(DB_PATH)
    except FileNotFoundError:
        pass
    con = sqlite3.connect(DB_PATH)
    con.cursor().execute("PRAGMA foreign_keys = ON")

    create_tables(con)
    insert_items(con)
    insert_all_sources(con)
