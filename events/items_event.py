from GUI.create_widgets import create_image_label,create_text_label,create_click_button
from GUI import GAME_ITEM_IMAGE_PATH
from functools import partial
from GUI_update.status_frame import update_status_message
import random


def healing_potion(overall_gui_frame, player_info):
    restore_point = min(player_info['Max HP']-player_info['Current HP'], 10)
    if player_info['Current HP'] < player_info['Max HP']:
        player_info['Current HP'] += restore_point
        overall_gui_frame['Status Frame'].children['character_status'].config(
            text=update_status_message(player_info, 4, -7))
        overall_gui_frame['Event Bar'].config(text=f'HP restored by {restore_point} Points!')
        player_info['Items']['Healing Potion'] -= 1
        if player_info['Items']['Healing Potion'] <= 0:
            player_info['Items'].pop('Healing Potion')
        create_items_display(overall_gui_frame['Item Frame'], player_info, overall_gui_frame)
    else:
        overall_gui_frame['Event Bar'].config(text=f'Healing Potion cannot be used now!')


def status_potion(overall_gui_frame, player_info):
    if player_info['Status'] != "Healthy":
        player_info['Status'] = "Healthy"
        overall_gui_frame['Status Frame'].children['character_status'].config(
            text=update_status_message(player_info, 4, -7))
        overall_gui_frame['Event Bar'].config(text=f'{player_info["Name"]} is healthy again!')
        player_info['Items']['Status Potion'] -= 1
        if player_info['Items']['Status Potion'] <= 0:
            player_info['Items'].pop('Status Potion')
        create_items_display(overall_gui_frame['Item Frame'], player_info, overall_gui_frame)
    else:
        overall_gui_frame['Event Bar'].config(text=f'Status Potion cannot be used now!')


def attribute_potion(overall_gui_frame, player_info):
    increase_point = random.randint(5, 20)
    attribute = random.sample(list(player_info.keys())[-4:], 1)[0]
    player_info[attribute] += increase_point
    overall_gui_frame['Status Frame'].children['character_status'].config(
        text=update_status_message(player_info, 4, -7))
    overall_gui_frame['Event Bar'].config(text=f'{attribute} increased by {increase_point} Points!')
    player_info['Items']['Attribute Potion'] -= 1
    if player_info['Items']['Attribute Potion'] <= 0:
        player_info['Items'].pop('Attribute Potion')
    create_items_display(overall_gui_frame['Item Frame'], player_info, overall_gui_frame)


def create_items_display(item_frame, player_data, overall_gui):
    [widget.destroy() for widget in item_frame.winfo_children()]
    for index, (key, value) in enumerate(player_data["Items"].items()):
        button_name = key.lower().replace(" ", "_")
        item_frame.grid_rowconfigure(index, weight=1)
        create_image_label(frame=item_frame, widget_name=f"{button_name}_image",
                           image_path=GAME_ITEM_IMAGE_PATH.format(button_name))
        item_frame.children[f"{button_name}_image"].grid(row=index, column=0, sticky='e', padx=(25, 0))
        create_text_label(frame_obj=item_frame, text_label_name=f"{button_name}_label", message=f"{key} x {value}",
                          font_size=8)
        item_frame.children[f"{button_name}_label"].grid(row=index, column=1, sticky='nsew', padx=(25, 0))
        if key not in ["Sanctum Key", "The Amulet of Knowledge", "Oasis Explorer"]:
            create_click_button(belonging_frame=item_frame, widget_name_id=f"{button_name}_button", message="USE")
            item_frame.children[f"{button_name}_button"].grid(row=index, column=2, sticky='e', padx=(25, 0), ipadx=20)
            item_frame.children[f"{button_name}_button"].config(command=partial(eval(button_name), overall_gui, player_data))


def search(overall_widgets, game_info):
    current_coordinate = (game_info['character']["X-coordinate"], game_info['character']["Y-coordinate"])
    searched_item = game_info['environment'][current_coordinate][1]
    item_bag = game_info['character']['Items']
    if searched_item and game_info['environment'][current_coordinate][0] == "ITEM":
        message = f"Congratulations adventurer! \nyou have discovered a {searched_item} in the vast!"
        item_bag[searched_item] = item_bag.get(searched_item, 0) + 1
        game_info['environment'][current_coordinate] = ("RANDOM", "")
        create_items_display(overall_widgets['Item Frame'], game_info['character'], overall_widgets)
    else:
        message = f"Nothing here!"
    overall_widgets['Script Frame'].children['script_display'].config(text=message)
