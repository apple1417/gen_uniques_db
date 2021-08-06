from dataclasses import dataclass, field


@dataclass
class BalancedItemsEntry:
    balances: set[str] = field(default_factory=set)
    pools: set[str] = field(default_factory=set)


HOTFIX_JUDGE_HIGHTOWER_PT_OVERRIDE: str = "/Game/NonPlayerCharacters/_Promethea/AtlasSoldier/_Design/Character/BPChar_AtlasSoldier_Bounty01.BPChar_AtlasSoldier_Bounty01"

HOTFIX_DOD_POOLS_REMOVE_ALL: dict[str, tuple[bool, bool]] = {
    "/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/b/BPChar_Punk_Bounty01b.BPChar_Punk_Bounty01b": (True, False),
    "/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/c/BPChar_Punk_Bounty01c.BPChar_Punk_Bounty01c": (True, False),
    "/Game/Enemies/Punk_Female/_Unique/Bounty01/_Design/Character/d/BPChar_Punk_Bounty01d.BPChar_Punk_Bounty01d": (True, False),
    "/Game/Enemies/Spiderant/_Unique/Hunt01/_Design/Character/BPChar_Spiderant_Hunt01.BPChar_Spiderant_Hunt01": (True, False),
}

HOTFIX_BALANCEDITEMS_REMOVE: dict[str, BalancedItemsEntry] = {
    "/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidBoss_Pool.ItemPool_RaidBoss_Pool": BalancedItemsEntry({
        "/Game/PatchDLC/Raid1/Gear/Shields/VersionOmNom/Balance/InvBalD_Shield_Legendary_VersionOmNom.InvBalD_Shield_Legendary_VersionOmNom",
        "/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_Recharger/InvBalD_Shield_SlideKickRecharger.InvBalD_Shield_SlideKickRecharger",
        "/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/SlideKick_FrozenHeart/Balance/InvBalD_Shield_SlideKickFrozenHeart.InvBalD_Shield_SlideKickFrozenHeart",
        "/Game/PatchDLC/Raid1/Gear/Shields/_HybridLegendary/SlideKickHybrid/ReCharger_Berner/InvBalD_Shield_LGD_ReCharger_Berner.InvBalD_Shield_LGD_ReCharger_Berner",
    }, {
        "/Game/PatchDLC/Raid1/Customizations/ItemPool_Raid1_Customization.ItemPool_Raid1_Customization",
    }),
    "/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Miniboss.ItemPool_TD2_Miniboss": BalancedItemsEntry(pools={
        "/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries"
    }),
    "/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Boss.ItemPool_TD2_Boss": BalancedItemsEntry(pools={
        "/Game/PatchDLC/Raid1/Re-Engagement/ItemPool/ItemPool_Mayhem4_Legendaries.ItemPool_Mayhem4_Legendaries",
    }),
    "/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss.ItemPool_AureliaBoss": BalancedItemsEntry({
        "/Game/PatchDLC/Raid1/Re-Engagement/Weapons/Juliet/Balance/Balance_AR_TOR_Juliet_WorldDrop.Balance_AR_TOR_Juliet_WorldDrop",
    }),
    "/Game/PatchDLC/DiamondLootChest/Loot/ItemPools/ItemPool_SMGs_Mayhem.ItemPool_SMGs_Mayhem": BalancedItemsEntry({
        "/Game/PatchDLC/Raid1/Gear/Weapons/Link/Balance/Balance_SM_MAL_Link.Balance_SM_MAL_Link",
    }),
    "/Game/PatchDLC/DiamondLootChest/Loot/ItemPools/ItemPool_Shields_AllAndDLC.ItemPool_Shields_AllAndDLC": BalancedItemsEntry(pools={
        "/Game/PatchDLC/Raid1/GameData/Loot/ItemPool_RaidMiniBosses_Pool.ItemPool_RaidMiniBosses_Pool",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Soulrender.ItemPool_Hibiscus_Soulrender": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Soulrender/Balance/Balance_DAL_AR_Soulrender.Balance_DAL_AR_Soulrender",
    }),
}

