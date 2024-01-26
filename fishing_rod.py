from typing import Union


class Rod:
    def __init__(
            self,
            fish_rate: tuple[int, int] = (90, 80),
            fish_rarity_default: tuple[int, int] = (75, 22),
            fish_rarity_peak: tuple[int, int] = (65, 27),
            junk_rarity: tuple[int, int] = (65, 32),
            small_fish_rate: int = 50,
            allowed_rares: Union[None, list[str]] = None
    ):
        """
        Defines the stats for a fishing rod. All rates are expressed as percentages times 100; 50% is 50.
        :param fish_rate: The rate at which you catch fish (rather than junk), at high and low population.
        :param fish_rarity_default: The rates of common and uncommon fish, during regular fishing hours.
        :param fish_rarity_peak: The rates of common and uncommon fish, during peak (6-9 am/pm) fishing hours.
        :param junk_rarity: The rates of common and uncommon junk.
        :param small_fish_rate: The rate at which small fish are caught vs big fish.
        :param allowed_rares: A list of rare fish that may be caught by this rod.
        """
        self.fish_rate = list(fish_rate) + [100 - sum(fish_rate)]
        self.fish_rarity_default = list(fish_rarity_default) + [100 - sum(fish_rarity_default)]
        self.fish_rarity_peak = list(fish_rarity_peak) + [100 - sum(fish_rarity_peak)]
        self.junk_rarity = list(junk_rarity) + [100 - sum(junk_rarity)]
        self.small_fish_rate = small_fish_rate
        self.large_fish_rate = 100 - small_fish_rate
        self.allowed_rares = ["Rare Junk"] + (allowed_rares or [])


ROD_DEFAULT = Rod()
ROD_ALIKRI = Rod(fish_rarity_default=(55, 35), fish_rarity_peak=(45, 40), small_fish_rate=80,
                 allowed_rares=["Angelfish", "Lyretail Anthias"])
ROD_ARGONIAN = Rod(fish_rarity_default=(55, 35), fish_rarity_peak=(45, 40), small_fish_rate=20,
                   allowed_rares=["Angler", "Scorpion Fish"])
ROD_DWARVEN = Rod(fish_rate=(60, 20), junk_rarity=(35, 56))

Rods = [ROD_DEFAULT, ROD_ALIKRI, ROD_ARGONIAN, ROD_DWARVEN]
