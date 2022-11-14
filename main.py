
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

    return {'hp': enemy_health, 'mr': enemy_magic_resistance, 'ap': starting_ap, 'mpen': starting_magic_penetration, 'haste': starting_haste, 'sorc': has_sorcs}

def optimize():
    parameters = get_parameters()


if __name__ == '__main__':
    optimize()
