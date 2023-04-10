from GUI_update.update_map_widget import map_widget_update
from combat.combat_widget import toggle_battle_buttons
from combat.player_info import exp_calculator

from GUI import DEFAULT_FONT


def escape_from_fight(overall_gui_info: dict, game_info: dict, saved_coordinate: tuple) -> None:
    """
    Update script, enemy info, player info and map widgets upon a successful escape from foe.

    :param overall_gui_info: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param game_info: a dictionary that contains the information of character as value of a key called "character" and
                      the information of the game environment as value of a key called "environment"
    :param saved_coordinate: a tuple that represents the location of the midd-progress boss
    :precondition: overall_gui_info must be a dictionary
    :precondition: game_info must be a dictionary
    :precondition: saved_coordinate must be a tuple that represents the coordinate of the location
    :precondition: overall_gui_info must contain key named as ['Script Frame']
    :precondition: the value of ['Script Frame'] key must be a tkinter Frame
    :precondition: the tkinter Frame of overall_gui_info['Script Frame'] must contain a tkinter label named as
                   ['script display'] and ['enemy_info']
    :precondition: game_info must contain key named as ['character']
    :precondition: the value of ['character'] inside game_info must contain keys ["X-coordinate"] and ["Y-coordinate"]
    :precondition: saved_coordinate must contain keys of tuple of coordinates
    :raises KeyError: if overall_gui_info does not contain key ['Script Frame']
                      if ['Script Frame'] does not have a widget named as ['script display'] and ['enemy_info']
                      if game_info does not contain key ['character']
                      if ['character'] inside game_info must contain keys ["X-coordinate"] and ["Y-coordinate"]
    :raises TypeError: if overall_gui_info and/or game_info is not a dictionary
                       if saved_coordinate is not a tuple
    """
    if type(overall_gui_info) is not dict or type(game_info) is not dict:
        raise TypeError("overall_gui_info and game_info must be dictionary")
    if type(saved_coordinate) is not tuple:
        raise TypeError("saved_coordinate must be a tuple.")
    toggle_battle_buttons(overall_gui_info, "disable")
    overall_gui_info['Script Frame'].children['enemy_info'].config(text=f"")
    overall_gui_info['Script Frame'].children['script_display'].config(
        text='Escaped the fight! Live to fight another day')
    game_info['character']["X-coordinate"] = saved_coordinate[0]
    game_info['character']["Y-coordinate"] = saved_coordinate[1]
    map_widget_update(game_info['character'], overall_gui_info)


def win_fight(overall_gui_info: dict, game_info: dict, progress_switch: dict) -> None:
    """
    Update the relevant buttons, player's info in terms of exp and levels,
    and enemy info after winning a flight with a foe.

    :param overall_gui_info: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param game_info: a dictionary that contains the information of character as value of a key called "character" and
                      the information of the game environment as value of a key called "environment"
    :param progress_switch: a dictionary that contains the event progress inside the current coordinate
    :precondition: overall_gui_info must be a dictionary
    :precondition: game_info must be a dictionary
    :precondition: progress_switch must be a dictionary
    :precondition: overall_gui_info must contain key named as ['Script Frame']
    :precondition: the value of ['Script Frame'] key must be a tkinter Frame
    :precondition: the tkinter Frame of overall_gui_info['Script Frame'] must contain a tkinter label named as
                   ['enemy_info']
    :precondition: progress_switch must contain keys named as ['opponent']
    :raises KeyError: if overall_gui_info does not contain key ['Script Frame']
                      if ['Script Frame'] does not have a widget named as ['enemy info']
                      if progress_switch does not contain keys ['opponent']
    :raises TypeError: if overall_gui_info, progress_switch and/or game_info is not a dictionary
    """
    if type(progress_switch) is not dict or type(overall_gui_info) is not dict or type(game_info) is not dict:
        raise TypeError("progress_switch, overall_gui_info and game_info must be dictionary")
    exp_calculator(overall_gui_info, game_info, progress_switch['opponent'])
    toggle_battle_buttons(overall_gui_info, "disable")
    overall_gui_info['Script Frame'].children['enemy_info'].config(text=f"")


def mid_boss_killed(progress_switch: dict, environment_info: dict, overall_gui_info: dict, location: tuple) -> None:
    """
    Update script, enemy info and map widgets upon winning a flight with a specific mid-progress boss.

    :param overall_gui_info: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param environment_info: a dictionary that contains the information of the game environment
    :param progress_switch: a dictionary that contains the event progress inside the current coordinate
    :param location: a tuple that represents the location of the midd-progress boss
    :precondition: overall_gui_info must be a dictionary
    :precondition: environment_info must be a dictionary
    :precondition: progress_switch must be a dictionary
    :precondition: location must be a tuple that represents the coordinate of the location
    :precondition: overall_gui_info must contain key named as ['Script Frame']
    :precondition: the value of ['Script Frame'] key must be a tkinter Frame
    :precondition: the tkinter Frame of overall_gui_info['Script Frame'] must contain a tkinter label named as
                   ['script display']
    :precondition: environment_info must contain keys of tuple of coordinates
    :precondition: the value of each key in environment_info should be a tuple of events inside that location
    :precondition: progress_switch must contain keys named as ['result'] and ['opponent']
    :precondition: the value of ['opponent'] must be a dictionary that contains key named as Name
    :raises KeyError: if overall_gui_info does not contain key ['Script Frame']
                      if ['Script Frame'] does not have a widget named as ['script display']
                      if progress_switch does not contain keys ['result'] and ['opponent']
                      if location does not exist in the key of environment_info
    :raises TypeError: if overall_gui_info, progress_switch and/or environment_info is not a dictionary
                       if location is not a tuple
    """
    if type(progress_switch) is not dict or type(overall_gui_info) is not dict or type(environment_info) is not dict:
        raise TypeError("progress_switch, overall_gui_info and environment_info must be dictionary")
    if type(location) is not tuple:
        raise TypeError("location must be a tuple.")
    if progress_switch['opponent']['Name'] == "Sage Thorne" and progress_switch['result'] == "win":
        overall_gui_info['Script Frame'].children['script_display'].config(
            text=f"Huh! Here you go, the Sanctum Key! ")
        environment_info[location] = ('Random', '')


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
