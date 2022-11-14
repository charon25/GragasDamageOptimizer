class Spell:
    def __init__(self, base_damages: list[int], ratios: dict[str, float], cooldowns: list[float]) -> None:
        self.base_damages: list[int] = list()
        self.ratios: dict[str, float] = {'ap': 0, 'hp': 0}
        self.cooldowns: list[float] = list()

    def compute_damage(self, level: int, stats: dict[str, int]) -> float:
        true_damages = self.base_damages[level] + stats['ap'] * self.ratios['ap'] + stats['hp'] * self.ratios['hp']
        reduction = 100 / (100 + stats['mr'] - stats['mpen'])
        return true_damages * reduction

    def compute_dps(self, level: int, stats: dict[str, int]) -> float:
        cooldown = self.cooldowns[level] * (100 / (100 + stats['haste']))
        return self.compute_damage(level, stats) / cooldown
