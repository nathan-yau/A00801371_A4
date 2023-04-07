import random


def create_character(name) -> dict:
    """
    Create a dictionary that contains the starting coordinates and health points (HP) of a character.

    :postcondition: create a dictionary that contains starting coordinates and health points (HP) of a character
    :return: a dictionary that contains the starting coordinates and health points (HP) of a character
    """

    keys = ["Name", "Level", "NEXT LV (EXP)", "Status", "X-coordinate", "Y-coordinate", "Items",
            "Current HP", "Current MP", "Max HP", "Max MP",
            "Strength", "Dexterity", "Intelligence", "Magic Power"]
    values = [name, 1, int(60*(random.uniform(1.5, 1.9))), "Healthy", 4, 4, {'Sanctum Key': 1, 'Healing Potion': 2,
                                                                          'Status Potion': 2, 'Attribute Potion': 2,
                                                                    'The Amulet of Knowledge': 1,
                                                                    'Oasis Explorer': 1}, 50, 50, 50, 50]
    while sum(values[11:]) < 160:
        [values.append(random.randint(30, 50)) for _ in keys]
    attributes = dict(zip(keys, values))
    attributes['Max HP'] = max(round(attributes['Strength'] + attributes['Intelligence'], -1), 60)
    attributes['Max MP'] = max(round(attributes['Dexterity'] + attributes['Magic Power'], -1), 60)
    attributes['Current HP'] = attributes['Max HP']
    attributes['Current MP'] = attributes['Max MP']
    return attributes


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
