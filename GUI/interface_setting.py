import tkinter as tk
from functools import partial
from save_load.load_game_file import load_file


def gui_default_setting(game_window, game_title: str, icon_path: str, window_size: str) -> None:
    """
    Create default window and grid setting for a tkinter GUI.

    :param game_window: a tkinter root window
    :param game_title: a string that represents the title of the game
    :param icon_path: an image path that represents an existing image
    :param window_size: a geometry specifier as string in the format like "100x120"
                        where 100 represents the width and 120 represents the height of the GUI
    :precondition: a tkinter root window must exist
    :precondition: game_window must be the tkinter root window
    :precondition: game_title must be a string
    :precondition: icon_path must be an image path that represents an existing image
    :precondition: window_size must be a geometry specifier as string in the format like "100x120"
                   where 100 represents the width and 120 represents the height of the GUI
    :postcondition: create default window and grid setting for a tkinter GUI
    :raise AttributeError: if game_window is not a tkinter root window
    :raise _tkinter.TclError: if icon_path is not an image path that represents an existing image or the image
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
    game_window.protocol("WM_DELETE_WINDOW", partial(closing_event, game_window))


def closing_event() -> None:
    if tk.messagebox.askyesno(title="Confirm?", message="Do you confirm to close this awesome game?"):
        exit()


def gui_menubar(overall_gui) -> None:
    menu_bar = tk.Menu()

    def create_file_menu():
        file_menu = tk.Menu(menu_bar, tearoff=False)
        menu_bar.add_cascade(menu=file_menu, label="File")

        file_dict = {"Load Game": partial(load_file, overall_gui),
                     "Seperator": None, "Exit Game": closing_event}
        for key, value in file_dict.items():
            if key == "Seperator":
                file_menu.add_separator()
            else:
                file_menu.add_command(label=key, command=value)

    create_file_menu()
    overall_gui['GUI'].config(menu=menu_bar)
