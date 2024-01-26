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
    rod_names = ["Fishing Rod", "Alik'ri Rod", "Argonian Rod", "Dwarven Rod"]
    biome_names = ["Arctic", "Underground", "Lakes, Clear", "Lakes, Raining", "Streams, Clear", "Streams, Raining"]
    populations = {True: "High Population", False: "Low Population"}
    times = {True: "Peak Hours", False: "Normal Hours"}
    best_places: dict[str, tuple[float, tuple[str, str, str, str]]] = {}
    for rod_id, rod_name in enumerate(rod_names):
        for biome_id, biome_name in enumerate(biome_names):
            for high_pop, pop_name in populations.items():
                for peak_time, time_name in times.items():
                    fish_result = fish(peak_time, high_pop, biome=Biomes[biome_id], rod=Rods[rod_id])
                    for fish_name, fish_chance in fish_result.items():
                        if fish_name not in best_places:
                            best_places[fish_name] = (0.0, ("", "", "", ""))
                        if fish_chance >= best_places[fish_name][0]:
                            best_places[fish_name] = (fish_chance, (rod_name, biome_name, pop_name, time_name))
    for fish_name, result_tuple in best_places.items():
        print(fish_name, end="\t")
        print(f"{result_tuple[0]:0.1f}%", end="\t")
        print(result_tuple[1][0], end="\t")
        print(result_tuple[1][1], end="\t")
        print(result_tuple[1][2], end="\t")
        print(result_tuple[1][3])


if __name__ == "__main__":
    main()