HOTFIX_BALANCEDITEMS_ADD: dict[str, BalancedItemsEntry] = {
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_Hampton.ItemPool_Hibiscus_Hunt_Hampton": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Anarchy/Balance/Balance_SG_TED_Anarchy.Balance_SG_TED_Anarchy",
    }),
    "/Game/GameData/Loot/ItemPools/Unique/ItemPool_Piss_ThunkandSloth.ItemPool_Piss_ThunkandSloth": BalancedItemsEntry({
        "/Game/Gear/Weapons/HeavyWeapons/Vladof/_Shared/_Design/_Unique/Mongol/Balance/Balance_HW_VLA_Mongol.Balance_HW_VLA_Mongol",
    }),
    "/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Miniboss.ItemPool_TD2_Miniboss": BalancedItemsEntry(pools={
        "/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPool_Mayhem2_Legendaries.ItemPool_Mayhem2_Legendaries",
    }),
    "/Game/PatchDLC/Takedown2/GameData/Loot/ItemPool_TD2_Boss.ItemPool_TD2_Boss": BalancedItemsEntry(pools={
        "/Game/PatchDLC/Mayhem2/Gear/ItemPoolExpansion_Mayhem2/ItemPool_Mayhem2_Legendaries.ItemPool_Mayhem2_Legendaries",
    }),
    "/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_AureliaBoss.ItemPool_AureliaBoss": BalancedItemsEntry({
        "/Game/Gear/GrenadeMods/_Design/_Unique/FireStorm/Balance/InvBalD_GM_VLA_FireStorm.InvBalD_GM_VLA_FireStorm",
    }),
    "/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Loot_Enemies.ItemPool_Loot_Enemies": BalancedItemsEntry({
        "/Game/Gear/Weapons/HeavyWeapons/Torgue/_Shared/_Design/_Unique/RYNO/Balance/Balance_HW_TOR_RYNO.Balance_HW_TOR_RYNO",
    }),
    "/Game/PatchDLC/DiamondLootChest/Loot/ItemPools/ItemPool_Shields_AllAndDLC.ItemPool_Shields_AllAndDLC": BalancedItemsEntry(pools={
        "/Game/PatchDLC/DiamondLootChest/Loot/ItemPools/ItemPool_Shields_MaliwanTD.ItemPool_Shields_MaliwanTD",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_SparkyBoom.ItemPool_Hibiscus_SparkyBoom": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Omen/Balance/Balance_SG_TED_Omen.Balance_SG_TED_Omen",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_VoidRift.ItemPool_Hibiscus_VoidRift": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Oldridian/Balance/Balance_SM_HYP_Oldridian.Balance_SM_HYP_Oldridian",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_UnseenThreat.ItemPool_Hibiscus_UnseenThreat": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Homicidal/Balance/Balance_AR_COV_Homicidal.Balance_AR_COV_Homicidal",
    }),
    # Technically this has the wrong capitalization at the end - should be `Gmork` - but the
    #  itempool reference goes through `fix_dotted_object_name()` which copies the first one
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hunt_GMork.ItemPool_Hibiscus_Hunt_GMork": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/Torch/Balance/InvBalD_Shield_Legendary_Torch.InvBalD_Shield_Legendary_Torch",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_LoveDrill.ItemPool_Hibiscus_LoveDrill": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Shields/_Unique/OldGod/Balance/InvBalD_Shield_OldGod.InvBalD_Shield_OldGod",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Mutant.ItemPool_Hibiscus_Mutant": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/SRN/InvBalD_CM_Siren_Hib.InvBalD_CM_Siren_Hib",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Shocker.ItemPool_Hibiscus_Shocker": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/OPE/InvBalD_CM_Operative_Hib.InvBalD_CM_Operative_Hib",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Hydrafrost.ItemPool_Hibiscus_Hydrafrost": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/BSM/InvBalD_CM_Beastmaster_Hib.InvBalD_CM_Beastmaster_Hib",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Soulrender.ItemPool_Hibiscus_Soulrender": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/Weapon/_Unique/Insider/Balance/Balance_SG_MAL_ETech_Insider.Balance_SG_MAL_ETech_Insider",
    }),
    "/Game/PatchDLC/Hibiscus/GameData/Loot/UniqueEnemyDrops/ItemPool_Hibiscus_Lunacy.ItemPool_Hibiscus_Lunacy": BalancedItemsEntry({
        "/Game/PatchDLC/Hibiscus/Gear/ClassMods/_Design/GUN/InvBalD_CM_Gunner_Hib.InvBalD_CM_Gunner_Hib",
    }),
}

HOTFIX_ITEMPOOLLISTS_ADD: dict[str, set[str]] = {
    "/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Terror.ItemPoolList_Boss_Terror": {
        "/Game/GameData/Loot/ItemPools/Unique/ItemPool_Agonizer1500_Terror.ItemPool_Agonizer1500_Terror"
    },
    "/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_Eista.ItemPoolList_Eista": {
        "/Game/PatchDLC/Hibiscus/GameData/Loot/Legendary/ItemPool_Hib_SnipeRifles_Legendary.ItemPool_Hib_SnipeRifles_Legendary",
    }
}
