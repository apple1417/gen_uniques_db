import logging
import sqlite3
from dataclasses import dataclass
from typing import Iterator

import bl3dump
from data.missions import (EXTRA_MISSION_REWARDS, MISSION_NAME_OVERRIDES, MISSION_PATH_GLOBS,
                           MISSION_WEAPON_BLACKLIST)
from itempool_handling import load_itempool_contents


@dataclass
class MissionData:
    mission_name: str
    object_name: str
    rewards: set[str]


def iter_missions() -> Iterator[MissionData]:
    for pattern in MISSION_PATH_GLOBS:
        for asset in bl3dump.glob(pattern):
            if not isinstance(asset, bl3dump.AssetFile):
                continue

            mission_data = asset.get_single_export(asset.name + "_C")
            name = mission_data["FormattedMissionName"]["FormatText"]["string"]
            obj_name = asset.path + "." + mission_data["_jwp_object_name"]

            rewards = set()
            for cls in ("OakMissionRewardData", "OakOptionalObjectiveRewardData"):
                for data in asset.iter_exports_of_class(cls):
                    if "ItemPoolReward" not in data:
                        continue
                    reward_pool = data["ItemPoolReward"]["asset_path_name"]
                    rewards.update(load_itempool_contents(reward_pool))

            if obj_name in EXTRA_MISSION_REWARDS:
                rewards.update(EXTRA_MISSION_REWARDS[obj_name])

            if obj_name in MISSION_NAME_OVERRIDES:
                name = MISSION_NAME_OVERRIDES[obj_name]
            elif "{" in name or "}" in name:
                logging.info(f"Ignoring mission with placeholder name: {obj_name}")
                continue

            if len(rewards) > 0:
                yield MissionData(name, obj_name, rewards)

            if (
                obj_name not in MISSION_WEAPON_BLACKLIST
                and "MissionWeaponBalanceData" in mission_data
            ):
                yield MissionData(
                    name + " (Mission Weapon)",
                    obj_name,
                    {mission_data["MissionWeaponBalanceData"]["asset_path_name"]}
                )


def insert_missions(con: sqlite3.Connection) -> None:
    cur = con.cursor()

    for mission_data in iter_missions():
        cur.execute(
            """
            INSERT INTO Sources (SourceType, Description, ObjectName) VALUES (
                "Mission",
                ?,
                ?
            )
            """,
            (mission_data.mission_name, mission_data.object_name)
        )
        row_id = cur.lastrowid

        for balance in mission_data.rewards:
            cur.execute(
                """
                INSERT INTO ObtainedFrom (ItemID, SourceID) VALUES (
                    (SELECT ID FROM Items WHERE ObjectName = ?),
                    ?
                )
                """,
                (balance, row_id)
            )

    con.commit()
