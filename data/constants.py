GEAR_CATEGORIES: tuple[tuple[str, str], ...] = (
    ("Artifact", "/Game/Gear/_Shared/_Design/GearBuilder/Category_Artifacts.Category_Artifacts"),
    ("COM", "/Game/Gear/_Shared/_Design/GearBuilder/Category_ClassMods.Category_ClassMods"),
    ("Grenade", "/Game/Gear/_Shared/_Design/GearBuilder/Category_GrenadeMods.Category_GrenadeMods"),
    ("Launcher", "/Game/Gear/_Shared/_Design/GearBuilder/Category_HeavyWeapons.Category_HeavyWeapons"),
    ("Pistol", "/Game/Gear/_Shared/_Design/GearBuilder/Category_Pistols.Category_Pistols"),
    ("Rifle", "/Game/Gear/_Shared/_Design/GearBuilder/Category_AssaultRifles.Category_AssaultRifles"),
    ("Shield", "/Game/Gear/_Shared/_Design/GearBuilder/Category_Shields.Category_Shields"),
    ("Shotgun", "/Game/Gear/_Shared/_Design/GearBuilder/Category_Shotguns.Category_Shotguns"),
    ("SMG", "/Game/Gear/_Shared/_Design/GearBuilder/Category_SMGs.Category_SMGs"),
    ("Sniper", "/Game/Gear/_Shared/_Design/GearBuilder/Category_SniperRifles.Category_SniperRifles"),
)

MANUFACTURERS: tuple[tuple[str, str], ...] = (
    ("Anshin", "/Game/Gear/Manufacturers/_Design/Anshin.Anshin"),
    ("Atlas", "/Game/Gear/Manufacturers/_Design/Atlas.Atlas"),
    ("CoV", "/Game/Gear/Manufacturers/_Design/CoV.CoV"),
    ("COM", "/Game/Gear/Manufacturers/_Design/ClassMod.ClassMod"),
    ("Dahl", "/Game/Gear/Manufacturers/_Design/Dahl.Dahl"),
    ("Eridian", "/Game/Gear/Manufacturers/_Design/Eridian.Eridian"),
    ("Hyperion", "/Game/Gear/Manufacturers/_Design/Hyperion.Hyperion"),
    ("Jakobs", "/Game/Gear/Manufacturers/_Design/Jakobs.Jakobs"),
    ("Maliwan", "/Game/Gear/Manufacturers/_Design/Maliwan.Maliwan"),
    ("Pangolin", "/Game/Gear/Manufacturers/_Design/Pangolin.Pangolin"),
    ("Tediore", "/Game/Gear/Manufacturers/_Design/Tediore.Tediore"),
    ("Torgue", "/Game/Gear/Manufacturers/_Design/Torgue.Torgue"),
    ("Vladof", "/Game/Gear/Manufacturers/_Design/Vladof.Vladof"),
)

SOURCE_TYPES: tuple[str, ...] = (
    "Enemy",
    "Mission",
    "Vendor",
    "World Drop",
    "Misc",
)

