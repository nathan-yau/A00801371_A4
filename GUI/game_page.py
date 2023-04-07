import tkinter as tk
from functools import partial

from GUI.create_widgets import create_click_button, create_text_label, create_image_label, attach_button_function_call
from GUI import GAME_MAP_PATH, GAME_LOCATION_IMAGE_PATH
from GUI import interface_setting
from events.action_manager import gameplay

from save_load.save_game_file import create_save_file
from GUI_update.status_frame import update_status_message
from events.serach_event import search, create_items_display


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
    :raise TypeError: if interface_frames is not a dictionary
                      if player_data is not a dictionary
    :raise KeyError: if interface_frames does not contain "Top Frame" as key
                     if player_data does not contain "Name", "X-coordinate" and "Y-coordinate" as key
    :raise AttributeError: if the value of the key "Top Frame" in interface_frame is not an existing tkinter frame
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
        :raise KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
                         if player_data does not contain "Name" as key
        """
        create_text_label(frame_obj=left_frame, text_label_name="status_label",
                          message=f"{player_data['Name']}'s Status", font_size=10, pady=5, relief="groove",
                          bg="#E89F71")
        left_frame.children['status_label'].grid(row=2, sticky='nsew')

        create_text_label(frame_obj=left_frame, text_label_name="character_status", font_size=12,
                          message=update_status_message(player_data), anchor="sw", justify="left")
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
        :raise KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
                         if player_data does not contain "X-coordinate" and "Y-coordinate" as keys
        """
        coordinate = str(player_data["X-coordinate"]) + str(player_data["Y-coordinate"])
        create_text_label(frame_obj=left_frame, text_label_name="map_label", message=f"Current Oasis Map",
                          font_size=10, pady=5, relief="groove", bg="#E89F71")
        left_frame.children['map_label'].grid(row=0, sticky='new')
        create_image_label(frame=left_frame, widget_name="current_map", image_path=GAME_MAP_PATH.format(coordinate))
        left_frame.children['current_map'].grid(row=1, sticky='nsew')

    left_frame = tk.Frame(overall_game_frame['Top Frame'], bd=1, relief='sunken', padx=0, pady=0)
    left_frame_list = (left_frame_grid_setting, create_character_status_widget, create_map_widget)
    [left_widget() for left_widget in left_frame_list]
    return left_frame


def create_script_frame(overall_interface_frame, game_info):
    middle_top_frame = tk.Frame(overall_interface_frame['Top Frame'], bd=1, relief='groove')

    def create_middle_grid():
        middle_top_frame.grid(column=1, row=0, sticky='nsew')
        middle_top_frame.grid_columnconfigure(0, weight=3)
        middle_top_frame.grid_columnconfigure(1, weight=0)
        middle_top_frame.grid_rowconfigure(0, weight=0)
        middle_top_frame.grid_rowconfigure(1, weight=1)
        # for index, cell in enumerate([(1, 1), (1, 0)]):
        #     column, row = cell
        #     middle_top_frame.grid_columnconfigure(index, weight=column)
        #     middle_top_frame.grid_rowconfigure(index, weight=row)
        #     print(index, column, row)

    def create_picture_display_frame():
        create_image_label(frame=middle_top_frame, widget_name="image_box", image_path=GAME_LOCATION_IMAGE_PATH.format("default"))
        middle_top_frame.children['image_box'].grid(row=0, column=1, sticky='nswe')

    def create_enemy_info_display_frame():
        create_text_label(frame=middle_top_frame, widget_name="enemy_info", message=f"",
                          font_size=10, relief="groove", justify="left")
        middle_top_frame.children['enemy_info'].grid(row=0, column=0, sticky='nswe')

    def create_script_display_frame():
        create_text_label(frame=middle_top_frame, widget_name="script_display", message=f"Welcome to Oasis",
                          font_size=8, pady=10, relief="groove")
        middle_top_frame.children['script_display'].grid(row=1, column=0, columnspan=2, sticky='nswe')

    create_middle_grid()
    create_picture_display_frame()
    create_enemy_info_display_frame()
    create_script_display_frame()
    return middle_top_frame


