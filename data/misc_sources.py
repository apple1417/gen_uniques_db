from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class MiscSource:
    description: str
    map_name: Optional[str] = None
    include_world_drops: bool = False


WORLD_DROP_MAP_OVERRIDE: dict[str, str] = {
    "Arms Race": "Stormblind Complex"
}


MISC_NOTABLE_POOLS: dict[MiscSource, set[str]] = {
    MiscSource("All Salvaged Claptraps"): {
        "/Game/GameData/Challenges/CrewChallenges/Salvage/SalvageRewards/ItemPool_Crew_Challenge_Salvage_GirlfriendReward.ItemPool_Crew_Challenge_Salvage_GirlfriendReward",
    },
    MiscSource("All Zero Kill Targets"): {
        "/Game/GameData/Challenges/CrewChallenges/KillTarget/ItemPool_Zer0_BountyDone.ItemPool_Zer0_BountyDone",
    },
    MiscSource("All Hammerlock Hunts"): {
        "/Game/GameData/Challenges/CrewChallenges/Hunt/ItemPool_Hammerlock_HuntDone.ItemPool_Hammerlock_HuntDone",
    },
    MiscSource("Random Chance from Radio Towers"): {
        "/Game/GameData/Challenges/CrewChallenges/Sabotage/ChallengeSabotageRewardStat/ItemPool_Crew_Challenge_Sabotage_GunReward.ItemPool_Crew_Challenge_Sabotage_GunReward",
    },
    MiscSource("Eridian Fabricator", include_world_drops=True): {
        "/Game/GameData/Loot/ItemPools/Fabricator/ItemPool_FabricatorGuns.ItemPool_FabricatorGuns",
        "/Game/GameData/Loot/ItemPools/Fabricator/ItemPool_FabricatorGuns_AltFire.ItemPool_FabricatorGuns_AltFire",
    },
    # TODO: Might do better to read these from vault card objects themselves
    MiscSource("Vault Card 1"): {
        "/Game/PatchDLC/VaultCard/Gear/Shields/Unique/SuperSoldier/Balance/ItemPool_VaultCard1_SuperSoldier.ItemPool_VaultCard1_SuperSoldier",
        "/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/BirdofPrey/Balance/ItemPool_VaultCard1_BirdofPrey.ItemPool_VaultCard1_BirdofPrey",
        "/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/Guardian/Balance/ItemPool_VaultCard1_Guardian.ItemPool_VaultCard1_Guardian",
        "/Game/PatchDLC/VaultCard/Gear/Weapons/Unique/Mechanic/Balance/ItemPool_VaultCard1_Mechanic.ItemPool_VaultCard1_Mechanic",
    },
    MiscSource("Vault Card 2"): {
        "/Game/PatchDLC/VaultCard2/Gear/Artifacts/Unique/Shlooter/Balance/ItemPool_VaultCard2_Shlooter.ItemPool_VaultCard2_Shlooter",
        "/Game/PatchDLC/VaultCard2/Gear/GrenadeMods/Unique/Pyroburst/Balance/ItemPool_VaultCard2_Pyroburst.ItemPool_VaultCard2_Pyroburst",
        "/Game/PatchDLC/VaultCard2/Gear/Weapons/Unique/GoldRush/Balance/ItemPool_VaultCard2_GoldRush.ItemPool_VaultCard2_GoldRush",
        "/Game/PatchDLC/VaultCard2/Gear/Weapons/Unique/Troubleshooter/Balance/ItemPool_VaultCard2_Troubleshooter.ItemPool_VaultCard2_Troubleshooter",
    },
    MiscSource("Vault Card 3"): {
        "/Game/PatchDLC/VaultCard3/Gear/GrenadeMods/Unique/Sidewinder/Balance/ItemPool_VaultCard3_Sidewinder",
        "/Game/PatchDLC/VaultCard3/Gear/Shields/Unique/Manawell/Balance/ItemPool_VaultCard3_Manawell",
        "/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/BladeFury/Balance/Itempool_VaultCard3_BladeFury",
        "/Game/PatchDLC/VaultCard3/Gear/Weapons/Unique/Corruption/Balance/Itempool_VaultCard3_Corruption",
    },
    MiscSource("Tipping Moxxi", "Sanctuary"): {
        "/Game/InteractiveObjects/TipJar/ItemPool_MoxxiTip_GunRewards.ItemPool_MoxxiTip_GunRewards",
    },
    MiscSource("Earl's Vendor", "Sanctuary", True): {
        "/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl.DA_ItemPool_VendingMachine_CrazyEarl",
        "/Game/GameData/Loot/ItemPools/VendingMachines/DA_ItemPool_VendingMachine_CrazyEarl_OfTheDay.DA_ItemPool_VendingMachine_CrazyEarl_OfTheDay",
    },
    MiscSource("Diamond Chest", "Sanctuary", True): {
        "/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/Data/ItemPool_DiamondWall_BigGuns.ItemPool_DiamondWall_BigGuns",
        "/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/Data/ItemPool_DiamondWall_SmallGuns.ItemPool_DiamondWall_SmallGuns",
        "/Game/PatchDLC/DiamondLootChest/InteractiveObjects/DiamondChest/Data/ItemPool_Heavy_All.ItemPool_Heavy_All",
        "/Game/PatchDLC/DiamondLootChest/Loot/ItemPools/ItemPool_GrenadeMods_DiamondKeyWall.ItemPool_GrenadeMods_DiamondKeyWall",
        "/Game/PatchDLC/DiamondLootChest/Loot/ItemPools/ItemPool_Shields_DiamondKeyWall.ItemPool_Shields_DiamondKeyWall",
    },
    MiscSource("Use Suicide Machine 20x", "Ambermire"): {
        "/Game/GameData/Challenges/Missions/Unique/ItemPool_SuckerPunch_BurningSummit.ItemPool_SuckerPunch_BurningSummit",
    },
    MiscSource("Loot Tink Backpacks"): {
        "/Game/Enemies/Tink/Loot/_Design/LootPools/ItemPool_LootTink_CashExplosion.ItemPool_LootTink_CashExplosion",
        "/Game/Enemies/Tink/Loot/_Design/LootPools/ItemPool_LootTink_TinkLootPackOpened_2.ItemPool_LootTink_TinkLootPackOpened_2",
        "/Game/Enemies/Tink/Loot/_Design/LootPools/ItemPool_LootTink_TinkLootPackOpened.ItemPool_LootTink_TinkLootPackOpened",
    },
    MiscSource("Loot Tink Damaged Drops"): {
        "/Game/Enemies/Tink/Loot/_Design/LootPools/ItemPool_LootTink_DamagedGearDrops.ItemPool_LootTink_DamagedGearDrops",
    },
    MiscSource("Break 50 hearts"): {
        "/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_PolyAim.ItemPool_VDay_Weapon_PolyAim",
    },
    MiscSource("Break 100 hearts"): {
        "/Game/PatchDLC/EventVDay/GameData/Challenges/ChallengeRewards/ItemPool_VDay_Weapon_WeddingInvitation.ItemPool_VDay_Weapon_WeddingInvitation",
    },
    MiscSource("All Ember Bombs"): {
        "/Game/PatchDLC/Dandelion/Missions/ItemPool_Reward/ItemPool_Mission_Crew_EmbersPurge.ItemPool_Mission_Crew_EmbersPurge",
    },
    MiscSource("All Torgue Hot Sauce"): {
        "/Game/PatchDLC/Dandelion/Missions/ItemPool_Reward/ItemPool_Mission_Crew_TorguesMarketingMistake.ItemPool_Mission_Crew_TorguesMarketingMistake",
    },
    MiscSource("Petting Mancubite 50+ times", "Lodge"): {
        "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Kaleidoscope.ItemPool_Hibiscus_Kaleidoscope",
    },
}

