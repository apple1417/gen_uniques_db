from dataclasses import dataclass, field
from typing import Optional


@dataclass
class EnemyDrops:
    itempools: set[str] = field(default_factory=set)
    itempool_lists: set[str] = field(default_factory=set)


ENEMY_DROP_EXPANSIONS: set[str] = {
    "/Game/PatchDLC/Raid1/GameData/Loot/ItemPoolExpansions/CharacterItemPoolExpansions_Raid1.CharacterItemPoolExpansions_Raid1",
}

# TODO: this probably needs to be automatic
BPCHAR_INHERITANCE_OVERRIDES: dict[str, str] = {
    # X3 Inherits practically everything from X2, there's nothing in it's actual uasset
    "/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX3.BPChar_AnointedX3": "/Game/Enemies/Punk_Female/_Unique/AnointedX2_X3/_Design/Character/BPChar_AnointedX2.BPChar_AnointedX2",
}

IGNORED_BPCHARS: set[str] = set()

BPCHAR_NAME_OVERRIDES: dict[str, str] = {
    "BPChar_Rakk_Dragon": "Dreg / Rage",

}

MAP_OVERRIDES: dict[str, Optional[str]] = {
    "/Game/Enemies/Agonizer_9k/_Shared/Character/BPChar_Agonizer_9k.BPChar_Agonizer_9k": "Guts of Carnivora",
    "/Game/Enemies/Ape/_Unique/JungleMonarch/_Design/Character/BPChar_ApeJungleMonarch.BPChar_ApeJungleMonarch": "Ambermire",
    "/Game/Enemies/Ape/Badass/_Design/Character/BPChar_ApeBadass.BPChar_ApeBadass": "Floodmoor Basin",
    "/Game/Enemies/EdenBoss/_Shared/_Design/Character/BPChar_EdenBoss.BPChar_EdenBoss": "Floating Tomb",
    "/Game/Enemies/Enforcer/_Unique/Terror/_Design/Character/BPChar_Terror.BPChar_Terror": "Guts of Carnivora",
    "/Game/Enemies/Enforcer/Anointed/_Design/Character/BPChar_EnforcerAnointed.BPChar_EnforcerAnointed": "Floodmoor Basin",
    "/Game/Enemies/Goon/_Unique/MonsterTrucker/_Design/Character/BPChar_GoonMonsterTrucker.BPChar_GoonMonsterTrucker": "Guts of Carnivora",
    "/Game/Enemies/Goon/_Unique/RoidRage/_Design/Character/BPChar_GoonBounty01.BPChar_GoonBounty01": "Cathedral of the Twin Gods",
    "/Game/Enemies/Goon/Anointed/_Design/Character/BPChar_GoonAnointed.BPChar_GoonAnointed": "Cathedral of the Twin Gods",
    # This one legitamately gets two maps cause the same BPChar is used for different enemies, arbitrarily putting it in Pyre
    "/Game/Enemies/Nekrobug/_Unique/HopperSwarm/_Design/Character/BPChar_Nekrobug_HopperSwarm.BPChar_Nekrobug_HopperSwarm": "Pyre of Stars",
    "/Game/Enemies/PrometheaBoss/Rampager/_Design/Character/BPChar_Rampager.BPChar_Rampager": "Forgotten Basilica",
    "/Game/Enemies/Psycho_Male/_Unique/Rakkman/_Design/Character/BPChar_Rakkman.BPChar_Rakkman": "Carnivora",
    "/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass": "Droughts",
    "/Game/Enemies/Tink/_Unique/Pain/_Design/Character/BPChar_Pain.BPChar_Pain": "Guts of Carnivora",
    "/Game/Enemies/Tink/_Unique/Rare02/_Design/Character/BPChar_TinkRare02.BPChar_TinkRare02": "Konrad's Hold",
    "/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaA.BPChar_VarkidHunt02_LarvaA": "Droughts",
    "/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaB.BPChar_VarkidHunt02_LarvaB": "Droughts",
    "/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaC.BPChar_VarkidHunt02_LarvaC": "Droughts",
    "/Game/Enemies/Varkid/_Unique/Hunt02/_Design/Larva/BPChar_VarkidHunt02_LarvaD.BPChar_VarkidHunt02_LarvaD": "Droughts",
    "/Game/NonPlayerCharacters/Aurelia/_TheBoss/_Design/Character/BPChar_AureliaBoss.BPChar_AureliaBoss": "Blackbarrel Cellars",
    "/Game/NonPlayerCharacters/Troy/_TheBoss/_Design/Character/BPChar_TroyBoss.BPChar_TroyBoss": "Great Vault",
    "/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/SpiderBrain/Character/BPChar_SpiderBrain.BPChar_SpiderBrain": "Midnight's Cairn",
    "/Game/PatchDLC/Raid1/Enemies/Behemoth/_Unique/RaidMiniBoss/UpperHalf/Character/BPChar_UpperHalf.BPChar_UpperHalf": "Midnight's Cairn",
    "/Geranium/Enemies/Biobeast/_Unique/AlteredBeast/_Design/Character/BPChar_Biobeast_AlteredBeast.BPChar_Biobeast_AlteredBeast": "Obsidian Forest",
    "/Geranium/Enemies/Biobeast/_Unique/CopyBeast/_Design/Character/BPChar_Biobeast_CopyBeast.BPChar_Biobeast_CopyBeast": "Obsidian Forest",
    "/Geranium/Enemies/Biobeast/_Unique/PlasmaBeast/_Design/Character/BPChar_Biobeast_PlasmaBeast.BPChar_Biobeast_PlasmaBeast": "Obsidian Forest",
    "/Geranium/Enemies/GerEnforcer/_Unique/Dispatcher/_Design/Character/BPChar_GerEnforcerDispatcher.BPChar_GerEnforcerDispatcher": "Blastplains",
    "/Geranium/Enemies/GerSaurian/_Unique/Devourer/_Design/Character/BPChar_GerSaurianDevourer_Pygmimus.BPChar_GerSaurianDevourer_Pygmimus": "Blastplains",
    "/Geranium/Enemies/GerSaurian/_Unique/Horsemen4/_Design/Character/BPChar_GerSaurianHorsemen4.BPChar_GerSaurianHorsemen4": "Blastplains",
    "/Geranium/Enemies/Quartermaster/Tink/_Design/Character/BPChar_Quartermaster_Tink.BPChar_Quartermaster_Tink": "Bloodsun Canyon",
    "/Ixora2/Enemies/CotV/Punk/BanditChief/_Design/Character/BPChar_Punk_BanditChief.BPChar_Punk_BanditChief": "Karass Canyon",
    "/Ixora2/Enemies/Guardian/Redeemer/_Design/Character/BPChar_GuardianBrute_Redeemer.BPChar_GuardianBrute_Redeemer": "Scryer's Crypt",
    "/Ixora2/Enemies/Varkid/_Unique/RaidBoss/_Design/Character/BPChar_Varkid_RaidBoss.BPChar_Varkid_RaidBoss": "Darkthirst Dominion",
    # Removing Maps
    "/Game/Enemies/Ape/Loot/_Design/Character/BPChar_ApeLoot.BPChar_ApeLoot": None,
    "/Game/Enemies/Psycho_Male/Loot/_Design/Character/BPChar_PsychoLoot.BPChar_PsychoLoot": None,
    "/Game/Enemies/Rakk/Queen/_Design/Character/BPChar_RakkQueen.BPChar_RakkQueen": None,
    "/Game/Enemies/Saurian/Shiny/_Design/Character/BPChar_SaurianShiny.BPChar_SaurianShiny": None,
    "/Game/Enemies/ServiceBot/LOOT/_Design/Character/BPChar_ServiceBot_LOOT.BPChar_ServiceBot_LOOT": None,
    "/Game/Enemies/Skag/Chubby/_Design/Character/BPChar_SkagChubby.BPChar_SkagChubby": None,
    "/Game/Enemies/Tink/Loot/_Design/Character/BPChar_TinkLoot.BPChar_TinkLoot": None,
}

