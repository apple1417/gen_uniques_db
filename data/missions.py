MISSION_NAME_OVERRIDES: dict[str, str] = {
    "/Game/Missions/Plot/Mission_Ep01_ChildrenOfTheVault.Default__Mission_Ep01_ChildrenOfTheVault_C": "Children of the Vault",
    "/Game/Missions/Plot/Mission_Ep02_Sacrifice.Default__Mission_Ep02_Sacrifice_C": "From The Ground Up",
    "/Game/Missions/Plot/Mission_Ep03_GetVaultMap.Default__Mission_Ep03_GetVaultMap_C": "Cult Following",
    "/Game/Missions/Plot/Mission_Ep04_EarnSpaceship.Default__Mission_Ep04_EarnSpaceship_C": "Taking Flight",
    "/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep01_MeetTimothy.Default__Mission_DLC1_Ep01_MeetTimothy_C": "The Handsome Jackpot",
    "/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep02_MeetCrad.Default__Mission_DLC1_Ep02_MeetCrad_C": "Playing with Fire",
    "/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep03_Impound.Default__Mission_DLC1_Ep03_Impound_C": "Winners and Losers",
    "/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep04_Trashtown.Default__Mission_DLC1_Ep04_Trashtown_C": "One Man’s Treasure",
    "/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep05_ThePlan.Default__Mission_DLC1_Ep05_ThePlan_C": "The Plan",
    "/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep07_TheHeist.Default__Mission_DLC1_Ep07_TheHeist_C": "All Bets Off",
}

MISSION_PATH_GLOBS: set[str] = {
    "/Game/Missions/Plot/Mission_*",
    "/Game/Missions/Side/**/Mission_*",
    "/Game/PatchDLC/Alisma/Missions/Plot/ALI_*",
    "/Game/PatchDLC/Alisma/Missions/Side/ALI_SM_*",
    "/Game/PatchDLC/BloodyHarvest/Missions/Side/Seasonal/Mission_*",
    "/Game/PatchDLC/CitizenScience/Missions/Mission_*",
    "/Game/PatchDLC/Dandelion/Missions/*/Mission_DLC1_*",
    "/Game/PatchDLC/Event2/Missions/Side/*/Mission_*",
    "/Game/PatchDLC/Geranium/Missions/*/Mission_*",
    "/Game/PatchDLC/Hibiscus/Missions/Plot/EP*",
    "/Game/PatchDLC/Hibiscus/Missions/Side/SideMission_DLC2_*",
    "/Game/PatchDLC/Ixora/Missions/Side/Mission_*",
    "/Game/PatchDLC/Ixora2/Missions/Side/Mission_*",
    "/Game/PatchDLC/Raid1/Missions/Mission_*",
    "/Game/PatchDLC/Takedown2/Missions/Side/Mission_*",
}


EXTRA_MISSION_REWARDS: dict[str, set[str]] = {
    "/Game/Missions/Plot/Mission_Ep05_OvercomeHQBlockade.Default__Mission_Ep05_OvercomeHQBlockade_C": {
        "/Game/Gear/Weapons/_Shared/NPC_Weapons/Zero/ZeroForPlayer/Balance_SR_HYP_ZeroForPlayer.Balance_SR_HYP_ZeroForPlayer",
    },
    "/Game/Missions/Side/Zone_1/Athenas/Mission_InvasionOfPrivacy.Default__Mission_InvasionOfPrivacy_C": {
        "/Game/Gear/Weapons/SMGs/Tediore/_Shared/_Design/_Unique/Beans/Balance/Balance_SM_TED_Beans.Balance_SM_TED_Beans",
    },
    "/Game/Missions/Side/Zone_3/Desert/Mission_BirthdaySurprise.Default__Mission_BirthdaySurprise_C": {
        "/Game/Gear/GrenadeMods/_Design/_Unique/BirthdaySuprise/Balance/InvBalD_GM_BirthdaySuprise.InvBalD_GM_BirthdaySuprise",
    },
    "/Game/PatchDLC/Dandelion/Missions/Plot/Mission_DLC1_Ep01_MeetTimothy.Default__Mission_DLC1_Ep01_MeetTimothy_C": {
        "/Game/PatchDLC/Dandelion/Gear/Weapon/_Unique/JustCaustic/Balance/Balance_SM_HYP_JustCaustic.Balance_SM_HYP_JustCaustic",
    },
    "/Game/PatchDLC/Hibiscus/Missions/Plot/EP06_DLC2.Default__EP06_DLC2_C": {
        "/Game/PatchDLC/Hibiscus/Gear/Artifacts/_Design/_Unique/PUK/Balance/InvBalD_Artifact_PUK.InvBalD_Artifact_PUK",
    },
    "/Game/PatchDLC/Geranium/Missions/Side/Mission_MoneyBackGuarantee.Default__Mission_MoneyBackGuarantee_C": {
        "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Fakobs/Balance/Balance_SG_JAK_Fakobs.Balance_SG_JAK_Fakobs",
    },
    "/Game/PatchDLC/Geranium/Missions/Plot/Mission_Ep05_Crater.Default__Mission_Ep05_Crater_C": {
        "/Game/PatchDLC/Geranium/Gear/Weapon/_Unique/Dakota/Balance/Balance_SG_JAK_Dakota.Balance_SG_JAK_Dakota",
    },
}
