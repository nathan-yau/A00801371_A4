import os
from tkinter import messagebox
from GUI.game_page import create_control_layout
from new_game.new_environment import make_environment_attributes
from save_load.save_game_file import create_save_file
from save_load import DEFAULT_SAVE_FOLDER


def load_into_game(all_interface_widgets: dict, game_info: dict) -> None:
    """
    Based on the game state (resume game or new game), load all necessary game data into the GUI

    :param all_interface_widgets: a dictionary that contain the description of the tkinter objects in string as
                                  key and their associated frame or widget objects as value
    :param game_info: a dictionary that contains the information of character and may or may not
                      the information of the game environment as value of a key called "environment"
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: all_interface_widgets must be a dictionary containing all the interface frame
    :precondition: game_info must be a dictionary containing the information of character
    :precondition: game_info must contain either 'character' or 'Name' key
    :precondition: the 'character' key of game_info must contain a dictionary of the character's attributes if it exists
    :precondition: game_info must contain the character's attributes if it exists
    :precondition: game_info must contain the 'Name' key if 'character' key does not exist in game_info
    :precondition: DEFAULT_SAVE_FOLDER must be defined and refer to a directory
    :postcondition: creates a new save file if a new character is created
    :postcondition: load all necessary game data and start the game with a GUI
    :raises KeyError: if game_info does not contain neither 'character' nor 'Name' key
    :raises TypeError: if all_interface_widgets or game_info is not a dictionary
    """
    if type(all_interface_widgets) is not dict or type(game_info) is not dict:
        raise TypeError("all_interface_widgets and game_info must be a dictionary.")
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


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()