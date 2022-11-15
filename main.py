from itertools import product, combinations
import distutils.util
import re

from items import Item, LEGENDARIES, MYTHICS 
from spell import Spell


Q_SPELL_UNCHARGED = Spell([80, 120, 160, 200, 240], {'ap': 0.8, 'hp': 0}, [10, 9, 8, 7, 6])
Q_SPELL_CHARGED = Spell([120, 180, 240, 300, 360], {'ap': 1.2, 'hp': 0}, [10, 9, 8, 7, 6])
W_SPELL = Spell([20, 50, 80, 110, 140], {'ap': 0.7, 'hp': 0.07}, [5, 5, 5, 5, 5])
E_SPELL = Spell([80, 125, 170, 215, 260], {'ap': 0.6, 'hp': 0}, [14, 13.5, 13, 12.5, 12])
R_SPELL = Spell([200, 300, 400], {'ap': 0.8, 'hp': 0}, [120, 100, 80])

GRAGAS_HP = (0, 670, 748.48, 830.78, 916.89, 1006.81, 1100.55, 1198.11, 1299.47, 1404.66, 1513.66, 1626.48, 1743.11, 1863.55, 1987.81, 2115.89, 2247.78, 2383.48, 2523)
GRAGAS_AD = (0, 64, 66.522, 69.16, 71.93, 74.82, 77.83, 80.96, 84.21, 87.59, 91.09, 94.71, 98.46, 102.33, 106.32, 110.43, 114.66, 119.02, 123.5)

SPELLS_LEVELING = (
    (0, 1, 1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5),
    (0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 5),
    (0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 3, 4, 5)
)

def get_positive_int_input(prompt: str, default: int) -> int:
    value = input(prompt.format(default))
    if not value:
        return default
    
    try:
        return int(value)
    except Exception:
        return default

def get_boolean_input(prompt: str, default: bool) -> bool:
    value = input(prompt.format(('0', '1')[default]))
    if not value:
        return default

    try:
        return distutils.util.strtobool(value)
    except Exception:
        return default

def get_string_input(prompt: str, default: str, re_match: str) -> str:
    value = input(prompt.format(default))
    if not value:
        return default

    try:
        return value if re.match(re_match, value) else default
    except Exception:
        return default


def get_parameters() -> dict[str, int]:
    enemy_health = get_positive_int_input("> Enemy HP ({}) ? ", 2000)
    enemy_magic_resistance = get_positive_int_input("> Enemy MR ({}) ? ", 30)
    starting_ap = get_positive_int_input("> Base AP ({}) ? ", 0)
    starting_magic_penetration = get_positive_int_input("> Base Magic pen ({}) ? ", 0)
    starting_haste = get_positive_int_input("> Base haste ({}) ? ", 0)
    has_sorcs = get_boolean_input("> Sorcerer's Shoes ({}) ? ", True)
    is_q_charged = get_boolean_input("> With charged Q ({}) ? ", False)
    level = get_positive_int_input("> Level ({}) ? ", 11)
    golds = get_positive_int_input("> Golds ({}) ? ", 100000)
    items = get_string_input("> Items ({}) ? ", 'm4', r'[mM]?[1-5]').lower()
    maxing = get_string_input("> Max [q/w/e] ({}) ? ", 'qew', r'qwe|qew|wqe|weq|eqw|ewq').lower()

    return {'hp': enemy_health, 'mr': enemy_magic_resistance, 'ap': starting_ap, 'mpen': starting_magic_penetration, 'haste': starting_haste, 'sorc': has_sorcs, 'q_charged': is_q_charged, 'level': level, 'golds': golds, 'items': items, 'maxing': maxing}


def get_builds(items: str):
    legendaries_count = int(items[-1])
    if 'm' in items:
        return product(MYTHICS, combinations(LEGENDARIES, r=legendaries_count))
    else:
        return combinations(LEGENDARIES, r=legendaries_count)

# In place
def add_stats(stats1: dict[str, int], stats2: dict[str, int], multiplier: float = 1.0) -> dict[str, int]:
    for stat, value in stats2.items():
        stats1[stat] = stats1.get(stat, 0) + value * multiplier

def get_spell_levels_by_maxing(level: int, maxing: str) -> list[int]:
    indexes = {'e': 0, 'w': 1, 'r': 2, 'q': 3}
    spell_levels = [0, 0, 0, 0]
    for i, char in enumerate(maxing):
        spell_levels[indexes[char]] = SPELLS_LEVELING[i][level]
    spell_levels[2] = (level - 1) // 5
    return spell_levels


