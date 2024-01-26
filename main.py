from fishing_rod import ROD_ALIKRI, ROD_ARGONIAN, ROD_DEFAULT, ROD_DWARVEN
from biome import *
from typing import Union


def merge_tables(table_1: dict[str, Union[float, int]], chance_1: int, table_2: dict[str, Union[float, int]],
                 chance_2: int) -> dict[str, Union[float, int]]:
    out_table = {}
    for entry, chance in table_1.items():
        if entry not in out_table:
            out_table[entry] = 0
        out_table[entry] += chance * chance_1 / 100
    for entry, chance in table_2.items():
        if entry not in out_table:
            out_table[entry] = 0
        out_table[entry] += chance * chance_2 / 100
    return out_table


def main():
    pass


if __name__ == "__main__":
    main()
