from GUI import GAME_ENEMY_IMAGE_PATH
from GUI.create_widgets import update_image_label


def enemy_status(enemy_info: dict) -> str:
    """
    Convert a dictionary that contains the "Name", "EXP", and "HP" of an enemy as keys and their corresponding
    values into an aligned string in multiple lines  with a title of "Enemy Information".

    :param enemy_info: a dictionary that contain the "Name", "EXP", and "HP" of an enemy as the first three keys
                        in this order and their corresponding data as values
    :precondition: enemy_info must be a dictionary that contain the "Name", "EXP", and "HP" of an enemy
                   as the first three keys and their corresponding data as values
    :precondition: enemy_info must contain keys named as "Name", "EXP" and "HP"
    :precondition: "Name", "EXP" and "HP" must be the first three keys of the enemy_info dictioary in this order
    :postcondition: convert a dictionary that contains the "Name", "EXP", and "HP" of an enemy as keys and
                    their corresponding values into an aligned string in multiple lines  with a title of
                    "Enemy Information"
    :return: an aligned string in multiple lines that contains the "Name", "EXP", and "HP" of an enemy with a title of
             "Enemy Information"
    :raise KeyError: if enemy_info does not contain keys named as "Name", "EXP", and "HP" as the first
                     three keys in this order
    :raise TypeError: if enemy_info is not a dictionary

    >>> character_dict = {"Name": "Nathan", "EXP": 100, "HP": 200, "MP": 404}
    >>> enemy_status(character_dict)


    >>> foe_dict = {"Name": "Nathan", "EXP": 100, "HP": 200}
    >>> enemy_status(foe_dict)
    'Enemy Information\\n\\nName        Nathan\\nEXP            100\\nHP             200'
    """
    if type(enemy_info) is not dict:
        raise TypeError("enemy_info must be a dictionary")
    if list(enemy_info.keys())[:3] != ['Name', 'EXP', 'HP']:
        raise KeyError("the first three keys of enemy_info must be 'Name', 'EXP', and 'HP' in this order")
    character_status = "Enemy Information\n\n"
    keys_print = set(list(enemy_info.keys())[:3])
    for key, value in enemy_info.items():
        if key not in keys_print:
            continue
        character_status += f"{key:<6}{value:>12}\n"
    return character_status.rstrip()


def update_enemy_info(overall_frames_info: dict, enemy: dict, script: str) -> None:
    """
    Update the enemy related widgets (image and text labels) on the GUI based on the
    enemy's information and given script string.

    :param overall_frames_info: a dictionary containing key named as ['Script Frame'],
                                whose value is a tkinter Frame
    :param enemy: a dictionary that contain the "Name", "EXP", and "HP" of an enemy as the first three keys
                    in this order and their corresponding data as values
    :param script: a string
    :precondition: overall_frames_info must be a dictionary containing key named as ['Script Frame'],
                   whose value is a tkinter Frame
    :precondition: the frame represented by the key ['Script Frame'] in overall_frames_info must contain two labels,
                   ['enemy_info'] and ['script_display']
    :precondition: enemy must be a dictionary that contain the "Name", "EXP", and "HP" of an enemy
                       as the first three keys and their corresponding data as values
    :precondition: enemy must contain keys named as "Name", "EXP" and "HP" as the first three keys in this order
    :precondition: script must be a string
    :postcondition: update the enemy related widgets (image and text labels) on the GUI based on the
                    enemy's information and given script string
    :raise KeyError: if enemy does not contain keys named as "Name", "EXP", and "HP" as the first
                     three keys in this order
                     if frame represented by the key ['Script Frame'] in overall_frames_info does not contain labels,
                     ['enemy_info'] and ['script_display']
    :raise TypeError: if overall_frames_info, enemy and/or script is not a dictionary
    """
    image_name = enemy['Name'].lower().replace(" ", "_")
    overall_frames_info['Script Frame'].children['enemy_info'].config(text=f"{enemy_status(enemy)}")
    update_image_label(overall_frames_info['Script Frame'], "image_box", GAME_ENEMY_IMAGE_PATH.format(image_name))
    overall_frames_info['Script Frame'].children['script_display'].config(text=script)
