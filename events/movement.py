from save_load.uid_converter import decoder
from GUI import GAME_WALL_DATA_PATH, GAME_REQUIRED_ITEM_PATH


def move_character(game_player: dict, path: int) -> None:
    """
    Update a player's current coorindate based on the given direction represented by an integer from 1 to 4 inclusive.

    :param game_player: a dictionary that contains integer values for keys "X-coordinate" and "Y-coordinate"
                        to represent the player's current coordinate
    :param path: an integer value between 1 and 4, inclusive, representing left, right, up or down respectively
    :precondition: game_player must be a dictionary whose keys named as "X-coordinate" and "Y-coordinate"
    :precondition: game_player must be a dictionary whose integer values associated
                   with the keys representing corrdinates
    :precondition: path must be a non-zero positive integer between 1 and 4 inclusive
    :postcondition: update a player's current coorindate based on the given direction
    :raises TypeError: if game_player is not a dictionary
                       if game_player does not conatin keys named as "X-coordinate" and "Y-coordinate"
    :raises ValueErrpr: if path is not a non-zero positive integer between 1 and 4 inclusive

    >>> character_in_game = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> move_character(game_player=character_in_game, path=2)
    >>> character_in_game
    {'X-coordinate': 1, 'Y-coordinate': 0}

    >>> move_character(game_player=character_in_game, path=1)
    >>> character_in_game
    {'X-coordinate': 0, 'Y-coordinate': 0}

    >>> move_character(game_player=character_in_game, path=4)
    >>> character_in_game
    {'X-coordinate': 0, 'Y-coordinate': 1}
    """
    if type(path) is not int or 0 >= path or path > 4:
        raise ValueError("path must be a non-zero positive integer between 1 and 4 inclusive")
    if type(game_player) is not dict or "X-coordinate" not in game_player or "Y-coordinate" not in game_player:
        raise TypeError("game_player must be a dictionary")
    key_coordinate = ("X-coordinate", "Y-coordinate")
    direction = key_coordinate[path // 3]
    value = (-1)**path
    game_player[direction] += int(value)


def board_validate_move(next_move: dict, environment: dict) -> bool:
    """
    Check whether the desired location represented by the dictionary is valid on the board layout.

    :param next_move: a dictionary that contains integer values for keys "X-coordinate" and "Y-coordinate"
                      to represent the player's desired coordinate
    :param environment: a dictionary that contains tuples of x and y coordinates to represent the keys
                        for all valid locations on the board
    :precondition: next_move must be a dictionary whose keys named as "X-coordinate" and "Y-coordinate"
    :precondition: next_move must be a dictionary whose integer values associated
                   with the keys representing coordinates
    :precondition: environment must be a dictionary that contains tuples of x and y coordinates to represent the keys
                   for all valid locations on the board
    :postcondition: check whether the desired location represented by the dictionary is valid on the board
    :return: True if the location represented by next_move is a valid spot on the board
    :raises TypeError: if next_move and/or environment is not a dictionary

    >>> coordinate = {"X-coordinate": 12, "Y-coordinate": 24}
    >>> valid_board = {(0, 0): 1, (0, 1): 2, (1, 0): 3, (1, 1): 4}
    >>> board_validate_move(coordinate, valid_board)
    False

    >>> next_coordinate = {"X-coordinate": 1, "Y-coordinate": 0}
    >>> board_validate_move(next_coordinate, valid_board)
    True

    >>> next_coordinate = {"X-coordinate": 0, "Y-coordinate": 0}
    >>> board_validate_move(next_coordinate, valid_board)
    True
    """
    if type(next_move) is not dict or type(environment) is not dict:
        raise TypeError("next_move and environment must be a dictionary")
    return tuple(next_move.values()) in list(environment.keys())


def route_validate_move(boundary_file: str, avatar: dict, heading: int) -> bool:
    """
    Check whether the desired travel direction is valid based on the player's location.

    :param boundary_file: a path linked to a plan text file that contains encoded Unicode characters representing the
                          invalid direction in each location, which can be converted into python dictionary format.
    :param avatar: a dictionary that contains integer values for keys "X-coordinate" and "Y-coordinate"
                      to represent the player's current coordinate
    :param heading: an integer value between 1 and 4, inclusive, that represents the player's desired travel direction
    :precondition: boundary_file must be a path linked to a plan text file that contains encoded Unicode characters,
                   which can be converted into python dictionary format
    :precondition: the decoded dictionary from boundary_file must contain integer keys ranging from 1 to 4,
                   representing left, right, up or down respectively
    :precondition: each key of the decoded dictionary from boundary_file is associated with a tuple of coordinates
    :precondition: avatar must be a dictionary whose keys named as "X-coordinate" and "Y-coordinate"
    :precondition: avatar must be a dictionary whose integer values associated
                   with the keys representing coordinates
    :precondition: heading must be an integer value between 1 and 4, inclusive
    :postcondition: check whether the desired move is valid based on a player's location
    :return: a Boolean value representing whether the player can travel in their desired direction
    :raises TypeError: if avatar is not a dictionary
                      if boundary_file does not contain an encoded python dictionary
    :raises FileNotFoundError: if file represented by boundary_file cannot be found
    :raises KeyError: if avatar does not contain keys named as "X-coordinate" and "Y-coordinate"
                     if heading cannot be found in the keys of the plan text file represented by boundary_file
    :raises ValueError: if path is not an non-zero integer less than or equal to 4
    """
    if type(heading) is not int or 0 >= heading or heading > 4:
        raise ValueError("path must be a non-zero positive integer between 1 and 4 inclusive")
    with open(boundary_file) as file_object:
        load_save = file_object.read()
    boundary_info = eval(decoder(load_save))
    current_coordinate = (avatar["X-coordinate"], avatar["Y-coordinate"])
    if current_coordinate in boundary_info[heading]:
        return False
    return True


def key_validate_move(key_file: str, next_move: dict, bag_info: dict) -> bool:
    """
    Check whether the required item needed in order to travel to the desired direction is obtained by the player

    :param key_file: a path linked to a plan text file that contains encoded Unicode characters representing
                     the required item needed for the desired location, which can be converted into
                     python dictionary format.
    :param next_move: a dictionary that contains integer values for keys "X-coordinate" and "Y-coordinate"
                      to represent the player's current coordinate
    :param bag_info: a dictionary that contains the name of game items as keys and their quantity as values
    :precondition: key_file must be a path linked to a plan text file that contains encoded Unicode characters,
                   which can be converted into python dictionary format
    :precondition: the decoded dictionary from key_file must contain tuple keys representing the coordinates, same
                   format as next_move
    :precondition: each key of the decoded dictionary from boundary_file is associated with a name of the required item
                   for entering the location
    :precondition: next_move must be a dictionary whose keys named as "X-coordinate" and "Y-coordinate"
    :precondition: next_move must be a dictionary whose integer values associated with the keys representing coordinates
    :precondition: bag_info must be a dictionary whose keys represented the name of the game item, same format as the
                   key of the decoded dictionary from key_file
    :precondition: bag_info must be a dictionary whose integer values represented the quantity of the game item
    :postcondition: check whether the desired move is valid based on a player's location and the items player has
    :return: a Boolean value representing whether the required item needed in order to travel to the
             desired direction is obtained by the player
    :raises TypeError: if next_move and/or bag_info is not a dictionary
                      if key_file does not contain an encoded python dictionary
    :raises FileNotFoundError: if file represented by key_file cannot be found
    """
    with open(key_file) as file_object:
        load_save = file_object.read()
    key_info = eval(decoder(load_save))
    if tuple(next_move.values()) in list(key_info.keys()) and key_info[tuple(next_move.values())] not in bag_info:
        return False
    return True


def player_movement(game_player: dict, path: int) -> bool:
    """
    Check whether the desired travel direction is allowed based the board layout, the player's location and the items
    player currently have

    :param game_player: a dictionary that contains the information of character as value of a key called "character" and
                        the information of the game environment as value of a key called "environment"
    :param path: an integer value between 1 and 4, inclusive, that represents the player's desired travel direction
    :precondition: path must be an integer value between 1 and 4, inclusive
    :precondition: game_player must be a dictionary that contains the information of character as value of a key
                   called "character" and the information of the game environment as value of a key called "environment"
    :precondition: the key ['character'] inside game_player should contain a dictionary having keys ['X-coordinate],
                   ['y-coordinate'] and ['items']
    :precondition: the key ['environment'] inside game_player should contain a dictionary having a tuple of available
                   coordinate for the game as the keys
    :postcondition: check whether the desired travel direction is allowed based the board layout,
                    the player's location and the items player currently have
    :return: a Boolean value representing whether the required item needed in order to travel to the
             desired direction is obtained by the player
    :raises TypeError: if game_player is not a dictionary
    :raises ValueError: if path is not an non-zero integer less than or equal to 4
    :raises KeyError: if game_player does not have keys named as ["character"] and ["environment"]
                      if game_player["character"] does not contain keys named as ["X-coordinate"], ["Y-coordinate"],
                      and ["Items"]
    """
    if type(path) is not int or 0 >= path or path > 4:
        raise ValueError("path must be an integer value between 1 and 4, inclusive!")
    coordinate_copy = {"X-coordinate": game_player['character']["X-coordinate"],
                       "Y-coordinate": game_player['character']["Y-coordinate"]}
    move_character(coordinate_copy, path)
    valid_move = board_validate_move(coordinate_copy, game_player['environment'])
    route_check = route_validate_move(GAME_WALL_DATA_PATH, game_player['character'], path)
    key_check = key_validate_move(GAME_REQUIRED_ITEM_PATH, coordinate_copy, game_player['character']['Items'])
    if valid_move is True and route_check is True and key_check is True:
        move_character(game_player['character'], path)
        return True
    return False


def main():
    """
    Drive the program
    """


if __name__ == "__main__":
    main()