# Coverted from map_to_eng from bl3-cli-saveedit
MAPS: tuple[tuple[str, str], ...] = (
    ("Ambermire", "MarshFields_P"),
    ("Anvil", "Prison_P"),
    ("Ascension Bluff", "Sacrifice_P"),
    ("Ashfall Peaks", "Lodge_P"),
    ("Athenas", "Monastery_P"),
    ("Atlas HQ", "AtlasHQ_P"),
    ("Benediction of Pain", "Experiment_P"),
    ("Blackbarrel Cellars", "WetlandsVault_P"),
    ("Bloodsun Canyon", "Facility_P"),
    ("Cankerwood", "Woods_P"),
    ("Carnivora", "MotorcadeFestival_P"),
    ("Castle Crimson", "Anger_P"),
    ("Cathedral of the Twin Gods", "Desertvault_P"),
    ("Cistern of Slaughter", "CreatureSlaughter_P"),
    ("Compactor", "Trashtown_P"),
    ("Covenant Pass", "Recruitment_P"),
    ("Crater's Edge", "CraterBoss_P"),
    ("Cursehaven", "Village_P"),
    ("Darkthirst Dominion", "SacrificeBoss_p"),
    ("Desolation's Edge", "Desolate_P"),
    ("Destroyer's Rift", "FinalBoss_P"),
    ("Devil's Razor", "Desert_P"),
    ("Droughts", "Prologue_P"),
    ("Dustbound Archives", "Archive_P"),
    ("Enoch's Grove", "Cabin_P"),
    ("Eschaton Row", "Noir_P"),
    ("Floating Tomb", "WetlandsBoss_P"),
    ("Floodmoor Basin", "Wetlands_P"),
    ("Forgotten Basilica", "CityBoss_P"),
    ("Ghostlight Beacon (Cunning)", "ProvingGrounds_Trial5_P"),
    ("Gradient of Dawn (Survival)", "ProvingGrounds_Trial1_P"),
    ("Grand Opening", "CasinoIntro_P"),
    ("Great Vault", "DesertBoss_P"),
    ("Guts of Carnivora", "MotorcadeInterior_P"),
    ("Hall Obsidian (Supremacy)", "ProvingGrounds_Trial6_P"),
    ("Heart's Desire", "Venue_P"),
    ("Heck Hole", "BloodyHarvest_P"),
    ("Impound Deluxe", "Impound_P"),
    ("Jack's Secret", "Core_P"),
    ("Jakobs Estate", "Mansion_P"),
    ("Karass Canyon", "PandoraMystery_p"),
    ("Konrad's Hold", "Mine_P"),
    ("Lectra City", "Towers_P"),
    ("Lodge", "Bar_P"),
    ("Meridian Metroplex", "City_P"),
    ("Meridian Outskirts", "Outskirts_P"),
    ("Midnight's Cairn", "Raid_P"),
    ("Minos Prime", "GuardianTakedown_P"),
    ("Negul Neshai", "Camp_P"),
    ("Neon Arterial", "CityVault_P"),
    ("Obsidian Forest", "Forest_P"),
    ("Precipice Anchor (Discipline)", "ProvingGrounds_Trial7_P"),
    ("Pyre of Stars", "Crypt_P"),
    ("Sanctuary", "Sanctuary3_P"),
    ("Sandblast Scar", "Convoy_P"),
    ("Sapphire's Run", "Chase_P"),
    ("Scryer's Crypt", "NekroMystery_p"),
    ("Skittermaw Basin", "Lake_P"),
    ("Skydrowned Pulpit (Fervor)", "ProvingGrounds_Trial4_P"),
    ("Skywell-27", "OrbitalPlatform_P"),
    ("Slaughter Shaft", "COVSlaughter_P"),
    ("Slaughterstar 3000", "TechSlaughter_P"),
    ("Spendopticon", "Strip_P"),
    ("Splinterlands", "Motorcade_P"),
    ("Stormblind Complex", "FrostSite_P"),
    ("Tazendeer Ruins", "Beach_P"),
    ("Blastplains", "Frontier_P"),
    ("Psychoscape", "Sanctum_P"),
    ("Vaulthalla", "Eldorado_P"),
    ("Vestige", "Town_P"),
    ("Villa Ultraviolet", "Cartels_P"),
    ("VIP Tower", "TowerLair_P"),
    ("Voracious Canopy", "Watership_P"),
    ("Wayward Tether (Instinct)", "ProvingGrounds_Trial8_P"),
)

RARITIES: tuple[tuple[str, str], ...] = (
    ("White", "/Game/GameData/Loot/RarityData/RarityData_01_Common.RarityData_01_Common"),
    # Watch out for this capitalization
    ("Green", "/Game/GameData/Loot/RarityData/RarityData_02_UnCommon.RarityData_02_Uncommon"),
    ("Blue", "/Game/GameData/Loot/RarityData/RarityData_03_Rare.RarityData_03_Rare"),
    ("Purple", "/Game/GameData/Loot/RarityData/RarityData_04_VeryRare.RarityData_04_VeryRare"),
    ("Legendary", "/Game/GameData/Loot/RarityData/RarityData_05_Legendary.RarityData_05_Legendary"),
)

ITEM_GROUPS: tuple[str, ...] = (
    "Base Game",
    "Booster Pack",
    "Butt Stallion Pack",
    "Toy Box Pack",
    "Steam Release",
    "Maliwan Takedown",
    "Guardian Takedown",
    "Bloody Harvest",
    "Broken Hearts",
    "Cartels",
    "Vault Card",
    "Vault Card 2",
    "Jackpot",
    "Wedding",
    "Bounty",
    "Krieg",
    "Arms Race",
    "Director's Cut",
)

PLAYER_CLASSES: tuple[tuple[str, str], ...] = (
    ("Amara", "/Game/PlayerCharacters/SirenBrawler/PlayerClassId_Siren.PlayerClassId_Siren"),
    ("Fl4k", "/Game/PlayerCharacters/Beastmaster/PlayerClassId_Beastmaster.PlayerClassId_Beastmaster"),
    ("Moze", "/Game/PlayerCharacters/Gunner/PlayerClassId_Gunner.PlayerClassId_Gunner"),
    ("Zane", "/Game/PlayerCharacters/Operative/PlayerClassId_Operative.PlayerClassId_Operative"),
)
