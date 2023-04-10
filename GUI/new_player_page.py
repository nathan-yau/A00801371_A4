from functools import partial

from GUI import GAME_BANNER, PLAYER_ICON_IMAGE_PATH
from new_game.new_player import create_character
from GUI.create_widgets import create_click_button, create_text_label, create_image_label, attach_button_function_call
from save_load.load_game_file import load_file
from utilities.initialize_game import load_into_game
import pathlib


def create_new_player_page(name: str, interface_frames: dict) -> None:
    """
    Recreate a frame located at the top of the GUI with new label and buttons to show the character's attribute
    for player's selection.

    :param name: a string that represents the character name of the current player
    :param interface_frames: a dictionary that contain the description of the tkinter objects in string as key and
                             their associated frame or widget objects as value
    :precondition: a tkinter root window must exist
    :precondition: interface_frame must be a dictionary that contain the description of the tkinter objects in
                             string as key and their associated frame or widget objects as value
    :precondition: interface_frame must contain two keys named as 'Event Bar' and 'Top Frame'
    :precondition: the value of the key "Event Bar" in interface_frame dictionary must be an existing text label widget
    :precondition: the value of the key "Top Frame" in interface_frame dictionary must be an existing frame
    :postcondition: reuse an existing frame located at the top of the GUI with new label and buttons to show the
                    character's attribute for player's selection.
    :raises TypeError: if interface_frames is not a dictionary
                      if name is not a string
    :raises KeyError: if interface_frames does not contain "Event Bar" and/or "Top Frame" as keys
    :raises AttributeError: if the value of the key "Event Bar" in interface_frame is not an existing text label widget
                           if the value of the key "Top Frame" in interface_frame is not an existing frame
    """
    def create_banner() -> None:
        """
        Create an image label at the top of the GUI as a game banner

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame used in create_image_label() must be a tkinter frame in the tkinter root window
        :precondition: widget name used in create_image_label() must not currently exist in the specific frame
        :precondition: GAME_BANNER must be defined
        :precondition: GAME_BANNER must represent an existing picture in size of 820 x 160 pixels
        :postcondition: create a label containing a banner that takes 5 columns of the GUI
        :raises _tkinter.TclError: if the image represented by image_directory does not exist
                                  if the image_directory does not represent an image
        :raises KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        :raises NameError: if GAME_BANNER are not defined
        :raises FileNotFoundError: if GAME_BANNER image cannot be found in the given path
        """
        if pathlib.Path(GAME_BANNER).is_file():
            create_image_label(frame=main_frame, widget_name="banner", image_path=GAME_BANNER)
        else:
            raise FileNotFoundError("Banner image cannot be found! Please check the path!")
        main_frame.children['banner'].grid(row=0, column=0, columnspan=5, sticky="nsew")

    def create_player_image() -> None:
        """
        Create an image label at the top of the GUI as a player icon

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame used in create_image_label() must be a tkinter frame in the tkinter root window
        :precondition: widget name used in create_image_label() must not currently exist in the specific frame
        :precondition: PLAYER_ICON_IMAGE_PATH must exist in __init__.py under GUI package
        :precondition: PLAYER_ICON_IMAGE_PATH must represent an existing picture in size of 205 x 300 pixels
        :postcondition: create a label containing a player icon that takes 4 rows of the GUI
        :raises _tkinter.TclError: if the image represented by image_directory does not exist
                                  if the image_directory does not represent an image
        :raises KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        :raises NameError: if PLAYER_ICON_IMAGE_PATH are not defined in __init__.py under GUI package
        """
        if pathlib.Path(GAME_BANNER).is_file():
            create_image_label(frame=main_frame, widget_name="player_icon", image_path=PLAYER_ICON_IMAGE_PATH)
        else:
            raise FileNotFoundError("Player icon image cannot be found! Please check the path!")
        main_frame.children['player_icon'].grid(row=1, column=0, rowspan=4, ipady=40)

    def generate_attribute_text(random_attribute: dict, start_skip: int, end_skip: int) -> str:
        """
        Convert a dictionary that contains the name of a player's attributes as key and their corresponding value into
        an aligned string in multiples lines.

        :param random_attribute: a dictionary that generated by create_character(), which produces a dictionary
                                 that contain the name of character's attributes as key and their corresponding values
        :param start_skip: an integer indicating the starting index of the attributes to skip in the list of attributes
        :param end_skip: an integer indicating the ending index of the attributes to skip in the list of attributes
        :precondition: random_attribute must be a dictionary that generated by create_character()
        :precondition: the length of the keys in random_attribute must be at least 16 characters
        :precondition: the length of the values in random_attribute must be no more than 10 characters
        :postcondition: returns an aligned string that contains the attributes and their corresponding values from the
                        random_attribute, excluding the attributes with indexes between start_skip and end_skip
        :return: an aligned string that contains the attributes and their corresponding values from the
                 random_attribute, excluding the attributes with indexes between start_skip and end_skip
        :raises AttributeError: if random_attribute is not a dictionary
        :raises TypeError: if start_skip and/or end_skip is not an integer
        """
        display_message = ""
        for key, value in random_attribute.items():
            if key not in list(random_attribute.keys())[start_skip:end_skip]:
                display_message += f"{str(key): <16}{str(value): >18}\n"
        return display_message

    def create_attribute_label() -> None:
        """
        Create an empty text label as a placeholder for displaying attributes for the new player at the top of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame used in create_text_label() must be a tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create an empty text label as a placeholder for displaying attributes
                        for the new player at the top of the GUI
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=main_frame, text_label_name="attribute_label",
                          message="", font_size=20, justify="left")
        main_frame.children['attribute_label'].grid(row=1, column=1, rowspan=4)

    def display_attribute() -> dict:
        """
        Update the attribute_label with randomly generated attributes for the new player to accept
        at the top of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame used in create_text_label() must be a tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: update some random generated attributes for the new player on the GUI as a label widget
        :return: a dictionary that contains generated attributes for the new player with string as key
        :raises KeyError: if the label used for configuration does not exist in the specific frame
        :raises TypeError: if name is not a string
        """
        generated_attributes = create_character(name=name)
        display_message = generate_attribute_text(random_attribute=generated_attributes, start_skip=2, end_skip=-7)
        main_frame.children['attribute_label'].config(text=f"{name}'s Attribute:\n\n{display_message}")
        return generated_attributes

    def create_attribute_buttons(character_attribute: dict) -> None:
        """
        Create regenerate, accept and cancel buttons for user to interact with the randomly generated attributes.

        :param character_attribute: a dictionary that contains generated attributes for the new player
                                    with string as key
        :precondition: character_attribute must be a dictionary that contains generated attributes for the new player
                       with string as key
        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_click_button() must not currently exist in the specific frame
        :postcondition: create regenerate, accept and cancel buttons for user to interact
                        with the randomly generated attributes
        :raises KeyError: if the proposed widget names used in this function already exist in the specific frame
        """

        new_player_button = {'Regenerate': display_attribute,
                             'Accept': partial(load_into_game, interface_frames, character_attribute),
                             'Load Save': partial(load_file, interface_frames)}
        for index, (key, value) in enumerate(new_player_button.items()):
            button_name = key.lower().replace(" ", "_")
            create_click_button(belonging_frame=main_frame, widget_name_id=button_name, message=key, button_width=10)
            attach_button_function_call(button_name=main_frame.children[button_name],
                                        callable_function=value)
            main_frame.children[button_name].grid(row=index + 1, column=3, sticky='e', ipady=20, pady=30, padx=(50, 0))

    main_frame = interface_frames['Top Frame']
    [widget.destroy() for widget in main_frame.winfo_children()]

    frame_level_list = (create_player_image, create_banner, create_attribute_label)
    [image_label() for image_label in frame_level_list]

    interface_frames['Event Bar'].config(text="Creating New User - " + name)
    create_attribute_buttons(display_attribute())


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
