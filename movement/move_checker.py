from save_load.uid_converter import decoder


def move_character(game_player, path):
    key_coordinate = ("X-coordinate", "Y-coordinate")
    direction = key_coordinate[path // 3]
    value = (-1)**path
    game_player[direction] += int(value)


def board_validate_move(next_move, environment):
    if tuple(next_move.values()) in list(environment.keys()):
        return True
    return False


def route_validate_move(boundary_file, game_info, heading):
    with open(boundary_file) as file_object:
        load_save = file_object.read()
    boundary_info = eval(decoder(load_save))
    avatar = game_info['character']
    current_coordinate = (avatar["X-coordinate"], avatar["Y-coordinate"])
    if current_coordinate in boundary_info[heading]:
        return False
    return True


def key_validate_move(key_file, next_move, game_info):
    bag_info = game_info['Items']
    with open(key_file) as file_object:
        load_save = file_object.read()
    key_info = eval(decoder(load_save))
    if tuple(next_move.values()) in list(key_info.keys()) and key_info[tuple(next_move.values())] not in bag_info:
        return False
    return True


def movement_check(game_player, path):
    coordinate_copy = {"X-coordinate": game_player['character']["X-coordinate"],
                       "Y-coordinate": game_player['character']["Y-coordinate"]}
    move_character(coordinate_copy, path)
    valid_move = board_validate_move(coordinate_copy, game_player['environment'])
    route_check = route_validate_move('./data/boundary.gamedata', game_player, path)
    key_check = key_validate_move('./data/map_trigger_item.gamedata', coordinate_copy, game_player['character'])
    if valid_move is True and route_check is True and key_check is True:
        move_character(game_player['character'], path)
        return True


def main():
    """
    Drive the program
    """
    board_validate_move('./data/boundary.gamedata')


if __name__ == "__main__":
    main()