def create_action_buttons_frame(overall_gui_view, game_info):
    middle_bottom_frame = tk.Frame(overall_gui_view['Top Frame'], bd=1, relief='groove')
    middle_bottom_frame.grid(column=1, row=1, sticky='nsew')
    middle_bottom_frame.grid_columnconfigure(0, weight=1)
    middle_bottom_frame.grid_columnconfigure(1, weight=1)

    def create_action_buttons():
        create_text_label(frame=middle_bottom_frame, widget_name="actions_label", message=f"Actions", relief="groove")
        middle_bottom_frame.children['actions_label'].grid(row=1, column=0, columnspan=3, sticky='nsew')

        action_buttons = {'Search': None,
                          'Physical Attack': None,
                          'Magic Attack': None,
                          'Run': None}
        for index, (key, value) in enumerate(action_buttons.items()):
            button_name = key.lower().replace(" ", "_")
            create_click_button(frame=middle_bottom_frame, widget_name=button_name, message=key)
            # attach_button_function_call(button_name=middle_bottom_frame.children[button_name],
            #                             callable_function=value)
            middle_bottom_frame.children[button_name].grid(row=index % 2+2, column=index//2, sticky='nsew')
            if key != "Search":
                middle_bottom_frame.children[button_name].config(state="disabled")

    def create_direction_buttons():
        create_text_label(frame=middle_bottom_frame, widget_name="direct_label", message=f"Direction", relief="groove")
        middle_bottom_frame.children['direct_label'].grid(row=4, column=0, columnspan=3, sticky='nsew')

        direction_buttons = ['MOVE LEFT (A)', 'MOVE RIGHT (D)', 'MOVE UP (W)', 'MOVE DOWN (S)']
        for index, key in enumerate(direction_buttons):
            button_name = key.lower().replace(" ", "_")[:-4]
            create_click_button(frame=middle_bottom_frame, widget_name=button_name, message=key)
            attach_button_function_call(button_name=middle_bottom_frame.children[button_name],
                                        callable_function=partial(gameplay, overall_gui_view, game_info, key[-2]))
            middle_bottom_frame.children[button_name].grid(row=index % 2+5, column= index//2, sticky='nsew')

    create_action_buttons()
    create_direction_buttons()
    middle_bottom_frame.bind("<KeyPress>", partial(gameplay, overall_gui_view, game_info))
    middle_bottom_frame.focus_set()
    return middle_bottom_frame


def create_options_frame(overall_game_gui, game_data):
    right_frame = tk.Frame(overall_game_gui['Top Frame'], bd=1, relief='groove')
    right_frame.grid(column=2, row=0, rowspan=2, sticky='nse')
    right_frame.grid_columnconfigure(0, weight=1)
    right_frame.grid_rowconfigure(0, weight=2)
    right_frame.grid_rowconfigure(1, weight=1)

    def toggle_item_frame():
        if overall_game_gui['Item Frame'].winfo_viewable():
            overall_game_gui['Item Frame'].grid_forget()
        else:
            overall_game_gui['Item Frame'].grid(column=1, row=0, sticky='nsew')

    side_dict = {'ITEMS': toggle_item_frame,
                 'SAVE': partial(create_save_file, -1, game_data),
                 'EXIT': interface_setting.closing_event}
    for index, (key, value) in enumerate(side_dict.items()):
        button_name = key.lower().replace(" ", "_")
        create_click_button(frame=right_frame, widget_name=button_name, message=key, bg='#FFDC00')
        attach_button_function_call(button_name=right_frame.children[button_name], callable_function=value)
        right_frame.children[button_name].grid(row=index, sticky='nsew')
    return right_frame


def create_item_frame(views_frame, player_data):
    item_frame = tk.Frame(views_frame['Top Frame'], name="item_frame", relief='groove')
    for index, (key, value) in enumerate(player_data["Items"].items()):
        button_name = key.lower().replace(" ", "_")
        item_frame.grid_rowconfigure(index, weight=1)

        create_image_label(frame=item_frame, widget_name=f"{button_name}_image",
                           image_path=GAME_ITEM_IMAGE_PATH.format(key))
        item_frame.children[f"{button_name}_image"].grid(row=index, column=0, sticky='e', padx=(35, 0))

        create_text_label(frame=item_frame, widget_name=f"{button_name}_label", message=f"{key} x {value}", font_size=8)
        item_frame.children[f"{button_name}_label"].grid(row=index, column=1, sticky='nsew', padx=(35, 0))
        if key not in ["Sanctum Key", "Raw Pig", "Oasis Explorer"]:
            create_click_button(frame=item_frame, widget_name=f"{button_name}_button", message="USE")
            item_frame.children[f"{button_name}_button"].grid(row=index, column=2, sticky='e', padx=(35, 0), ipadx=20)
    return item_frame
    # display_message.children['item_frame'].children['heal_potions'].config(
    #     command=partial(using_health_potion, player_info, status_column, display_message))


def create_control_layout(overall_gui_widgets, game_data: dict):
    def rearrange_game_panel_grid():
        player_view_weight = ((1, 0), (0, 1), (0, 0))
        for index in range(3):
            overall_gui_widgets['Top Frame'].grid_rowconfigure(index, weight=player_view_weight[index][0])
            overall_gui_widgets['Top Frame'].grid_columnconfigure(index, weight=player_view_weight[index][1])

    for widget in overall_gui_widgets['Top Frame'].winfo_children():
        widget.destroy()
    rearrange_game_panel_grid()
    overall_gui_widgets['Event Bar'].config(text=f"Login as {game_data['character']['Name']}")
    overall_gui_widgets.update({'Status Frame': create_status_frame(overall_gui_widgets, game_data['character']),
                                'Script Frame': create_script_frame(overall_gui_widgets, game_data),
                                'Buttons Frame': create_action_buttons_frame(overall_gui_widgets, game_data),
                                'Item Frame': create_item_frame(overall_gui_widgets, game_data['character']),
                                'Side Bar Frame': create_options_frame(overall_gui_widgets, game_data)})
    print([stack[3] for stack in inspect.stack()])


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
