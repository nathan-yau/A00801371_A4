import random
from GUI import DEFAULT_FONT
from GUI_update.status_frame import update_status_message
from new_game.new_player import status_reset
from events.items_event import create_items_display


def level_up(overall_gui_frame, player_info):
    """

    """
    while player_info['NEXT LV (EXP)'] <= 0:
        player_info['Level'] += 1
        player_info['NEXT LV (EXP)'] += int(player_info['Level']*60*(random.uniform(1.5, 1.9)))
        for attribute in ["Strength", "Dexterity", "Intelligence", "Magic Power"]:
            player_info[attribute] += random.randint(5, 15)
        status_reset(player_info)
        overall_gui_frame['Status Frame'].children['character_status'].config(
            text=update_status_message(player_info, 4, -6))
        overall_gui_frame['Script Frame'].children['script_display'].config(
            text=f"Achieved Level {player_info['Level']}!")


def drop_item(gui_widgets_all, player_character, picked_foe):
    """

    """
    if random.randint(1,100) <= picked_foe['PROBABILITY']:
        item_bag = player_character['Items']
        item_bag[picked_foe['Items'][0]] = item_bag.get(picked_foe['Items'][0], 0) + 1
        create_items_display(gui_widgets_all['Item Frame'], player_character, gui_widgets_all)


def exp_calculator(gui_widgets_all, game_info, picked_foe):
    if random.randint(1, 20) == 1:
        EXP = int(picked_foe['EXP'] * 1.5)
        message = f'Wow! Defeating it granted you an unexpected surge of {EXP} experience points.'
    else:
        EXP = picked_foe['EXP']
        message = f'Gained {EXP} experience points by defeating {picked_foe["Name"]}'
    game_info['character']['NEXT LV (EXP)'] -= EXP
    gui_widgets_all['Script Frame'].children['script_display'].config(text=message, font=(DEFAULT_FONT, 8))
    gui_widgets_all['Status Frame'].children['character_status'].config(
        text=update_status_message(game_info['character'], 4, -6))
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