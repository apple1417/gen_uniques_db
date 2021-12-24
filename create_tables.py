import sqlite3
from datetime import datetime

from data.constants import (GEAR_CATEGORIES, ITEM_GROUPS, MANUFACTURERS, MAPS, PLAYER_CLASSES,
                            RARITIES, SOURCE_TYPES)


def create_tables(con: sqlite3.Connection) -> None:
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE MetaData (
            Key   TEXT NOT NULL UNIQUE,
            Value TEXT NOT NULL,
            PRIMARY KEY(Key)
        );
        """
    )
    cur.execute(
        """
        INSERT INTO MetaData (Key, Value) VALUES
            ("Version", "11"),
            ("GeneratedTime", ?);
        """,
        (datetime.utcnow().strftime("%Y%m%d%H%M%S"),)
    )

    cur.execute(
        """
        CREATE TABLE Rarities (
            Name       TEXT NOT NULL UNIQUE,
            ObjectName TEXT NOT NULL UNIQUE,
            PRIMARY KEY(Name),
            UNIQUE(Name, ObjectName)
        );
        """
    )
    for name, obj_name in RARITIES:
        cur.execute(
            "INSERT INTO Rarities (Name, ObjectName) VALUES (?, ?);",
            (name, obj_name)
        )

    cur.execute(
        """
        CREATE TABLE GearCategories (
            Name       TEXT NOT NULL UNIQUE,
            ObjectName TEXT NOT NULL UNIQUE,
            PRIMARY KEY(Name),
            UNIQUE(Name, ObjectName)
        );
        """
    )
    for name, obj_name in GEAR_CATEGORIES:
        cur.execute(
            "INSERT INTO GearCategories (Name, ObjectName) VALUES (?, ?);",
            (name, obj_name)
        )

    cur.execute(
        """
        CREATE TABLE ItemGroups (
            Name       TEXT NOT NULL UNIQUE,
            PRIMARY KEY(Name)
        );
        """
    )
    for name in ITEM_GROUPS:
        cur.execute(
            "INSERT INTO ItemGroups (Name) VALUES (?);",
            (name,)
        )

    cur.execute(
        """
        CREATE TABLE Manufacturers (
            Name       TEXT NOT NULL UNIQUE,
            ObjectName TEXT NOT NULL UNIQUE,
            PRIMARY KEY(Name),
            UNIQUE(Name, ObjectName)
        );
        """
    )
    for name, obj_name in MANUFACTURERS:
        cur.execute(
            "INSERT INTO Manufacturers (Name, ObjectName) VALUES (?, ?);",
            (name, obj_name)
        )

    cur.execute(
        """
        CREATE TABLE SourceTypes (
            Name       TEXT NOT NULL UNIQUE,
            PRIMARY KEY(Name)
        );
        """
    )
    for name in SOURCE_TYPES:
        cur.execute(
            "INSERT INTO SourceTypes (Name) VALUES (?);",
            (name,)
        )

    cur.execute(
        """
        CREATE TABLE Maps (
            Name       TEXT NOT NULL UNIQUE,
            ObjectName TEXT NOT NULL UNIQUE,
            PRIMARY KEY(Name),
            UNIQUE(Name, ObjectName)
        );
        """
    )
    for name, obj_name in MAPS:
        cur.execute(
            "INSERT INTO Maps (Name, ObjectName) VALUES (?, ?);",
            (name, obj_name)
        )

    cur.execute(
        """
        CREATE TABLE PlayerClass (
            Name       TEXT NOT NULL UNIQUE,
            ObjectName TEXT NOT NULL UNIQUE,
            PRIMARY KEY(Name),
            UNIQUE(Name, ObjectName)
        );
        """
    )
    for name, obj_name in PLAYER_CLASSES:
        cur.execute(
            "INSERT INTO PlayerClass (Name, ObjectName) VALUES (?, ?);",
            (name, obj_name)
        )

    cur.execute(
        """
        CREATE TABLE Items (
            ID            INTEGER NOT NULL UNIQUE,
            Rarity        TEXT NOT NULL,
            GearCategory  TEXT NOT NULL,
            ItemGroup     TEXT NOT NULL,
            RequiredClass TEXT,
            Name          TEXT NOT NULL UNIQUE,
            ObjectName    TEXT NOT NULL UNIQUE,
            PRIMARY KEY(ID AUTOINCREMENT),
            FOREIGN KEY(Rarity)        REFERENCES Rarities(Name),
            FOREIGN KEY(GearCategory)  REFERENCES GearCategories(Name),
            FOREIGN KEY(ItemGroup)     REFERENCES ItemGroups(Name),
            FOREIGN KEY(RequiredClass) REFERENCES PlayerClass(Name)
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE ManufacturedBy (
            ID           INTEGER NOT NULL UNIQUE,
            ItemID       INTEGER NOT NULL,
            Manufacturer TEXT NOT NULL,
            PRIMARY KEY(ID AUTOINCREMENT),
            FOREIGN KEY(ItemID)       REFERENCES Items(ID),
            FOREIGN KEY(Manufacturer) REFERENCES Manufacturers(Name),
            UNIQUE(ItemID, Manufacturer)
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE Variants (
            ID          INTEGER NOT NULL UNIQUE,
            ItemID      INTEGER NOT NULL,
            VariantName TEXT NOT NULL UNIQUE,
            PRIMARY KEY(ID AUTOINCREMENT),
            FOREIGN KEY(ItemID) REFERENCES Items(ID)
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE Sources (
            ID          INTEGER NOT NULL UNIQUE,
            SourceType  TEXT NOT NULL,
            Map         TEXT,
            Description TEXT NOT NULL UNIQUE,
            ObjectName  TEXT,
            PRIMARY KEY(ID AUTOINCREMENT),
            FOREIGN KEY(SourceType) REFERENCES SourceTypes(Name),
            FOREIGN KEY(Map)        REFERENCES Maps(Name)
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE ObtainedFrom (
            ID         INTEGER NOT NULL UNIQUE,
            ItemID     INTEGER NOT NULL,
            SourceID   INTEGER NOT NULL,
            PRIMARY KEY(ID AUTOINCREMENT),
            FOREIGN KEY(ItemID)   REFERENCES Items(ID),
            FOREIGN KEY(SourceID) REFERENCES Sources(ID),
            UNIQUE(ItemID, SourceID)
        );
        """
    )

    con.commit()
