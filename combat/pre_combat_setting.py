from GUI import GAME_ENEMY_IMAGE_PATH
from GUI.create_widgets import update_image_label
from combat.combat_enemy import enemy_status


def toggle_battle_buttons(button_frame_views, action: str):
    if action not in ["enable", "disable"]:
        raise ValueError("action parameter must be 'enable' or 'disable'")
    movement_state = "normal"
    battle_state = "disabled"
    if action == "enable":
        movement_state = "disabled"
        battle_state = "normal"
        button_frame_views.unbind("<KeyPress>")
    disable_button = ['move_left', 'move_right', 'move_up', 'move_down', 'search']
    [button_frame_views.children[button].config(state=movement_state) for button in disable_button]
    enable_button = ['physical_attack', 'magic_attack', 'run']
    [button_frame_views.children[button].config(state=battle_state) for button in enable_button]


def update_enemy_info(overall_frames_info, enemy, script):
    overall_frames_info['Script Frame'].children['enemy_info'].config(text=f"{enemy_status(enemy)}")
    update_image_label(overall_frames_info['Script Frame'], "image_box", GAME_ENEMY_IMAGE_PATH.format(enemy['Name']))
    overall_frames_info['Script Frame'].children['script_display'].config(text=script)



