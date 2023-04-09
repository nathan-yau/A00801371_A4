import random
import tkinter as tk
from GUI import DEFAULT_FONT
from GUI_update.status_frame import update_status_message
from new_game.new_player import status_reset
from events.items_event import create_items_display


def level_up(overall_gui_frame: dict, player_info: dict) -> None:
    """
    Reflect the player's new information on GUI after increasing the player's level and attributes
    if their experience points are high enough for next levels.

    :param overall_gui_frame: a dictionary containing key named as ['Script Frame'] whose value is a tkinter Frame
    :param player_info: a dictionary containing keys named as ['NEXT LV (EXP)'], ['Level'],
                        ["Strength"], ["Dexterity"], ["Intelligence"], ["Magic Resistance"] and ["Magic Power"],
                        each of which has an associated numeric value
    :precondition: overall_gui_frame must be a dictionary containing key named as ['Script Frame'],
                   each of which has an associated tkinter Frame
    :precondition: ['Script Frame'] key from overall_gui_frame must have an associated tkinter frame as value
    :precondition: ['Script Frame'] key from overall_gui_frame must contain labels named as ['character_status']
                   and ['script_display']
    :precondition: player_info must be a dictionary containing keys named as ['NEXT LV (EXP)'], ['Level'],
                   ["Strength"], ["Dexterity"], ["Intelligence"], ["Magic Resistance"] and ["Magic Power"]
    :precondition: ['NEXT LV (EXP)'], ['Level'], ["Strength"], ["Dexterity"], ["Intelligence"], ["Magic Resistance"]
                   and ["Magic Power"] keys from player_info must have an associated numeric value
    :postcondition: reflect the player's new information on GUI after increasing the player's level and attributes
                    if their experience points are high enough for next levels
    :raise KeyError: if the keys ['Script Frame'] cannot be found inside all_widgets_dict
                     if the keys ["Strength"], ["Dexterity"], ["Intelligence"], ["Magic Resistance"] and ["Magic Power"]
                     inside game_player_info cannot be found
    :raise TypeError: if the value of the keys ['Level'], ['NEXT LV (EXP)'], ["Strength"], ["Dexterity"],
                      ["Intelligence"], ["Magic Resistance"] and ["Magic Power"] inside foe is not number
                      if game_player_info is not a dictionary
    """
    while player_info['NEXT LV (EXP)'] <= 0:
        player_info['Level'] += 1
        player_info['NEXT LV (EXP)'] += int(player_info['Level']*60*(random.uniform(1.5, 1.9)))
        for attribute in ["Strength", "Dexterity", "Intelligence", "Magic Power", "Magic Resistance"]:
            player_info[attribute] += random.randint(5, 15)
        status_reset(player_info)
        level_up_widget_update(overall_gui_frame, player_info)


def level_up_widget_update(overall_gui_frame, player_info):
    """
    Update GUI to reflect the player's information upon level up.

    :param overall_gui_frame: a dictionary containing key named as ['Script Frame'] whose value is a tkinter Frame
    :param player_info: a dictionary containing keys named as ['Level'], which has an associated numeric value
    :precondition: overall_gui_frame must be a dictionary containing key named as ['Script Frame'],
                   each of which has an associated tkinter Frame
    :precondition: ['Script Frame'] key from overall_gui_frame must have an associated tkinter frame as value
    :precondition: ['Script Frame'] key from overall_gui_frame must contain labels named as ['character_status']
                   and ['script_display']
    :precondition: player_info must be a dictionary containing key named as ['Level']
    :postcondition: update GUI to reflect the player's information upon level up.
    """
    overall_gui_frame['Status Frame'].children['character_status'].config(
        text=update_status_message(player_info, 4, -7))
    overall_gui_frame['Script Frame'].children['script_display'].config(
        text=f"Achieved Level {player_info['Level']}!")


def drop_item(gui_widgets_all: dict, player_character: dict, picked_foe: dict) -> None:
    """
    Updates the GUI display if an item dropped from a foe's inventory to the player's bag
    based on a random probability assigned to the foe.

    :param gui_widgets_all: a dictionary containing key named as ['Item Frame'] whose value is a tkinter Frame
    :param player_character: a dictionary containing keys named as ["Items"], which has an associated dictionary
    :param picked_foe: a dictionary containing keys named as ['Items'] and ['Probability'], which has an
                       associated value of list and a positive non-zero integer less than or equal to 100
    :precondition: gui_widgets_all must be a dictionary containing key named as ['Item Frame'],
                   each of which has an associated tkinter Frame
    :precondition: ['Item Frame'] key from gui_widgets_all must have an associated tkinter frame as value
    :precondition: player_character must be a dictionary containing keys named as ['Items']
    :precondition: ['Items"] key from player_character must have a dictionary of name of item as keys and
                   integer number as its value
    :precondition: picked_foe must be a dictionary containing keys named as ['Items']
    :precondition: ['Items"] key from picked_foe must have a list as its value
    :precondition: ['Probability"] key from picked_foe must have an associated non-zero positive integer less than or
                   equal to 100 as its value.
    :postcondition: updates the GUI display if an item dropped from a foe's inventory to the player's bag
                    based on a random probability assigned to the foe
    :raise KeyError: if the keys ['Item Frame'] cannot be found inside gui_widgets_all
                     if the key ["Items"] cannot be found inside player_character
                     if the keys ['Items'] and ['Probability'] cannot be found inside picked_foe
    :raise TypeError: if gui_widgets_all, player_character and/or picked_foe is not a dictionary
                      if key ["Items"] from picked_foe is not a list
    :raise AttributeError: if key ["Items] from player_character is not a dictionary
    :raise ValueError:  if picked_foe['Probability'] is not a non-zero positive integer less than or
                        equal to 100
    """
    if type(picked_foe['Probability']) is not int or 0 >= picked_foe['Probability'] or 100 < picked_foe['Probability']:
        raise ValueError("Probability must be a non-zero positive integer less than or  equal to 100.")
    if random.randint(1, 100) <= picked_foe['Probability']:
        item_bag = player_character['Items']
        item_bag[picked_foe['Items'][0]] = item_bag.get(picked_foe['Items'][0], 0) + 1
        create_items_display(gui_widgets_all['Item Frame'], player_character, gui_widgets_all)


