import random
from GUI import GAME_FOE_DATA_PATH


def check_for_predetermined_events(game_player: dict) -> str:
    """
    Checks if there are any predetermined events in the player's current coordinate.

    :param game_player: a dictionary that contains the information of character as value of a key called "character" and
                        the information of the game environment as value of a key called "environment"
    :precondition: game_player must be a dictionary that contains the information of character as value of a key
                   called "character" and the information of the game environment as value of a key called "environment"
    :precondition: the key ['character'] inside game_player should contain a dictionary having keys ['X-coordinate'] and
                   ['y-coordinate']
    :precondition: the key ['environment'] inside game_player should contain a dictionary having a tuple of available
                   coordinate for the game as the keys
    :postcondition: checks if there are any predetermined events in the player's current coordinate
    :return: a string that represents the type of event player is expected to encounter in this coordinate
    :raises KeyError: if game_player does not have keys named as ["character"] and ["environment"]
                      if game_player["character"] does not contain keys named as ["X-coordinate"] and ["Y-coordinate"]
                      if player's current_coordinate is not one of the keys inside game_player['environment']

    >>> player = {'character': {'X-coordinate': 1, 'Y-coordinate': 2}, 'environment': {(1, 2): ('BOSS', 'Nathan')}}
    >>> check_for_predetermined_events(player)
    'Nathan'

    >>> player = {'character': {'X-coordinate': 1, 'Y-coordinate': 2}, 'environment': {(1, 2): ('Random', '')}}
    >>> check_for_predetermined_events(player)
    'Random'
    """
    avatar = game_player['character']
    current_coordinate = (avatar["X-coordinate"], avatar["Y-coordinate"])
    if current_coordinate not in game_player['environment']:
        raise KeyError("Invalid datapoint! Reload last save to continue!")
    predetermined_events = game_player['environment'][current_coordinate][1]
    return "Random" if not predetermined_events else predetermined_events


def pick_available_foe(happened_event, max_level_foe):
    sample_monster = {
        1: {'Name': 'Megalizard', 'EXP': 20, 'HP': 50, 'Items': ['Healing Potion'], 'PROBABILITY': 30, 'Strength': 23, 'Dexterity': 5,
            'Intelligence': 20, 'Magic Resistance': 999},
        2: {'Name': 'Skeletons ', 'EXP': 30, 'HP': 70, 'Items': ['Healing Potion'], 'PROBABILITY': 30, 'Strength': 25, 'Dexterity': 10,
            'Intelligence': 25, 'Magic Resistance': 26},
        3: {'Name': 'Venomweaver', 'EXP': 40, 'HP': 80, 'Items': ['Status Potion'], 'PROBABILITY': 30, 'Strength': 30, 'Dexterity': 30,
            'Intelligence': 30, 'Magic Resistance': 40},
        4: {'Name': 'Hydra', 'EXP': 80, 'HP': 100, 'Items': ['Healing Potion'], 'PROBABILITY': 30, 'Strength': 37, 'Dexterity': 50,
            'Intelligence': 46, 'Magic Resistance': 999},
        5: {'Name': 'Griffin', 'EXP': 100, 'HP': 120, 'Items': ['Attribute Potion'], 'PROBABILITY': 30, 'Strength': 37, 'Dexterity': 50,
            'Intelligence': 46, 'Magic Resistance': 26}}
    if happened_event == "RANDOM":
        picked_foe = random.randint(1, min(max_level_foe, len(sample_monster)))
        sample_monster[picked_foe]['EXP'] = int(random.uniform(1, 2) * sample_monster[picked_foe]['EXP'])
        return sample_monster[picked_foe]
    elif happened_event == "MID-BOSS":
        return {'Name': 'MID-BOSS', 'EXP': 500, 'HP': 80, 'Items': ['Sanctum Key'], 'PROBABILITY': 100, 'Strength': 30, 'Dexterity': 30,
                'Intelligence': 30, 'Magic Resistance': 40}
    elif happened_event == "FINAL-BOSS":
        return {'Name': 'FINAL-BOSS', 'EXP': 500, 'HP': 80, 'Items': ['Oasis Explorer'], 'PROBABILITY': 100, 'Strength': 30,
                'Dexterity': 30, 'Intelligence': 30, 'Magic Resistance': 40}
    else:
        return {}
