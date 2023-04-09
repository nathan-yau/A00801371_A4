import tkinter as tk
from functools import partial
from save_load.load_game_file import load_file
from utilities.closing_window import closing_event


def gui_default_setting(game_window, game_title: str, icon_path: str, window_size: str, pause: tk.BooleanVar) -> None:
    """
    Create default window and grid setting for a tkinter GUI.

    :param game_window: a tkinter root window
    :param game_title: a string that represents the title of the game
    :param icon_path: an image path that represents an existing image
    :param window_size: a geometry specifier as string in the format like "100x120"
                        where 100 represents the width and 120 represents the height of the GUI
    :param pause: a tkinter boolean value used for indicating whether the game is currently paused or not
    :precondition: a tkinter root window must exist
    :precondition: game_window must be the tkinter root window
    :precondition: game_title must be a string
    :precondition: icon_path must be an image path that represents an existing image
    :precondition: window_size must be a geometry specifier as string in the format like "100x120"
                   where 100 represents the width and 120 represents the height of the GUI
    :postcondition: create default window and grid setting for a tkinter GUI
    :raises AttributeError: if game_window is not a tkinter root window
    :raises _tkinter.TclError: if icon_path is not an image path that represents an existing image or the image
                              does not exist in the path it represents
                              if window_size must be a geometry specifier as string in the format like "100x120"
    """
    icon = tk.PhotoImage(file=icon_path)
    game_window.grid_rowconfigure(0, weight=1)
    game_window.grid_columnconfigure(0, weight=1)
    game_window.resizable(False, False)
    game_window.title(game_title)
    game_window.iconphoto(False, icon)
    game_window.geometry(window_size)
    game_window.protocol("WM_DELETE_WINDOW", partial(closing_event, game_window, pause))


def gui_menubar(overall_gui: dict) -> None:
    """
    Attach a newly created file menu dropdown tab with its options to the menu bar of the given GUI.

    :param overall_gui: a dictionary that contain the description of the tkinter objects in string as keys and
                        their associated frame or widget objects as value
    :precondition: a tkinter root window must exist
    :precondition: overall_gui must be a dictionary that contain the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_gui must contain a key named as 'GUI'
    :precondition: the value of "GUI" in overall_gui dictionary must be an existing tkinter root window
    :postcondition: attach a newly created file menu dropdown tab with its options to the menu bar of the given GUI
    :raises AttributeError: if the value of "GUI" in overall_gui dictionary is not a tkinter root window
    """
    menu_bar = tk.Menu(name="menu_bar")

    def create_file_menu():
        """
        Create file menu dropdown tab with load game and exit game options on the menu bar of the given GUI.

        :precondition: game_window a tkinter root window
        :postcondition: close out all tkinter windows upon the player's confirmation on exiting the program
        :raises AttributeError: if game_window is not a tkinter root window
        """
        file_menu = tk.Menu(menu_bar, tearoff=False, name="file_menu")
        menu_bar.add_cascade(menu=file_menu, label="File")

        file_dict = {"Load Game": partial(load_file, overall_gui),
                     "Seperator": None, "Exit Game": partial(closing_event, overall_gui['GUI'], overall_gui['pause'])}
        for key, value in file_dict.items():
            if key == "Seperator":
                file_menu.add_separator()
            else:
                file_menu.add_command(label=key, command=value)

    create_file_menu()
    overall_gui['GUI'].config(menu=menu_bar)
