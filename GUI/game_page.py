import tkinter as tk
from functools import partial
import pathlib

from GUI.create_widgets import create_click_button, create_text_label, create_image_label, attach_button_function_call
from GUI import GAME_MAP_PATH, GAME_LOCATION_IMAGE_PATH
from utilities.closing_window import closing_event
from events.gameplay import game

from save_load.save_game_file import create_save_file
from GUI_update.update_status_frame import update_status_message
from events.items_event import search, create_items_display


def create_status_frame(overall_game_frame: dict, player_data: dict) -> tk.Frame:
    """
    Create a frame on the left side of the GUI to display character's status and map based on their location.

    :param overall_game_frame: a dictionary that contain the description of the tkinter objects in string as keys and
                               their associated frame or widget objects as value
    :param player_data: a dictionary that contains the description of the character's attributes as key and
                        its corresponding data as values
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_game_frame must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_game_frame must contain a key named as 'Top Frame'
    :precondition: the value of the key "Top Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :precondition: player_data must be a dictionary that contains the description of the character's attributes as
                   key and its corresponding data as values
    :precondition: player_data must contain keys named as "Name", "X-coordinate" and "Y-coordinate"
    :postcondition: create a tkinter Frame that contains status and map widgets on the top of the GUI window
    :raises TypeError: if interface_frames is not a dictionary
                       if player_data is not a dictionary
    :raises KeyError: if interface_frames does not contain "Top Frame" as key
                      if player_data does not contain "Name", "X-coordinate" and "Y-coordinate" as key
    :raises AttributeError: if the value of the key "Top Frame" in interface_frame is not an existing tkinter frame
    :return: a tkinter Frame that contains status and map widgets on the top of the GUI window
    """
    def left_frame_grid_setting() -> None:
        """
        Set up the grid in terms of column and row weights for a frame located on the left side of the GUI.

        :postcondition: set up the grid in terms of column and row weights for a frame located on the
                        left side of the GUI.
        """
        left_frame.grid(column=0, row=0, rowspan=2, sticky='nsw')
        left_frame.grid_columnconfigure(0, weight=1)
        for row, weight in enumerate([0, 0, 0, 1]):
            left_frame.grid_rowconfigure(row, weight=weight)

    def create_character_status_widget() -> None:
        """
        Create text labels for displaying character's status on the left side frame of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :precondition: player_data must be a dictionary that contains the description of the character's attributes as
                       key and its corresponding data as values
        :precondition: player_data must contain keys named as "Name"
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
                         if player_data does not contain "Name" as key
        """
        create_text_label(frame_obj=left_frame, text_label_name="status_label",
                          message=f"{player_data['Name']}'s Status", font_size=12, pady=5, relief="groove",
                          bg="#E89F71")
        left_frame.children['status_label'].grid(row=2, sticky='nsew')

        create_text_label(frame_obj=left_frame, text_label_name="character_status", font_size=15,
                          message=update_status_message(player_data, 4, -7), anchor="sw", justify="left")
        left_frame.children['character_status'].grid(row=3, sticky='n')

    def create_map_widget() -> None:
        """
        Create image label for displaying the game map on the left side frame of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used must not currently exist in the specific frame
        :precondition: player_data must be a dictionary that contains the description of the character's attributes as
                       key and its corresponding data as values
        :precondition: player_data must contain keys named as "X-coordinate" and "Y-coordinate"
        :postcondition: create image label for displaying the game map on the left side frame of the GUI
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                          if the widget name cannot be found in the specific frame after creation
                          if player_data does not contain "X-coordinate" and "Y-coordinate" as keys
        :raises FileNotFoundError: if game map image cannot be found
        """
        coordinate = str(player_data["X-coordinate"]) + str(player_data["Y-coordinate"])
        create_text_label(frame_obj=left_frame, text_label_name="map_label", message=f"Current Oasis Map",
                          pady=5, relief="groove", bg="#E89F71", font_size=12)
        left_frame.children['map_label'].grid(row=0, sticky='new')
        if pathlib.Path(GAME_MAP_PATH.format(coordinate)).is_file():
            create_image_label(frame=left_frame, widget_name="current_map", image_path=GAME_MAP_PATH.format(coordinate))
        else:
            raise FileNotFoundError("Game map image cannot be found! Please check the path!")
        left_frame.children['current_map'].grid(row=1, sticky='nsew')

    left_frame = tk.Frame(overall_game_frame['Top Frame'], bd=1, relief='sunken', padx=0, pady=0)
    left_frame_list = (left_frame_grid_setting, create_character_status_widget, create_map_widget)
    [left_widget() for left_widget in left_frame_list]
    return left_frame


