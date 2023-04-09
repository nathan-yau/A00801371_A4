import os
from tkinter import messagebox, filedialog
from save_load.uid_converter import encoder
from save_load import DEFAULT_SAVE_FOLDER


def create_save_file(save_slot: int, all_key_attributes: dict) -> None:
    """
    Saves an encoded dictionary as a string to a file, given a save slot and all key attributes.

    :parameter save_slot: an integer that represents the slot in which the save file will be stored,
                          or -1 to indicate for open file window for selection
    :parameter all_key_attributes: a dictionary that contains all player data and game environment data
    :precondition: save_slot must be greater than or equal to -1
    :precondition: all_key_attributes must be a dictionary that conatins all player data and game environment data
    :postcondition: create a plan text file, which contains an encoded dictionary as string
    :raise TypeError: if all_key_attributes is not a dictionary
    """
    if type(all_key_attributes) is not dict:
        raise TypeError("all_key_attributes must be dictionary")
    if save_slot == -1:
        filename = filedialog.askopenfilename(title="Select a File", initialdir=DEFAULT_SAVE_FOLDER,
                                              filetypes=(("SAVE File", "*.save"), ("SAVE File", " ")))
    else:
        filename = f'{DEFAULT_SAVE_FOLDER}SAVE{str(save_slot).zfill(2)}.save'
    if filename:
        saves = encoder(phrase=str(all_key_attributes))
        with open(filename, 'w') as file_object:
            file_object.write(saves)
        messagebox.showinfo(title="Saved!", message=f"Progress Saved - {filename[-11:]}")
    else:
        messagebox.showinfo(title="Warning!", message=f"Select a file to save your progress.")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
