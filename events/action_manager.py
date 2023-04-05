from movement.move_checker import movement_check
from GUI_update.map_widget import map_widget_update
from combat.pre_combat_setting import toggle_battle_buttons, update_enemy_info
from events.event_checker import pick_available_foe, check_for_predetermined_events, encounter_confirmation
from combat.battle_events import activate_battle_button
from combat.pro_combat_setting import battle_end_widget_update
from functools import partial

from GUI_update.status_frame import update_status_message
from GUI import GAME_LOCATION_IMAGE_PATH
from GUI.create_widgets import update_image_label
import tkinter as tk


def gameplay(overall_gui_info, game_info, event):
    """

    :param overall_gui_info:
    :param game_info:
    :param event:
    """
    battle = [False]
    index = 0
    var = tk.BooleanVar()
    opponent = {}
    display = overall_gui_info['Script Frame'].children['script_display']
    pass_value = event if type(event) is str else event.keysym
    shortcut_list = ("a", "A", "d", "D", "w", "W", "s", "S")
    triggered_event = ""
    # If movement key is pressed
    if pass_value in shortcut_list and movement_check(game_info, shortcut_list.index(pass_value)//2 + 1):
        map_widget_update(game_info['character'], overall_gui_info)
        triggered_event = check_for_predetermined_events(game_info)

    # If battle event is confirmed
    if encounter_confirmation(triggered_event, game_info):
        display.config(text=triggered_event, image="")
        toggle_battle_buttons(overall_gui_info['Buttons Frame'], "enable")
        opponent = pick_available_foe(triggered_event, game_info['character']['Level'])
        update_enemy_info(overall_gui_info, opponent, f"Encountered {opponent['Name']}")
        battle = [opponent['HP'] > 0, game_info['character']['Current HP'] > 0]
        activate_battle_button(overall_gui_info, game_info, opponent, var)
        display.config(text=f"Round 1")
        var.set(False)

    # Battle round starts
    while False not in battle:
        index += 1
        overall_gui_info['Top Frame'].wait_variable(var)
        update_enemy_info(overall_gui_info, opponent, f"Round {index}\nTook the hit")
        overall_gui_info['Status Frame'].children['character_status'].config(text=update_status_message(game_info['character']))
        battle = [opponent['HP'] > 0, game_info['character']['Current HP'] > 0]
        if overall_gui_info['Event Bar'].cget("text")[0:3] == "Run":
            break

    if len(battle) > 1 and game_info['character']['Current HP'] <= 0:
        overall_gui_info['Script Frame'].children['script_display'].config(
                              text="Game Over!\nReload Save to continue!", compound="center", anchor="center")

    if len(battle) > 1 and game_info['character']['Current HP'] > 0:
        battle_end_widget_update(overall_gui_info, game_info, opponent)
        toggle_battle_buttons(overall_gui_info['Buttons Frame'], "disable")
        overall_gui_info['Buttons Frame'].bind("<KeyPress>", partial(gameplay, overall_gui_info, game_info))
        overall_gui_info['Script Frame'].children['enemy_info'].config(text=f"")
        update_image_label(overall_gui_info['Script Frame'], "image_box", GAME_LOCATION_IMAGE_PATH.format('Default'))