# Only use this where it's not possible to assign an itempool
MISC_NOTABLE_BALANCES: dict[MiscSource, set[str]] = {
    MiscSource("Booster Pack"): {
        "/Game/Gear/GrenadeMods/_Design/_Unique/CashMoneyPreorder/Balance/InvBalD_GM_CashMoneyPreorder.InvBalD_GM_CashMoneyPreorder",
        "/Game/Gear/Shields/_Design/_Uniques/_XPLootBooster/Balance/InvBalD_Shield_XPLootBooster.InvBalD_Shield_XPLootBooster",
    },
    MiscSource("Butt Stallion Pack"): {
        "/Game/Gear/GrenadeMods/_Design/_Unique/ButtStallion/Balance/InvBalD_GM_ButtStallion.InvBalD_GM_ButtStallion",
    },
    MiscSource("Toy Box Pack"): {
        "/Game/Gear/GrenadeMods/_Design/_Unique/ToyGrenade/Balance/InvBalD_GM_ToyGrenade.InvBalD_GM_ToyGrenade",
        "/Game/Gear/Weapons/Pistols/Maliwan/_Shared/_Design/_Unique/HyperHydrator/Balance/Balance_PS_MAL_HyperHydrator.Balance_PS_MAL_HyperHydrator",
        "/Game/Gear/Weapons/Pistols/Torgue/_Shared/_Design/_Unique/Nurf/Balance/Balance_PS_TOR_Nurf.Balance_PS_TOR_Nurf",
    },
    MiscSource("Tink of Cunning (True Trial)"): {
        "/Game/Gear/Weapons/AssaultRifles/Vladof/_Shared/_Design/_Unique/Sickle/Balance/Balance_AR_VLA_Sickle.Balance_AR_VLA_Sickle",
        "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Skullmasher/Balance/Balance_SR_JAK_Skullmasher.Balance_SR_JAK_Skullmasher",
    },
    MiscSource("Skag of Survival (True Trial)"): {
        "/Game/Gear/Weapons/Shotguns/Torgue/_Shared/_Design/_Unique/TheLob/Balance/Balance_SG_Torgue_ETech_TheLob.Balance_SG_Torgue_ETech_TheLob",
        "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/Lucky7/Balance/Balance_PS_JAK_Lucky7.Balance_PS_JAK_Lucky7",
    },
    MiscSource("Arbalest of Discipline (True Trial)"): {
        "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Flipper/Balance/Balance_SM_MAL_Flipper.Balance_SM_MAL_Flipper",
        "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Kaoson/Balance/Balance_SM_DAHL_Kaoson.Balance_SM_DAHL_Kaoson",
    },
    MiscSource("Sera of Supremacy (True Trial)"): {
        "/Game/PatchDLC/Ixora2/Gear/Weapons/_Unique/Replay/Balance/Balance_PS_ATL_Replay.Balance_PS_ATL_Replay",
        "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Monarch/Balance/Balance_AR_VLA_Monarch.Balance_AR_VLA_Monarch",
    },
    MiscSource("Hag of Fervor (True Trial)"): {
        "/Game/Gear/Weapons/Pistols/Jakobs/_Shared/_Design/_Unique/Maggie/Balance/Balance_PS_JAK_Maggie.Balance_PS_JAK_Maggie",
        "/Game/PatchDLC/Alisma/Gear/Weapon/_Unique/Convergence/Balance/Balance_SG_HYP_Convergence.Balance_SG_HYP_Convergence",
    },
    MiscSource("Tyrant of Instinct (True Trial)"): {
        "/Game/PatchDLC/Ixora/Gear/Weapons/_Unique/Tizzy/Balance/Balance_PS_COV_Tizzy.Balance_PS_COV_Tizzy",
        "/Game/PatchDLC/Mayhem2/Gear/Weapon/_Shared/_Unique/Backburner/Balance/Balance_HW_VLA_ETech_BackBurner.Balance_HW_VLA_ETech_BackBurner",
    },
}
