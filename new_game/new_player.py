import random


def status_reset(player_attribute: dict) -> None:
    """
    Set a character's health point, magical point and status based on their attributes

    :param player_attribute: a dictionary that contains the description of the character's attributes as
                             key and its corresponding data as values
    :precondition: player_attribute must be a dictionary that contains the description of the character's attributes as
                   key and its corresponding data as values
    :precondition: player_attribute must contain "Strength", "Intelligence", "Dexterity" and "Magix Power" as keys
    :postcondition: set a character's health point, magical point and status based on their attributes
    :raises TypeError: if player_attribute is not a dictionary
                       if "Strength", "Intelligence", "Dexterity" and"Magix Power" are not paired up with
                       numeric value in player_attribute
    :raises KeyError: if player_attribute does not contain "Strength", "Intelligence", "Dexterity" and"Magix Power"
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


def create_character(name: str) -> dict:
    """
    Create a dictionary that contains the starting coordinates at (4, 4), health points (HP), name and other attributes
    of a character.

    :param name: a non-empty string that represents the character's name
    :precondition: name must be a string that represents the character's name
    :postcondition: create a dictionary that contains initial attributes and name of a character
    :return: a dictionary that contains initial attributes and name of a character
    :raises TypeError: if name is not a string
    """
    keys = ["Name", "Level", "NEXT LV (EXP)", "Status", "X-coordinate", "Y-coordinate", "Items", "Escape",
            "Current HP", "Current MP", "Max HP", "Max MP", "Strength", "Dexterity", "Intelligence", "Magic Power",
            "Magic Resistance"]
    values = [name, 1, int(60*(random.uniform(1.5, 1.9))), "Healthy", 4, 4, {}, False, 50, 50, 50, 50]
    number_of_random_attribute = len(values)
    if type(name) is not str or len(name) == 0:
        raise TypeError("Name of the character must be a non-empty string!")
    [values.append(random.randint(30, 50)) for _ in keys[number_of_random_attribute:]]
    attributes = dict(zip(keys, values))
    status_reset(attributes)
    return attributes


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
