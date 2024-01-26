class Biome:
    def __init__(self, common_fish_small: list[str], common_fish_large: list[str],
                 uncommon_fish_small: list[str], uncommon_fish_large: list[str],
                 rare_fish_small: list[str], rare_fish_large: list[str]):
        self.common_fish_small = {fish: 100 / len(common_fish_small) for fish in common_fish_small}
        self.common_fish_large = {fish: 100 / len(common_fish_large) for fish in common_fish_large}
        self.uncommon_fish_small = {fish: 100 / len(uncommon_fish_small) for fish in uncommon_fish_small}
        self.uncommon_fish_large = {fish: 100 / len(uncommon_fish_large) for fish in uncommon_fish_large}
        self.rare_fish_small = {fish: 100 / len(rare_fish_small) for fish in rare_fish_small}
        self.rare_fish_large = {fish: 100 / len(rare_fish_large) for fish in rare_fish_large}


BIOME_FREEZING = Biome(
    common_fish_small=["Abecean Longfin", "Angler Larvae"],
    common_fish_large=["Arctic Grayling"],
    uncommon_fish_small=["Juvenile Mudcrab"],
    uncommon_fish_large=["Arctic Char", "Cod"],
    rare_fish_small=["Rare Junk"],
    rare_fish_large=["Angler"]
)
BIOME_UNDERGROUND = Biome(
    common_fish_small=["Silverside Perch"],
    common_fish_large=["Direfish", "Glass Catfish"],
    uncommon_fish_small=["Histcarp"],
    uncommon_fish_large=["Tripod Spiderfish", "Vampire Fish"],
    rare_fish_small=["Rare Junk"],
    rare_fish_large=["Scorpion Fish"]
)
BIOME_LAKE_CLEAR = Biome(
    common_fish_small=["Abecean Longfin", "Glassfish", "Silverside Perch"],
    common_fish_large=["Salmon", "Slaughterfish"],
    uncommon_fish_small=["Cyrodilic Spadetail", "Goldfish", "Juvenile Mudcrab", "Silverside Perch"],
    uncommon_fish_large=["Brook Bass", "Carp"],
    rare_fish_small=["Angelfish"],
    rare_fish_large=["Rare Junk"]
)
BIOME_LAKE_RAIN = Biome(
    common_fish_small=["Cyrodilic Spadetail"],
    common_fish_large=["Catfish"],
    uncommon_fish_small=["Abecean Longfin", "Glassfish", "Pearlfish", "Pygmy Sunfish"],
    uncommon_fish_large=["Salmon", "Slaughterfish"],
    rare_fish_small=["Angelfish"],
    rare_fish_large=["Rare Junk"]
)
BIOME_STREAM_CLEAR = Biome(
    common_fish_small=["River Betty"],
    common_fish_large=["Brook Bass", "Pogfish", "Salmon"],
    uncommon_fish_small=["Histcarp", "Juvenile Mudcrab", "Spadefish"],
    uncommon_fish_large=["Carp"],
    rare_fish_small=["Lyretail Anthias"],
    rare_fish_large=["Rare Junk"]
)
BIOME_STREAM_RAIN = Biome(
    common_fish_small=["River Betty", "Spadefish"],
    common_fish_large=["Pogfish", "Salmon"],
    uncommon_fish_small=["Histcarp", "Juvenile Mudcrab", "Pearlfish"],
    uncommon_fish_large=["Brook Bass", "Slaughterfish"],
    rare_fish_small=["Lyretail Anthias"],
    rare_fish_large=["Rare Junk"]
)
Biomes = [BIOME_FREEZING, BIOME_UNDERGROUND, BIOME_LAKE_CLEAR, BIOME_LAKE_RAIN, BIOME_STREAM_CLEAR, BIOME_STREAM_RAIN]