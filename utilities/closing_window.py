import tkinter as tk


def closing_event(game_window, pause: tk.BooleanVar) -> None:
    """
    Close out all tkinter windows upon the player's confirmation on exiting the program.

    :param game_window: a tkinter root window
    :param pause: a tkinter boolean value used for indicating whether the game is currently paused or not
    :precondition: game_window must be a tkinter root window
    :postcondition: close out all tkinter windows upon the player's confirmation on exiting the program.
    :raises AttributeError: if game_window is not a tkinter root window
    """
    if tk.messagebox.askyesno(title="Confirm?", message="Do you confirm to close this awesome game?"):
        if pause.get():
            tk.messagebox.showwarning(title="Confirm?", message="Can't exit game during battle")
        else:
            game_window.destroy()
            quit()


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()