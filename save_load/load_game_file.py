import os
from tkinter import messagebox, filedialog
from utilities.initialize_game import load_into_game
from save_load.uid_converter import decoder
from save_load import DEFAULT_SAVE_FOLDER


def load_file(game_frames):
    """
    Process a selected plain text file after converting the context from string to dictionary that
    represents the player data and game data.

    :parameter game_frames: a dictionary that contains Tkinter frames as value and their corresponding names as keys
    :precondition: game_frames must be a dictionary that contains Tkinter frames and their corresponding names as keys
    :postcondition: load an encoded save file upon user's confirmation

    """
    filename = filedialog.askopenfilename(title="Select a File", initialdir=DEFAULT_SAVE_FOLDER,
                                          filetypes=(("SAVE File", "*.save"), ("SAVE File", " ")))
    if filename:
        with open(filename) as file_object:
            load_save = file_object.read()
        loaded_info = eval(decoder(load_save))
        character = loaded_info['character']
        confirm_message = f" Welcome back! {character['Name']} (Level {str(character['Level']).zfill(2)})\n\n" \
                          f"Are you ready to resume your adventure?"
        if messagebox.askyesno(title="Confirm?", message=confirm_message):
            load_into_game(game_frames, loaded_info)


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
