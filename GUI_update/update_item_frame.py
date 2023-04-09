from GUI.create_widgets import create_image_label, create_text_label, create_click_button
from functools import partial
from GUI import GAME_ITEM_IMAGE_PATH
from events import items_event


def create_items_display(item_frame, player_data: dict, overall_gui: dict) -> None:
    """
    Create display of the player's items on an existing frame with buttons for using them.

    :param item_frame: an existing tkinter frame
    :param player_data: a dictionary that contains keys named as ["Items"]
    :param overall_gui: a dictionary that contain the description of the tkinter objects in string as keys
                        and their associated frame or widget objects as value
    :precondition: player_data must be a dictionary that contains the name of character's attributes as key
                   and their corresponding data as values
    :precondition: player_data must contain keys named as ["Items"]
    :precondition: overall_gui must be a dictionary that contain the description of the tkinter objects in string
                   as keys and their associated frame or widget objects as value
    :postcondition: create display of the player's items on an existing frame with buttons for using them
    :raises KeyError: if player_data does not contain ["Items"]
    :raises TypeError: if player_data is not a dictionary
                       if overall_gui is not a dictionary
    """
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
            item_frame.children[f"{button_name}_button"].config(command=partial(getattr(items_event, button_name),
                                                                                overall_gui, player_data))


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