def exp_calculator(gui_widgets_all, game_info, picked_foe):
    """
    Display the experience point gained from the defeated foe and the updated EXP point of the player on GUI

    :param gui_widgets_all: a dictionary containing key named as ['Item Frame'] whose value is a tkinter Frame
    :param game_info: a dictionary that contains the information of character as value of a key called "character"
    :param picked_foe: a dictionary containing keys named as ['Name'] and ['EXP'], which has an
                       associated value of string and an integer
    :precondition: gui_widgets_all must be a dictionary containing key named as ['Script Frame'],
                   each of which has an associated tkinter Frame
    :precondition: ['Script Frame'] key from gui_widgets_all must have an associated tkinter frame as value
    :precondition: the frame represented by gui_widgets_all['Script Frame'] must contain ['character_status'] and
                   ['script_display']
    :precondition: player_character must be a dictionary containing keys named as ['character']
    :precondition: ['character"] key from player_character must be a dictionary that contains ['NEXT LV (EXP)'] as key
                   and an integer as value
    :precondition: picked_foe must be a dictionary containing keys named as ['EXP'] and ['Name']
    :precondition: ['EXP'] key from picked_foe must be an integer
    :precondition: ['Name'] key from picked_foe must be a string
    :postcondition: display the experience point gained from the defeated foe and
                    the updated EXP point of the player on GUI
    :raise KeyError: if the keys ['Script Frame'] cannot be found inside gui_widgets_all
                     if the key ["character"] cannot be found inside player_character
                     if the key ['NEXT LV (EXP)'] cannot be found inside player_character["character"]
                     if the keys ['EXP'] and ['Name'] cannot be found inside picked_foe
    :raise TypeError: if gui_widgets_all, player_character and/or picked_foe is not a dictionary
                      if key ["EXP"] from picked_foe is not an integer
                      if key ["character"] inside player_character is not a dictionary
                      if key ['NEXT LV (EXP)'] inside player_character["character"] is not an integer
    """
    if random.randint(1, 20) == 1:
        EXP = int(picked_foe['EXP'] * 1.5)
        message = f'Wow! Defeating it granted you an unexpected surge of {EXP} experience points.'
    else:
        EXP = picked_foe['EXP']
        message = f'Gained {EXP} experience points by defeating {picked_foe["Name"]}'
    game_info['character']['NEXT LV (EXP)'] -= EXP
    gui_widgets_all['Script Frame'].children['script_display'].config(text=message, font=(DEFAULT_FONT, 8))
    gui_widgets_all['Status Frame'].children['character_status'].config(
        text=update_status_message(game_info['character'], 4, -7))
    level_up(gui_widgets_all, game_info['character'])


def check_if_alive(gui_dict, player_info):
    """
    Disable buttons on GUI if player's HP is less than or equal to 0.

    :param player_info: a dictionary that contains a key named as "Current HP" and its corresponding value is an integer
    :param gui_dict: a dictionary that contain the description of the tkinter objects in string as key and
                     their associated frame or widget objects as value
    :precondition: a tkinter root window must exist
    :precondition: player_info must be a dictionary with a key named as "Current HP"
    :precondition: player_info must be a dictionary with an integer value associated with the key "Current HP"
    :precondition: gui_dict must be a dictionary that contain the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: gui_dict must contain two keys named as "Buttons Frame" and "Side Bar Frame"
    :precondition: the value of the key "Buttons Frame" in interface_frame dictionary must be an existing frame
    :precondition: the value of the key "Side Bar Frame" in interface_frame dictionary must be an existing frame
    :postcondition: check if the heath points of player is less than or equal to 0
    :raise KeyError: if player_info does not have a key named as "Current HP"
                     if gui_dict does not have keys named as "Buttons Frame" and "Side Bar Frame"
                     if "items" and "save" do not exist in the sider bar frame indicated by gui_dict
    """
    if player_info['Current HP'] <= 0:
        button_frame_widgets = gui_dict['Buttons Frame'].winfo_children()
        [widget.config(state="disabled") for widget in button_frame_widgets if isinstance(widget, tk.Button)]
        gui_dict['Side Bar Frame'].children['items'].config(state="disabled")
        gui_dict['Side Bar Frame'].children['save'].config(state="disabled")
        gui_dict['pause'].set(False)