def create_script_frame(overall_interface_frame: dict) -> tk.Frame:
    """
    Create a frame in the middle of the GUI to display game script based on the player's location and events.

    :param overall_interface_frame: a dictionary that contain the description of the tkinter objects in string as keys
                                    and their associated frame or widget objects as value
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_interface_frame must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_interface_frame must contain a key named as 'Top Frame'
    :precondition: the value of the key "Top Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :postcondition: create a tkinter Frame that contains a game script in the middle of the GUI window
    :raises TypeError: if interface_frames is not a dictionary
    :raises KeyError: if interface_frames does not contain "Top Frame" as key
    :raises AttributeError: if the value of the key "Top Frame" in interface_frame is not an existing tkinter frame
    :return: a tkinter Frame that contains game script widgets in the middle of the GUI window
    """

    def create_middle_grid() -> None:
        """
        Set up the grid in terms of column and row weights for a frame located in the middle side of the GUI.

        :postcondition: set up the grid in terms of column and row weights for a frame located ine the
                        middle of the GUI.
        """
        middle_top_frame.grid(column=1, row=0, sticky='nsew')
        weight_tuple = ((3, 0), (0, 1))
        for index, weight in enumerate(weight_tuple):
            middle_top_frame.grid_columnconfigure(index, weight=weight[0])
            middle_top_frame.grid_rowconfigure(index, weight=weight[1])

    def create_picture_display_frame() -> None:
        """
        Create image label for displaying the location or event image in the middle frame of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_image_label() must not currently exist in the specific frame
        :postcondition: create image label for displaying the location or event image in the middle frame of the GUI
        :raises KeyError: if the proposed widget name already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_image_label(frame=middle_top_frame, widget_name="image_box",
                           image_path=GAME_LOCATION_IMAGE_PATH.format("default"))
        middle_top_frame.children['image_box'].grid(row=0, column=1, sticky='nswe')

    def create_enemy_info_display_frame() -> None:
        """
        Create text label for displaying the status of enemy in the middle frame of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_image_label() must not currently exist in the specific frame
        :postcondition: create image label for displaying the location or event image in the middle frame of the GUI
        :raises KeyError: if the proposed widget name already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=middle_top_frame, text_label_name="enemy_info", message=f"",
                          relief="groove", justify="left")
        middle_top_frame.children['enemy_info'].grid(row=0, column=0, sticky='nswe')

    def create_script_display_frame() -> None:
        """
        Create text label for displaying the game plot in the middle frame of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_image_label() must not currently exist in the specific frame
        :postcondition: create image label for displaying the location or event image in the middle frame of the GUI
        :raises KeyError: if the proposed widget name already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=middle_top_frame, text_label_name="script_display", message=f"Welcome to Oasis",
                          pady=10, relief="groove")
        middle_top_frame.children['script_display'].grid(row=1, column=0, columnspan=2, sticky='nswe')

    middle_top_frame = tk.Frame(overall_interface_frame['Top Frame'], bd=1, relief='groove')
    middle_top_frame_list = (create_middle_grid, create_picture_display_frame, create_enemy_info_display_frame,
                             create_script_display_frame)
    [middle_top_widget() for middle_top_widget in middle_top_frame_list]
    return middle_top_frame


def create_action_buttons_frame(overall_gui_view: dict, game_info: dict) -> tk.Frame:
    """
    Create a frame in the bottom middle of the GUI to display the action buttons for player to trigger events.

    :param overall_gui_view: a dictionary that contain the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param game_info: a dictionary that contains the information of character as value of a key called "character" and
                      the information of the game environment as value of a key called "environment"
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_interface_frame must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_interface_frame must contain a key named as 'Top Frame'
    :precondition: the value of the key "Top Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :precondition: game_info must be a dictionary that contains the information of character as value of a key
                   called "character" and the information of the game environment as value of a key called "environment"
    :postcondition: create a tkinter Frame that contains a game script in the middle of the GUI window
    :raises TypeError: if interface_frames is not a dictionary
    :raises KeyError: if interface_frames does not contain "Top Frame" as key
    :raises AttributeError: if the value of the key "Top Frame" in interface_frame is not an existing tkinter frame
    :return: a tkinter Frame that contains action buttons widgets in the middle of the GUI window
    """

    def create_buttons_grid() -> None:
        """
        Set up the grid in terms of column and row weights for a frame located in the bottom middle side of the GUI.

        :postcondition: set up the grid in terms of column and row weights for a frame located ine the
                        bottom middle of the GUI.
        """
        middle_bottom_frame.grid(column=1, row=1, sticky='nsew')
        middle_bottom_frame.grid_columnconfigure(0, weight=1)
        middle_bottom_frame.grid_columnconfigure(1, weight=1)

    def create_action_buttons() -> None:
        """
        Create four buttons (search, physical attack, magic attack and run) in the bottom middle of the frame in a
        graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_click_button() must not currently exist in the specific frame
        :postcondition: create four buttons (search, physical attack, magic attack and run) in the bottom middle
                        of the frame in a graphical user interface (GUI)
        :raises KeyError: if the proposed widget names in create_click_button() already exists in the specific frame
                          if the widget names cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=middle_bottom_frame, text_label_name="actions_label", message=f"Actions",
                          relief="groove")
        middle_bottom_frame.children['actions_label'].grid(row=1, column=0, columnspan=3, sticky='nsew')

        action_buttons = {'Search': partial(search, overall_gui_view, game_info), 'Physical Attack': None,
                          'Magic Attack': None, 'Run': None}
        for index, (key, value) in enumerate(action_buttons.items()):
            button_name = key.lower().replace(" ", "_")
            create_click_button(belonging_frame=middle_bottom_frame, widget_name_id=button_name, message=key)
            attach_button_function_call(button_name=middle_bottom_frame.children[button_name], callable_function=value)
            middle_bottom_frame.children[button_name].grid(row=index % 2+2, column=index//2, sticky='nsew')
            if key != "Search":
                middle_bottom_frame.children[button_name].config(state="disabled")

    def create_direction_buttons() -> None:
        """
        Create four buttons (move left, move up, move down, move right) in the bottom middle of the frame in a
        graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_click_button() must not currently exist in the specific frame
        :postcondition: create four buttons (move left, move up, move down, move right) in the bottom middle
                        of the frame in a graphical user interface (GUI)
        :raises KeyError: if the proposed widget names in create_click_button() already exists in the specific frame
                          if the widget names cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=middle_bottom_frame, text_label_name="direct_label", message=f"Direction",
                          relief="groove")
        middle_bottom_frame.children['direct_label'].grid(row=4, column=0, columnspan=3, sticky='nsew')

        direction_buttons = ['MOVE LEFT (A)', 'MOVE RIGHT (D)', 'MOVE UP (W)', 'MOVE DOWN (S)']
        for index, key in enumerate(direction_buttons):
            button_name = key.lower().replace(" ", "_")[:-4]
            create_click_button(belonging_frame=middle_bottom_frame, widget_name_id=button_name, message=key)
            attach_button_function_call(button_name=middle_bottom_frame.children[button_name],
                                        callable_function=partial(game, overall_gui_view, game_info, key[-2]))
            middle_bottom_frame.children[button_name].grid(row=index % 2+5, column=index//2, sticky='nsew')

    middle_bottom_frame = tk.Frame(overall_gui_view['Top Frame'], bd=1, relief='groove')
    middle_bottom_list = (create_buttons_grid, create_action_buttons, create_direction_buttons)
    [widget() for widget in middle_bottom_list]
    middle_bottom_frame.bind("<KeyPress>", partial(game, overall_gui_view, game_info))
    middle_bottom_frame.focus_set()
    return middle_bottom_frame


def create_options_frame(overall_game_gui: dict, game_data: dict) -> tk.Frame:
    """
    Create a frame on the side of the GUI to display the buttons for player to trigger events.

    :param overall_game_gui: a dictionary that contain the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param game_data: a dictionary that contains the information of character as value of a key called "character" and
                      the information of the game environment as value of a key called "environment"
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_game_gui must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_game_gui must contain keys named as "Top Frame" and "Item Frame"
    :precondition: the value of the key "Top Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :precondition: the value of the key "Item Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :precondition: game_data must be a dictionary that contains the information of character as value of a key
                   called "character" and the information of the game environment as value of a key called "environment"
    : postcondition: create a frame on the side of the GUI to display the buttons for player to trigger events
    : raises TypeError: if interface_frames is not a dictionary
    : raises KeyError: if interface_frames does not contain "Top Frame" and "Item Frame" as key
    : raises AttributeError: if the value of the key "Top Frame" or "Item Frame" in interface_frame is not
                             an existing tkinter frame
    : return: a tkinter Frame that contains action buttons widgets in the middle of the GUI window
    """
    def create_side_buttons_grid() -> None:
        """
        Set up the grid in terms of column and row weights for a frame located on the right side of the GUI.

        :postcondition: set up the grid in terms of column and row weights for a frame located ine the
                       bottom middle of the GUI.
        """
        right_frame.grid(column=2, row=0, rowspan=2, sticky='nse')
        right_frame.grid_columnconfigure(0, weight=1)
        right_frame.grid_rowconfigure(0, weight=2)
        right_frame.grid_rowconfigure(1, weight=1)

    def toggle_item_frame() -> None:
        """
        Toggle the visibility of the item frame on GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: overall_game_gui must be a dictionary that contains the description of the tkinter objects in
                       string as key and their associated frame or widget objects as value
        :precondition: overall_game_gui must contain a key named as 'Item Frame'
        :raises TypeError: if interface_frames is not a dictionary
        :raises KeyError: if interface_frames does not contain 'Item Frame' as key
        """
        if overall_game_gui['Item Frame'].winfo_viewable():
            overall_game_gui['Item Frame'].grid_forget()
        else:
            overall_game_gui['Item Frame'].grid(column=1, row=0, sticky='nsew')

    def create_side_buttons() -> None:
        """
        Create three buttons (items, save and exit) on the right side of the frame in a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_click_button() must not currently exist in the specific frame
        :postcondition: create three buttons (items, save and exit) on the right side
                        of the frame in a graphical user interface (GUI)
        :raises KeyError: if the proposed widget names in create_click_button() already exists in the specific frame
                         if the widget names cannot be found in the specific frame after creation
        """
        side_dict = {'ITEMS': toggle_item_frame,
                     'SAVE': partial(create_save_file, -1, game_data),
                     'EXIT': partial(closing_event,
                                     overall_game_gui['GUI'], overall_game_gui['pause'])}
        for index, (key, value) in enumerate(side_dict.items()):
            button_name = key.lower().replace(" ", "_")
            create_click_button(belonging_frame=right_frame, widget_name_id=button_name, message=key, bg='#FFDC00')
            attach_button_function_call(button_name=right_frame.children[button_name], callable_function=value)
            right_frame.children[button_name].grid(row=index, sticky='nsew')

    right_frame = tk.Frame(overall_game_gui['Top Frame'], bd=1, relief='groove')
    side_frame_list = (create_side_buttons_grid, create_side_buttons)
    [sid_widget() for sid_widget in side_frame_list]
    return right_frame


def create_item_frame(views_frame: dict, player_data: dict) -> tk.Frame:
    """
    Create a frame on the side of the GUI to display the buttons for player to trigger events.

    :param views_frame: a dictionary that contain the description of the tkinter objects in string as keys
                        and their associated frame or widget objects as value
    :param player_data: a dictionary that contains the description of the character's attributes as key and
                        its corresponding data as values
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: views_frame must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: views_frame must contain a key named as "Top Frame"
    :precondition: the value of the key "Top Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :precondition: player_data must be a dictionary that contains the description of the character's attributes as
                   key and its corresponding data as values
    :postcondition: create a frame on the side of the GUI to display the buttons for player to trigger events
    :raises TypeError: if interface_frames is not a dictionary
    :raises KeyError: if interface_frames does not contain "Top Frame" and "Item Frame" as key
    :raises AttributeError: if the value of the key "Top Frame" or "Item Frame" in interface_frame is not
                           an existing tkinter frame
    :return: a tkinter Frame that contains action buttons widgets in the middle of the GUI window
    """
    item_frame = tk.Frame(views_frame['Top Frame'], name="item_frame", relief='groove')
    create_items_display(item_frame, player_data, views_frame)
    return item_frame


def create_control_layout(overall_gui_widgets: dict, game_data: dict) -> None:
    """
    Recreate a frame located at the top of the GUI with new five inner frames to show the game information and buttons
    for player to trigger events.

    :param overall_gui_widgets: a dictionary that contain the description of the tkinter objects in string as keys
                                and their associated frame or widget objects as value
    :param game_data: a dictionary that contains the information of character as value of a key called "character" and
                      the information of the game environment as value of a key called "environment"
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_game_gui must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_game_gui must contain keys named as "Top Frame" and "Event Bar"
    :precondition: the value of the key "Top Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :precondition: the value of the key "Event Bar" in overall_game_frame dictionary must be an existing tkinter label
    :precondition: game_data must be a dictionary that contains the information of character as value of a key
                   called "character" and the information of the game environment as value of a key called "environment"
    :postcondition: recreate a frame located at the top of the GUI with new five inner frames to show the
                    game information and buttons for player to trigger events
    :raises TypeError: if interface_frames is not a dictionary
    :raises KeyError: if interface_frames does not contain "Top Frame" and "Event Bar" as key
    :raises AttributeError: if the value of the key "Top Frame" or "Event Bar" in interface_frame is not
                            an existing tkinter frame
    """
    def rearrange_game_panel_grid() -> None:
        """
        Rearrange the grid in terms of column and row weights for a frame located at the top of the GUI.

        :postcondition: rearrange the grid in terms of column and row weights for a frame located at the top of the GUI
        """
        player_view_weight = ((1, 0), (0, 1), (0, 0))
        for index, weight_tuple in enumerate(player_view_weight):
            overall_gui_widgets['Top Frame'].grid_rowconfigure(index, weight=weight_tuple[0])
            overall_gui_widgets['Top Frame'].grid_columnconfigure(index, weight=weight_tuple[1])

    [widget.destroy() for widget in overall_gui_widgets['Top Frame'].winfo_children()]
    rearrange_game_panel_grid()
    overall_gui_widgets['Event Bar'].config(text=f"Login as {game_data['character']['Name']}")
    overall_gui_widgets.update({'Status Frame': create_status_frame(overall_gui_widgets, game_data['character']),
                                'Script Frame': create_script_frame(overall_gui_widgets),
                                'Buttons Frame': create_action_buttons_frame(overall_gui_widgets, game_data),
                                'Item Frame': create_item_frame(overall_gui_widgets, game_data['character']),
                                'Side Bar Frame': create_options_frame(overall_gui_widgets, game_data)})


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
