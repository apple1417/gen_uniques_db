import unrealsdk
import json
from typing import Optional, Set

"""
This file uses the (wip) BL3 PythonSDK to generate some JSON dumps for use with the generation
scripts. Originally I manually fixed up the dumps, hence the two steps. There are a number of
reasons I left it like this:

The `sqlite3` module relies on a C extension, which is a little harder to get working in the sdk.
It's awkward needing to load objects to access them via sdk.
It's nice not needing the game open while working on this stuff.
Trying to use only extracted assets requires reading everything from disk, which is much slower than
 from objects already loaded in memory.

MAKE SURE NOT TO HAVE HOTFIXES WHEN RUNNING THIS FOR CONSISTENCY'S SAKE.
"""

INVBAL_CLS_BLACKLIST = (
    "CustomizationInventoryBalanceData",
    "InventoryBalanceData_Generated",  # Echo logs
)


def name(obj: unrealsdk.UObject) -> Optional[str]:
    if obj is None:
        return None
    if not isinstance(obj, unrealsdk.UObject):
        raise ValueError(f"'{str(obj)}' is not an object")
    return str(obj).split(" ")[-1]


names_from_strategy = {}
for obj in unrealsdk.FindAll("OakInventoryNamingStrategyData"):
    for entry in obj.SingleNames:
        if None in (entry.Part, entry.NamePart):
            continue
        names_from_strategy[name(entry.Part)] = entry.NamePart.PartName


all_items = {}
for obj in unrealsdk.FindAll("InventoryBalanceData"):
    if obj.Class.Name in INVBAL_CLS_BLACKLIST:
        continue
    obj_name = name(obj)

    all_names: Set[str] = set()
    for field_names in (("RuntimePartList", "AllParts"), ("RuntimeGenericPartList", "PartList")):
        part_list = getattr(obj, field_names[0])
        if part_list is None:
            continue
        for part_struct in getattr(part_list, field_names[1], []):
            part = part_struct.PartData
            if part is None:
                continue

            part_name = name(part)
            if part_name in names_from_strategy:
                all_names.add(names_from_strategy[part_name])

            for title in part.TitlePartList:
                if title.PartName is not None:
                    all_names.add(title.PartName)

    req_class = None
    if obj.InventoryData:
        req_class = name(obj.InventoryData.RequiredPlayerClass)

    all_items[obj_name] = {
        "RarityData": name(obj.RarityData),
        "GearBuilderCategory": name(obj.GearBuilderCategory),
        "DlcInventorySetData": name(obj.DlcInventorySetData),
        "Manufacturers": [name(m.ManufacturerData) for m in obj.Manufacturers],
        "Names": list(all_names),
        "RequiredClass": req_class
    }


# Had some issues getting these objects to load, so add them manually
all_items["/Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick_Legendary.Balance_SM_HYP_ShortStick_Legendary"] = {
    "RarityData": "/Game/GameData/Loot/RarityData/RarityData_05_Legendary.RarityData_05_Legendary",
    "GearBuilderCategory": "/Game/Gear/_Shared/_Design/GearBuilder/Category_SMGs.Category_SMGs",
    "DlcInventorySetData": None,
    "Manufacturers": [
        "/Game/Gear/Manufacturers/_Design/Hyperion.Hyperion"
    ],
    "Names": [
        "Short Stick (Legendary)"
    ],
    "RequiredClass": None
}
all_items["/Game/PatchDLC/Steam/Gear/Weapons/SteamGun/Balance/Balance_SM_HYP_ShortStick.Balance_SM_HYP_ShortStick"] = {
    "RarityData": "/Game/GameData/Loot/RarityData/RarityData_04_VeryRare.RarityData_04_VeryRare",
    "GearBuilderCategory": "/Game/Gear/_Shared/_Design/GearBuilder/Category_SMGs.Category_SMGs",
    "DlcInventorySetData": None,
    "Manufacturers": [
        "/Game/Gear/Manufacturers/_Design/Hyperion.Hyperion"
    ],
    "Names": [
        "Short Stick (Purple)"
    ],
    "RequiredClass": None
}

with open("item_dump.json", "w") as file:
    json.dump(all_items, file, indent=4)
