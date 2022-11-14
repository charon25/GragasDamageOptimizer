from spell import Spell


Q_SPELL_UNCHARGED = Spell([80, 120, 160, 200, 240], {'ap': 0.8, 'hp': 0}, [10, 9, 8, 7, 6])
Q_SPELL_CHARGED = Spell([120, 180, 240, 300, 360], {'ap': 1.2, 'hp': 0}, [10, 9, 8, 7, 6])
W_SPELL = Spell([20, 50, 80, 110, 140], {'ap': 0.7, 'hp': 0.07}, [5, 5, 5, 5, 5])
E_SPELL = Spell([80, 125, 170, 215, 260], {'ap': 0.6, 'hp': 0}, [14, 13.5, 13, 12.5, 12])
R_SPELL = Spell([200, 300, 400], {'ap': 0.8, 'hp': 0}, [120, 100, 80])


def get_positive_int_input(prompt: str, default: int) -> int:
    value = input(prompt.format(default))
    if not value:
        return default

    while not value.isnumeric():
        value = input(prompt.format(default))

    return int(value)


def get_parameters() -> dict[str, int]:
    enemy_health = get_positive_int_input("Enemy HP ({}) ? ", 2000)
    enemy_magic_resistance = get_positive_int_input("Enemy MR ({}) ? ", 30)
    starting_ap = get_positive_int_input("Base AP ({}) ? ", 0)
    starting_magic_penetration = get_positive_int_input("Base Magic pen ({}) ? ", 0)
    starting_haste = get_positive_int_input("Base haste ({}) ? ", 0)
    has_sorcs = bool(get_positive_int_input("Sorcerer's Shoes ? ", 0))
    is_q_charged = bool(get_positive_int_input("With charged Q ? ", 0))

    return {'hp': enemy_health, 'mr': enemy_magic_resistance, 'ap': starting_ap, 'mpen': starting_magic_penetration, 'haste': starting_haste, 'sorc': has_sorcs, 'q_charged': is_q_charged}

def optimize():
    parameters = get_parameters()


if __name__ == '__main__':
    optimize()
