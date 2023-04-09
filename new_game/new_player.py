import random


def status_reset(player_attribute):
    """
    Set a character's health point, magical point and status based on their attributes

    :param player_attribute: a dictionary that contains the description of the character's attributes as
                             key and its corresponding data as values
    :precondition: player_attribute must be a dictionary that contains the description of the character's attributes as
                   key and its corresponding data as values
    :precondition: player_attribute must contain "Max HP", "Max MP", "Current HP", "Current MP" or "Status" as keys
    :postcondition: set a character's health point, magical point and status based on their attributes
    :raise TypeError: if player_attribute is not a dictionary
    :raise KeyError: if player_attribute does not contain "Strength", "Intelligence", "Dexterity" and "Magix Power"
                     as keys
    >>> player = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32}
    >>> status_reset(player)
    >>> player
    {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32, 'Max HP': 80, 'Max MP': 80, \
'Current HP': 80, 'Current MP': 80, 'Status': 'Healthy'}
    """
    player_attribute['Max HP'] = max(round(player_attribute['Strength'] + player_attribute['Intelligence'], -1), 60)
    player_attribute['Max MP'] = max(round(player_attribute['Dexterity'] + player_attribute['Magic Power'], -1), 60)
    player_attribute['Current HP'] = player_attribute['Max HP']
    player_attribute['Current MP'] = player_attribute['Max MP']
    player_attribute['Status'] = 'Healthy'


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