def optimize():
    parameters = get_parameters()
    # parameters = {'hp': 2500, 'mr': 45, 'ap': 30, 'mpen': 5, 'haste': 10, 'sorc': True, 'q_charged': 0, 'level': 16, 'golds': 100000, 'items': 'm4', 'maxing': 'qew'}

    SPELLS = [E_SPELL, W_SPELL, R_SPELL]
    SPELLS.append(Q_SPELL_CHARGED if parameters['q_charged'] else Q_SPELL_UNCHARGED)
    spells_levels = get_spell_levels_by_maxing(parameters['level'], parameters['maxing'])

    legendaries_count = int(parameters['items'][-1])
    base_stats = {'ap': parameters['ap'], 'hp': 0, 'mpen': parameters['mpen'] + 18 * parameters['sorc'], 'haste': parameters['haste'], 'mana': 0, 'bonus': 0, 'mpen_perc': 0, 'enn_hp': parameters['hp'], 'enn_mr': parameters['mr']}

    damages_by_build: dict[tuple[str], float] = dict()
    dps_by_build: dict[tuple[str], float] = dict()

    for build in get_builds(parameters['items']):
        current_stats = dict(base_stats)
        if 'm' in parameters['items']:
            build: tuple[Item] = (build[0], *build[1])
            add_stats(current_stats, build[0].stats_per_item, legendaries_count)

        if sum(item.cost for item in build) > parameters['golds']:
            continue

        items_spells: list[Spell] = list()
        for item in build:
            add_stats(current_stats, item.stats)
            if not item.spell is None:
                items_spells.append(item.spell)


        items_ids = [item.id for item in build]
        # Effets des mythiques
        if 1 in items_ids: # Liandry's Anguish
            bonus_health = parameters['hp'] - GRAGAS_HP[parameters['level']]
            if bonus_health < 0:
                bonus_health = 0
            current_stats['bonus'] += 0.012 * (bonus_health // 125)
        elif 5 in items_ids: # Crown of the Shattered Queen
            bonus_ap = 10 + (3 * (parameters['level'] - 8) if parameters['level'] >= 9 else 0)
            current_stats['ap'] += bonus_ap

        # Effets des légendaires
        if 8 in items_ids: # Cosmic Drive
            # Normalement +40 après 3 attaques, mais moyenné à +20
            current_stats['ap'] += 20
        if 9 in items_ids: # Demonic Embrace
            current_stats['ap'] += 0.02 * current_stats['hp']
        if 11 in items_ids: # Lich Bane
            items_spells.append(Spell([0.75 * GRAGAS_AD[parameters['level']]], {'ap': 0.5, 'hp': 0}, [1.5], True))
        if 13 in items_ids: # Shadowflame
            current_stats['mpen'] += 10 + max(0, (2500 - parameters['hp']) // 150)
        if 16 in items_ids: # Seraph's Embrace
            current_stats['haste'] += 0.013 * current_stats['mana']
        if 7 in items_ids: # Rabadon's Deathcap
            current_stats['ap'] *= 1.35

        total_damages = 0
        total_dps = 0
        for k, spell in enumerate(SPELLS):
            total_damages += spell.compute_damage(spells_levels[k] - 1, current_stats)
            total_dps += spell.compute_dps(spells_levels[k] - 1, current_stats)
        for spell in items_spells:
            total_damages += spell.compute_damage(0, current_stats)
            total_dps += spell.compute_dps(0, current_stats)

        build_str = tuple(item.name for item in build)
        damages_by_build[build_str] = total_damages
        dps_by_build[build_str] = total_dps

    damages_by_build = [(build_str, damages) for build_str, damages in sorted(damages_by_build.items(), key=lambda kv:kv[1], reverse=True)]
    dps_by_build = [(build_str, dps) for build_str, dps in sorted(dps_by_build.items(), key=lambda kv:kv[1], reverse=True)]

    print("\n")
    print(f"> Enemy : {parameters['hp']} HP - {parameters['mr']} Magic Resist")
    print(f"> Runes : {parameters['ap']} AP - {parameters['haste']} Haste - {parameters['mpen']} Magic Pen")
    print(f"> Level : {parameters['level']} - Q : {'' if parameters['q_charged'] else 'un'}charged")
    print(f"> Golds : {'∞' if parameters['golds'] > 50000 else parameters['golds']} - With Sorcerer's Shoes : {parameters['sorc']}")
    print(f"> Build : {'1 Mythic with ' if 'm' in parameters['items'] else ''}{parameters['items'][-1]} legendary items")
    print(f"> Maxing : {parameters['maxing'].upper()}")

    print()
    print(" === BURST\n\n 3 bests builds :")
    for i in range(3):
        print(f"  {i+1}. {damages_by_build[i][1]:.0f} dmg : {' - '.join(damages_by_build[i][0])}")

    print("\n\n === DPS\n\n 3 bests builds :")
    for i in range(3):
        print(f"  {i+1}. {dps_by_build[i][1]:.0f} dmg/s : {' - '.join(dps_by_build[i][0])}")


if __name__ == '__main__':
    optimize()
