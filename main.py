from fishing_rod import Rod, Rods
from biome import Biome, Biomes
from typing import Union


def fish(peak_hours: bool, high_population: bool, rod: Rod, biome: Biome) -> dict[str, Union[float, int]]:
    small_rate = rod.small_fish_rate
    large_rate = rod.large_fish_rate
    common_table = merge_tables(biome.common_fish_small, small_rate, biome.common_fish_large, large_rate)
    uncommon_table = merge_tables(biome.uncommon_fish_small, small_rate, biome.uncommon_fish_large, large_rate)
    rare_table = merge_tables(biome.rare_fish_small, small_rate, biome.rare_fish_large, large_rate)
    for fish_name, chance in rare_table.copy().items():
        if fish_name not in rod.allowed_rares:
            rare_table.pop(fish_name)
            rare_table["Nothing"] = chance
    common_chance = rod.fish_rarity_peak[0] if peak_hours else rod.fish_rarity_default[0]
    uncommon_chance = rod.fish_rarity_peak[1] if peak_hours else rod.fish_rarity_default[1]
    rare_chance = rod.fish_rarity_peak[2] if peak_hours else rod.fish_rarity_default[2]
    fish_table_tmp = merge_tables(common_table, common_chance, uncommon_table, uncommon_chance)
    fish_table = merge_tables(fish_table_tmp, common_chance + uncommon_chance, rare_table, rare_chance)
    junk_table = {"Common Junk": rod.junk_rarity[0], "Uncommon Junk": rod.junk_rarity[1],
                  "Rare Junk": rod.junk_rarity[2]}
    chance_fish = rod.fish_rate[0] if high_population else rod.fish_rate[1]
    final_table = merge_tables(fish_table, chance_fish, junk_table, 100 - chance_fish)
    return final_table


def merge_tables(table_1: dict[str, Union[float, int]], chance_1: int, table_2: dict[str, Union[float, int]],
                 chance_2: int) -> dict[str, Union[float, int]]:
    out_table = {}
    for entry, chance in table_1.items():
        if entry not in out_table:
            out_table[entry] = 0
        out_table[entry] += chance * chance_1 / (chance_1 + chance_2)
    for entry, chance in table_2.items():
        if entry not in out_table:
            out_table[entry] = 0
        out_table[entry] += chance * chance_2 / (chance_1 + chance_2)
    return out_table


def main():
    rod_names = ["Fishing Rod"]
    print(fish(True, True, Rods[0], Biomes[0]))


if __name__ == "__main__":
    main()
