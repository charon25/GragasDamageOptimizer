from spell import Spell


class Item():
    def __init__(self, id: int, name: str, stats: dict[str, float], cost: int, spell: Spell) -> None:
        self.id = id
        self.name: str = name
        self.stats: dict[str, float] = stats
        self.cost: int = cost
        self.spell: Spell = spell

    def __repr__(self) -> str:
        return self.name

class MythicItem(Item):
    def __init__(self, id: int, name: str, stats: dict[str, float], cost: int, spell: Spell, stats_per_item: dict[str, float]) -> None:
        super().__init__(id, name, stats, cost, spell)
        self.stats_per_item: dict[str, float] = stats_per_item

MYTHICS: tuple[MythicItem] = (
    MythicItem(0, 'Hextech Rocketbelt', {'ap': 90, 'haste': 15, 'hp': 250, 'mpen': 6}, 3200, Spell([125], {'ap': 0.15, 'hp': 0}, [40], True), {'mpen': 5}),
    MythicItem(1, "Liandry's Anguish", {'ap': 80, 'haste': 20, 'mana': 600}, 3200, Spell([50], {'ap': 0.06, 'hp': 0.04}, [4], True), {'haste': 5}), # Effet en +
    MythicItem(2, "Luden's Tempest", {'ap': 80, 'haste': 20, 'mana': 600, 'mpen': 6}, 3200, Spell([100], {'ap': 0.1, 'hp': 0}, [10], True), {'mpen': 5}),
    MythicItem(3, 'Night Harvester', {'ap': 90, 'haste': 25, 'hp': 300}, 3200, Spell([125], {'ap': 0.15, 'hp': 0}, [30], True), {'haste': 5}),
    MythicItem(4, 'Riftmaker', {'ap': 70, 'haste': 15, 'hp': 300, 'bonus': 0.06}, 3200, None, {'ap': 8}),
    MythicItem(5, 'Crown of the Shattered Queen', {'ap': 70, 'haste': 20, 'hp': 250, 'mana': 600}, 2800, None, {'ap': 8}), # Effet en +
    MythicItem(55, 'Everfrost', {'ap': 70, 'haste': 20, 'hp': 250, 'mana': 600}, 2800, Spell([100], {'ap': 0.3, 'hp': 0}, [30], True), {'ap': 10}),
    MythicItem(6, 'Imperial Mandate', {'ap': 40, 'haste': 20, 'hp': 200}, 2500, None, {'ap': 15})
)

LEGENDARIES: tuple[Item] = {
    Item(7, "Rabadon's Deathcap", {'ap': 120}, 3600, None), # Effet en +
    Item(8, 'Cosmic Drive', {'ap': 65, 'haste': 30, 'hp': 200}, 3000, None), # Effet en +
    Item(9, 'Demonic Embrace', {'ap': 75, 'hp': 350}, 3000, Spell([0], {'ap': 0, 'hp': 0.072}, [4], True)), # Effet en +
    Item(10, 'Horizon Focus', {'ap': 85, 'haste': 15, 'hp': 150, 'bonus': 0.1}, 3000, None),
    Item(11, 'Lich Bane', {'ap': 75, 'haste': 15}, 3000, None), # Effet en +
    Item(12, "Nashor's Tooth", {'ap': 100}, 3000, Spell([15], {'ap': 0.2, 'hp': 0}, [2], True)),
    Item(13, 'Shadowflame', {'ap': 100, 'hp': 200}, 3000, None), # Effet en +
    Item(14, "Zhonya's Hourglass", {'ap': 80, 'haste': 15}, 3000, None),
    Item(15, 'Void Staff', {'ap': 65, 'mpen_perc': 0.4}, 2800, None),
    Item(16, "Seraph's Embrace", {'ap': 80, 'hp': 250, 'mana': 860}, 2600, None), # Effet en +
    Item(17, "Banshee's Veil", {'ap': 80, 'haste': 10}, 2600, None),
    Item(18, "Rylai's Crystal Scepter", {'ap': 75, 'hp': 400}, 2600, None),
    Item(19, 'Morellonomicon', {'ap': 90, 'hp': 300}, 2500, None)
}

