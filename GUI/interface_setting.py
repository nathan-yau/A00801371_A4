import tkinter as tk
from functools import partial
from save_load.load_game_file import load_file


def gui_default_setting(game_window, game_title, icon_path, window_size):
    icon = tk.PhotoImage(file=icon_path)
    game_window.grid_rowconfigure(0, weight=1)
    game_window.grid_columnconfigure(0, weight=1)
    game_window.resizable(False, False)
    game_window.title(game_title)
    game_window.iconphoto(False, icon)
    game_window.geometry(window_size)
    game_window.protocol("WM_DELETE_WINDOW", closing_event)


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
