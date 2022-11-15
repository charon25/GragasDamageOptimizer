class Spell:
    def __init__(self, base_damages: list[int], ratios: dict[str, float], cooldowns: list[float], is_from_item: bool = False) -> None:
        self.base_damages: list[int] = base_damages
        self.ratios: dict[str, float] = ratios
        self.cooldowns: list[float] = cooldowns
        self.is_from_item = is_from_item

    def compute_damage(self, level: int, stats: dict[str, int]) -> float:
        if self.is_from_item:
            level = 0

        true_damages = self.base_damages[level] + stats['ap'] * self.ratios['ap'] + stats['enn_hp'] * self.ratios['hp']
        reduction = 100 / (100 + stats['enn_mr'] * (1 - stats['mpen_perc']) - stats['mpen'])
        if reduction < 0:
            reduction = 0
        if reduction > 1:
            reduction = 1
        return true_damages * reduction * (1 + stats['bonus'])

    def compute_dps(self, level: int, stats: dict[str, int]) -> float:
        if self.is_from_item:
            level = 0

        cooldown = self.cooldowns[level]
        if not self.is_from_item:
            cooldown *= (100 / (100 + stats['haste']))

        return self.compute_damage(level, stats) / cooldown
