from events.movement import player_movement, default_script_for_location
from events.event_checker import pick_available_foe, check_for_predetermined_events
from events.game_ending import game_over, goal_achieve, easter_egg

from combat.enemy_info import update_enemy_info
from combat.combat_widget import activate_battle_button, toggle_battle_buttons
from combat.player_info import drop_item
from combat.combat_result import escape_from_fight, win_fight, mid_boss_killed

from GUI import GAME_LOCATION_IMAGE_PATH
from GUI.create_widgets import update_image_label

from GUI_update.update_map_widget import map_widget_update
from GUI_update.update_status_frame import update_status_message

import os
from functools import partial


def game(overall_gui_info, game_info, event):
    """
    Drive the game flow.
    """
    battle_round = 0
    saved_coordinate = (game_info['character']["X-coordinate"], game_info['character']["Y-coordinate"])
    progress_switch = {"move": '', "event": False, "opponent": False, "battle": False, "result": False}
    pass_value = event if type(event) is str else event.keysym
    shortcut_list = ("a", "A", "d", "D", "w", "W", "s", "S")

    if pass_value in shortcut_list:
        if player_movement(game_info, shortcut_list.index(pass_value) // 2 + 1, overall_gui_info):
            map_widget_update(game_info['character'], overall_gui_info)
            triggered_event = check_for_predetermined_events(game_info)
            progress_switch['move'] = (game_info['character']["X-coordinate"], game_info['character']["Y-coordinate"])
            progress_switch['event'] = triggered_event
            progress_switch['opponent'] = pick_available_foe(triggered_event, game_info)
            default_script_for_location(game_info['character'], overall_gui_info)
        else:
            overall_gui_info['Event Bar'].config(text="Invalid Move!")

    if progress_switch['opponent']:
        update_enemy_info(overall_gui_info, progress_switch['opponent'],
                          f"Encountered {progress_switch['opponent']['Name']}")
        progress_switch['battle'] = True

    if progress_switch['battle']:
        toggle_battle_buttons(overall_gui_info, "enable")
        activate_battle_button(overall_gui_info, game_info['character'], progress_switch['opponent'])
        overall_gui_info['Script Frame'].children['script_display'].config(text=f"Round 1")
        overall_gui_info['pause'].set(True)

    while progress_switch['battle']:
        battle_round += 1
        overall_gui_info['GUI'].wait_variable(overall_gui_info['pause'])
        update_enemy_info(overall_gui_info, progress_switch['opponent'], f"Round {battle_round}\nTook the hit")
        overall_gui_info['Status Frame'].children['character_status'].config(
            text=update_status_message(game_info['character'], 4, -7))
        if progress_switch['opponent']['HP'] <= 0 or \
                game_info['character']['Current HP'] <= 0 or game_info['character']['Escape']:
            progress_switch['battle'] = False

    if progress_switch['opponent'] and game_info['character']['Current HP'] <= 0:
        game_over(overall_gui_info)

    if progress_switch['opponent'] and game_info['character']['Current HP'] > 0:
        overall_gui_info['Buttons Frame'].bind("<KeyPress>", partial(game, overall_gui_info, game_info))

    if progress_switch['opponent'] and progress_switch['opponent']['HP'] <= 0 < game_info['character']['Current HP']:
        win_fight(overall_gui_info, game_info, progress_switch)
        drop_item(overall_gui_info, game_info['character'], progress_switch['opponent'])
        progress_switch['result'] = "win"

    if progress_switch['opponent'] and game_info['character']['Escape']:
        escape_from_fight(overall_gui_info, game_info, saved_coordinate)
        progress_switch['result'] = "run"

    if progress_switch['move']:
        game_info['character']['Escape'] = False
        image_file = 'Default'
        if os.path.exists(GAME_LOCATION_IMAGE_PATH.format(progress_switch['move'])):
            image_file = str(progress_switch['move'])
        update_image_label(overall_gui_info['Script Frame'], "image_box", GAME_LOCATION_IMAGE_PATH.format(image_file))

    if progress_switch['opponent']:
        mid_boss_killed(progress_switch, game_info['environment'], overall_gui_info, (4, 2))
        goal_achieve(progress_switch, game_info['environment'], overall_gui_info)

    if progress_switch['move'] == (0, 4):
        easter_egg(overall_gui_info)


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
