from GUI_update.update_status_frame import update_status_message
from GUI_update.update_item_frame import create_items_display
import random


def search(overall_widgets: dict, game_info: dict) -> None:
    """
    Search the current coordinate for any predetermined items.

    :param overall_widgets: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param game_info: a dictionary that contains the information of character as value of a key called "character" and
                      the information of the game environment as value of a key called "environment"
    :precondition: overall_gui_info must be a dictionary
    :precondition: game_info must be a dictionary
    :precondition: overall_gui_info must contain key named as ['Script Frame'] and ['Item Frame']
    :precondition: the value of ['Script Frame'] and ['Item Frame'] key must be a tkinter Frame
    :precondition: the tkinter Frame of overall_gui_info['Script Frame'] must contain a tkinter label named as
                   ['script display']
    :precondition: game_info must contain keys named as ['character'] and ['environment']
    :precondition: the value of ['character'] inside game_info must contain keys ["X-coordinate"], ['Items']
                   and ["Y-coordinate"]
    :precondition: the value of ['environment'] inside game_info must contain keys that is a tuple of coordinate (x, y)
                   and their predetermined events as a tuple associated with the coordinate keys
    :postcondition: search the current coordinate for any predetermined items
    :raises KeyError: if overall_gui_info does not contain key ['Script Frame'] and ['Item Frame']
                      if ['Script Frame'] does not have a widget named as ['script display']
                      if game_info does not contain key ['character'] and ['environment']
                      if ['character'] inside game_info must contain keys ["X-coordinate"], ['Items']
                      and ["Y-coordinate"]
    """
    current_coordinate = (game_info['character']["X-coordinate"], game_info['character']["Y-coordinate"])
    searched_item = game_info['environment'][current_coordinate][1]
    item_bag = game_info['character']['Items']
    if searched_item and game_info['environment'][current_coordinate][0] == "ITEM":
        message = f"Congratulations adventurer! \nyou have discovered a {searched_item} in the vast!"
        item_bag[searched_item] = item_bag.get(searched_item, 0) + 1
        game_info['environment'][current_coordinate] = ("Random", "")
        create_items_display(overall_widgets['Item Frame'], game_info['character'], overall_widgets)
    else:
        message = f"Nothing here!"
    overall_widgets['Script Frame'].children['script_display'].config(text=message)


def healing_potion(overall_gui_frame: dict, player_info: dict) -> None:
    """
    Update the player's info in terms of the effects of healing potion on HP and the display on item frame.


    :param overall_gui_frame: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param player_info: a dictionary that contains the name of a player's attributes as key and their
                        corresponding value
    :precondition: overall_gui_info must be a dictionary
    :precondition: player_info must be a dictionary that contains the name of a player's attributes as key and their
                   corresponding value
    :precondition: player_info must contain keys named as "Max HP", "Current HP", "Items"
    :precondition: overall_gui_info must contain key named as ['Script Frame'], ['Event Bar'], and ['Item Frame']
    :precondition: the value of ['Status Frame'] and ['Item Frame'] key must be a tkinter Frame
    :precondition: the value of ['Event Bar'] key must be a tkinter Text Label
    :precondition: the tkinter Frame of overall_gui_frame['Status Frame'] must contain a tkinter label named as
                   ['character_status']
    :postcondition: update the player's info in terms of the effects of healing potion on HP and the
                    display on item frame
    :raises KeyError: if overall_gui_info does not contain key['Script Frame'], ['Event Bar'], and ['Item Frame']
                      if ['Status Frame'] does not have a widget named as ['character_status']
                      if player_info does not contain key "Max HP", "Current HP", "Items"
    """
    restore_point = min(player_info['Max HP']-player_info['Current HP'], 50)
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


def status_potion(overall_gui_frame: dict, player_info: dict) -> None:
    """
    Update the player's info in terms of the effects of status potion on status and the display on item frame.


    :param overall_gui_frame: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param player_info: a dictionary that contains the name of a player's attributes as key and their
                        corresponding value
    :precondition: overall_gui_info must be a dictionary
    :precondition: player_info must be a dictionary that contains the name of a player's attributes as key and their
                   corresponding value
    :precondition: player_info must contain keys named as "Status" and "Items"
    :precondition: overall_gui_info must contain key named as ['Script Frame'], ['Event Bar'], and ['Item Frame']
    :precondition: the value of ['Status Frame'] and ['Item Frame'] key must be a tkinter Frame
    :precondition: the value of ['Event Bar'] key must be a tkinter Text Label
    :precondition: the tkinter Frame of overall_gui_frame['Status Frame'] must contain a tkinter label named as
                   ['character_status']
    :postcondition: update the player's info in terms of the effects of status potion on status and the
                    display on item frame.
    :raises KeyError: if overall_gui_info does not contain key['Script Frame'], ['Event Bar'], and ['Item Frame']
                      if ['Status Frame'] does not have a widget named as ['character_status']
                      if player_info does not contain key "Status", "Items"
    """
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


def attribute_potion(overall_gui_frame: dict, player_info: dict) -> None:
    """
    Update the player's info in terms of the effects of attribute potion on the character's attribute
    and the display on item frame.

    :param overall_gui_frame: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param player_info: a dictionary that contains the name of a player's attributes as key and their
                        corresponding value
    :precondition: overall_gui_info must be a dictionary
    :precondition: player_info must be a dictionary that contains the name of a player's attributes as key and their
                   corresponding value
    :precondition: player_info must contain keys named as "Status" and "Items"
    :precondition: overall_gui_info must contain key named as ['Script Frame'], ['Event Bar'], and ['Item Frame']
    :precondition: the value of ['Status Frame'] and ['Item Frame'] key must be a tkinter Frame
    :precondition: the value of ['Event Bar'] key must be a tkinter Text Label
    :precondition: the tkinter Frame of overall_gui_frame['Status Frame'] must contain a tkinter label named as
                   ['character_status']
    :postcondition: update the player's info in terms of the effects of attribute potion on the character's attribute
                    and the display on item frame.
    :raises KeyError: if overall_gui_info does not contain key['Script Frame'], ['Event Bar'], and ['Item Frame']
                      if ['Status Frame'] does not have a widget named as ['character_status']
                      if player_info does not contain key "Items"
    """
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


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