DROP_OVERRIDES: dict[str, EnemyDrops] = {
    # TODO: probably need to do these automatically
    # Extras added via spawnoptions
    "/Game/Enemies/Ape/Badass/_Design/Character/BPChar_ApeBadass.BPChar_ApeBadass": EnemyDrops({
        "/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Artemis.ItemPool_Artemis",
    }, {
        "/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear",
    }),
    "/Game/Enemies/Goliath/Anointed/_Design/Character/BPChar_MansionBoss.BPChar_MansionBoss": EnemyDrops({
        "/Game/GameData/Loot/ItemPools/Unique/ItemPool_LeadSprinkler_AnointedIntro",
    }),
    "/Game/Enemies/Psycho_Male/Badasss/_Design/Character/BPChar_PsychoBadass.BPChar_PsychoBadass": EnemyDrops({
        "/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Mincemeat.ItemPool_Mincemeat",
    }, {
        "/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear",
    }),
    "/Game/Enemies/Enforcer/Anointed/_Design/Character/BPChar_EnforcerAnointed.BPChar_EnforcerAnointed": EnemyDrops({
        "/Game/PatchDLC/Raid1/GameData/Loot/ItemPools/ItemPool_Muldock.ItemPool_Muldock",
    }, {
        "/Game/GameData/Loot/ItemPools/ItemPoolList_AnointedEnemyGunsGear.ItemPoolList_AnointedEnemyGunsGear",
    }),
    "/Game/Enemies/Nog/_Unique/Beans/_Design/Character/BPChar_NogBeans.BPChar_NogBeans": EnemyDrops({
        "/Game/GameData/Loot/ItemPools/Unique/ItemPool_Westergun_TheBoo",
        "/Game/Missions/Side/Zone_1/Athenas/InvasionOfPrivacy/ItemPool_InvasionOfPrivacy_BeansRunnable",
    }),
    "/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/Character/BPChar_EnforcerSacrificeBoss.BPChar_EnforcerSacrificeBoss": EnemyDrops({
        "/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Gun.ItemPool_EnforcerSacrificeBoss_Gun",
        "/Game/Enemies/Enforcer/_Unique/SacrificeBoss/_Design/ItemPool/ItemPool_EnforcerSacrificeBoss_Shotgun.ItemPool_EnforcerSacrificeBoss_Shotgun",
    }, {
        "/Game/GameData/Loot/ItemPools/ItemPoolList_MiniBoss.ItemPoolList_MiniBoss",
    }),
    # Add the hellfire
    "/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/BPChar_Ape_Hunt01.BPChar_Ape_Hunt01": EnemyDrops({
        "/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/ItemPool_Ape01_Hunt.ItemPool_Ape01_Hunt",
        "/Game/Enemies/Ape/_Unique/Hunt01/_Design/Character/ItemPool_Ape_Hunt01_FireDeath.ItemPool_Ape_Hunt01_FireDeath",
    }, {
        "/Game/GameData/Loot/ItemPools/ItemPoolList_BadassEnemyGunsGear.ItemPoolList_BadassEnemyGunsGear",
    }),
    # Agonizer's just a mess
    # Referenced via /Game/Enemies/Agonizer_9k/_Shared/Actions/Emergent/A_A9K_Death
    # https://gist.github.com/apocalyptech/ed93fcaf2926ffa5ac728f81c65ec4ad
    "/Game/Enemies/Agonizer_9k/_Shared/Character/BPChar_Agonizer_9k.BPChar_Agonizer_9k": EnemyDrops(itempool_lists={
        "/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Pain.ItemPoolList_Boss_Pain",
        "/Game/GameData/Loot/ItemPools/ItemPoolList_Boss_Terror.ItemPoolList_Boss_Terror",
    }),
    # TODO: can probably just remove this
    # This comes from BPChar_Hib_EistaChild_Radiation but it feels more appropriate to list the base
    "/Hibiscus/NonPlayerCharacters/Eista/_Design/Character/BPChar_Hib_Eista.BPChar_Hib_Eista": EnemyDrops(itempool_lists={
        "/Game/PatchDLC/Hibiscus/GameData/Loot/EnemyPools/ItemPoolList_Eista.ItemPoolList_Eista",
    })
}
