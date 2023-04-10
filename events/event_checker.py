import random
from GUI import GAME_FOE_DATA_PATH
from save_load.uid_converter import decoder


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


def pick_available_foe(happened_event: str, game_info: dict, foe_data: str = GAME_FOE_DATA_PATH) -> dict:
    """
    Picks a random foe from the game foe data based on the player current level, key items and locations.

    :param happened_event: a string that indicate the specific event the player currently encounter
    :param game_info: a dictionary that contains the information of character as value of a key called "character" and
                        the information of the game environment as value of a key called "environment"
    :param foe_data: a string that refers to the path of the encoded game date that contains foe information
    :precondition: happened_event must be a string that indicate the specific event the player currently encounter
    :precondition: game_player must be a dictionary that contains the information of character as value of a key
                   called "character" and the information of the game environment as value of a key called "environment"
    :precondition: the key ['character'] inside game_player should contain a dictionary having keys ['Level'] and
                   ['Items']
    :precondition: foe_data must be a string that refers to the path of the encoded game date that
                   contains foe information
    :precondition: the encoded game data from foe_data must be a dictionary that contains an integer or string as keys
                   and a dictionary representing the foe's attributes and information.
    :precondition: the dictionary representing the foe's attributes and information must contain "EXP"
    :postcondition: picks a random foe from the game data based on the player current level, key items and locations
    :return: an empty dictionary or a dictionary that contains the information of a foe
    :raises KeyError: if ['character'] cannot be found inside game_player
                      if ['Level'] and ['Items'] cannot be found inside game_player['character']
                      if the foe information inside encoded dictionary does not have key ["EXP"]
    :raises TypeError: if the decoded message is not a dictionary
    """
    with open(foe_data) as file_object:
        foe_data = eval(decoder(file_object.read()))
    if type(foe_data) is not dict:
        raise TypeError("the decoded message from boundary_file must represent a dictionary.")
    if happened_event == "Random" and random.randint(1, 10) <= 3:
        picked_foe = random.randint(1, min(game_info['character']['Level'], len(foe_data)-2))
        foe_data[picked_foe]['EXP'] = int(random.uniform(1, 2) * foe_data[picked_foe]['EXP'])
        return foe_data[picked_foe]
    elif happened_event == "Sage Thorne" and 'The Amulet of Knowledge' in game_info['character']['Items']:
        return foe_data[happened_event]
    elif happened_event == "General Havoc" and 'Sanctum Key' in game_info['character']['Items']:
        return foe_data[happened_event]
    else:
        return {}


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
