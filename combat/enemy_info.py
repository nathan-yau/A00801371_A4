from GUI import GAME_ENEMY_IMAGE_PATH
from GUI.create_widgets import update_image_label


def enemy_status(player_info):
    character_status = "Enemy Information\n\n"
    keys_print = set(list(player_info.keys())[:3])
    for key, value in player_info.items():
        if key not in keys_print:
            continue
        character_status += f"{key:<6}{value:>12}\n"
    return character_status.rstrip()


def update_enemy_info(overall_frames_info, enemy, script):
    image_name = enemy['Name'].lower().replace(" ", "_")
    overall_frames_info['Script Frame'].children['enemy_info'].config(text=f"{enemy_status(enemy)}")
    update_image_label(overall_frames_info['Script Frame'], "image_box", GAME_ENEMY_IMAGE_PATH.format(image_name))
    overall_frames_info['Script Frame'].children['script_display'].config(text=script)
