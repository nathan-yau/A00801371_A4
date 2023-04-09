import os
import tkinter as tk
from tkinter import messagebox
from GUI.game_page import create_control_layout
from new_game.new_environment import make_environment_attributes
from save_load.save_game_file import create_save_file
from save_load import DEFAULT_SAVE_FOLDER


def load_into_game(all_interface_widgets: dict, game_info: dict):
    """

    :param all_interface_widgets:
    :param game_info:
    :return:
    """
    if not os.path.exists(DEFAULT_SAVE_FOLDER):
        os.mkdir(DEFAULT_SAVE_FOLDER)
    if 'character' in game_info.keys():
        create_control_layout(all_interface_widgets, game_info)
    elif messagebox.askyesno(title="Confirm?", message=f"Do you confirm to create a player - {game_info['Name']}?"):
        game_board = make_environment_attributes(5, 5)
        game_state = {'character': game_info, 'environment': game_board}
        create_save_file(len(os.listdir(DEFAULT_SAVE_FOLDER)) + 1, game_state)
        messagebox.showinfo(title="Welcome!", message="Welcome to Oasis of Lost Adventure!\nEnjoy the game!")
        create_control_layout(all_interface_widgets, game_state)
