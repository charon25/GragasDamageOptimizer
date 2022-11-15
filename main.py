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
    enemy_health = get_positive_int_input("Enemy HP ({}) ? ", 2000)
    enemy_magic_resistance = get_positive_int_input("Enemy MR ({}) ? ", 30)
    starting_ap = get_positive_int_input("Base AP ({}) ? ", 0)
    starting_magic_penetration = get_positive_int_input("Base Magic pen ({}) ? ", 0)
    starting_haste = get_positive_int_input("Base haste ({}) ? ", 0)
    has_sorcs = get_boolean_input("Sorcerer's Shoes ({}) ? ", True)
    is_q_charged = get_boolean_input("With charged Q ({}) ? ", True)
    level = get_positive_int_input("Level ({}) ? ", 11)
    golds = get_positive_int_input("Golds ({}) ? ", 100000)
    items = get_string_input("Items ({}) ? ", 'm4', r'[mM]?[1-5]').lower()

    return {'hp': enemy_health, 'mr': enemy_magic_resistance, 'ap': starting_ap, 'mpen': starting_magic_penetration, 'haste': starting_haste, 'sorc': has_sorcs, 'q_charged': is_q_charged, 'level': level, 'golds': golds, 'items': items}


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


def optimize():
    # parameters = get_parameters()
    parameters = {'hp': 2000, 'mr': 30, 'ap': 0, 'mpen': 0, 'haste': 0, 'sorc': True, 'q_charged': True, 'level': 11, 'golds': 100000, 'items': 'm4'}

    SPELLS = [E_SPELL, W_SPELL, R_SPELL]
    SPELLS.append(Q_SPELL_CHARGED if parameters['q_charged'] else Q_SPELL_UNCHARGED)

    legendaries_count = int(parameters['items'][-1])
    base_stats = {'ap': parameters['ap'], 'hp': 0, 'mpen': parameters['mpen'] + 18 * parameters['sorc'], 'haste': parameters['haste'], 'mana': 0, 'bonus': 0, 'mpen_perc': 0}

    for build in get_builds(parameters['items']):
        current_stats = dict(base_stats)
        if 'm' in parameters['items']:
            build: tuple[Item] = (build[0], *build[1])
            add_stats(current_stats, build[0].stats_per_item, legendaries_count)

        items_ids = [item.id for item in build]
        if 1 in items_ids:
            bonus_health = parameters['hp'] - GRAGAS_HP[parameters['level']]
            current_stats['bonus'] += 0.012 * (bonus_health // 125)


if __name__ == '__main__':
    optimize()
