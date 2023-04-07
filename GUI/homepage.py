import tkinter as tk
from datetime import datetime
from functools import partial
from tkinter import messagebox

from GUI import GAME_COVER_PHOTO, GAME_NAME, GAME_ICON, GUI_WINDOW_SIZE, MAX_LEN_NAME, MIN_LEN_NAME
from GUI.interface_setting import gui_menubar, gui_default_setting
from GUI.create_widgets import create_click_button, create_text_label, create_image_label
from GUI.create_widgets import create_user_entry, attach_button_function_call
from GUI.new_player_page import new_player_page
from save_load.load_game_file import load_file


def create_top_frame():
    """
    Create a frame at the top of a graphical user interface (GUI), containing a cover photo,
    a text field for player's name, a button to start a new game, and a button to load a saved game.

    :precondition: a tkinter root window must exist
    :postcondition: create a frame that contains a cover photo, text entry for player's name,
                    "NEW GAME" and "LOAD GAME" buttons, and a copyright label
    :return: a tkinter frame that contains three labels, two buttons and one entry located at the top frame of the GUI
    :raise KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                     if the widget name cannot be found in the specific frame after creation
    """

    def create_cover_photo():
        """
        Create a label containing a cover photo in the top frame of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame used in create_image_label() must be a tkinter frame in the tkinter root window
        :precondition: widget name used in create_image_label() must not currently exist in the specific frame
        :postcondition: create a label containing a cover photo that takes 4 columns width of the GUI
        :raise _tkinter.TclError: if the image represented by image_directory does not exist
                                  if the image_directory does not represent an image
        :raise KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_image_label(frame=main_frame, widget_name="cover_photo", image_path=GAME_COVER_PHOTO)
        main_frame.children['cover_photo'].grid(row=0, columnspan=4, sticky='we', padx=10)

    def create_new_game_widgets():
        """
        Create a text field with label for player to enter their character's name in the top frame
        of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used must not currently exist in the specific frame
        :postcondition: create a text field with label and button to enter and confirm the player's character name
        :raise KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=main_frame, text_label_name="name_label", message="Create Profile: ",
                          font_size=12)
        main_frame.children['name_label'].grid(row=1, column=0, sticky='we', pady=10)

        create_user_entry(upper_frame=main_frame, box_width=30, widget_id="player_name", entry_font_size=12)
        main_frame.children['player_name'].grid(row=1, column=1, sticky='we', padx=10, pady=10)

        create_click_button(belonging_frame=main_frame, widget_name_id="new_game", message="NEW GAME")
        main_frame.children['new_game'].grid(row=1, column=2, sticky='we', pady=10)

    def create_load_game_button():
        """
        Create a load game button in the top frame of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_click_button() must not currently exist in the specific frame
        :postcondition: create a load game button in the top frame of a graphical user interface (GUI)
        :raise KeyError: if the proposed widget name in create_click_button() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_click_button(belonging_frame=main_frame, widget_name_id="load_game", message="LOAD GAME")
        main_frame.children['load_game'].grid(row=1, column=3, sticky='we', padx=10, pady=10)

    def create_copyright_label():
        """
        Create a copyright label in the top frame of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create a copyright label in the top frame of a graphical user interface (GUI).
        :raise KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=main_frame, text_label_name="copyright_label", message="All rights reserved ©",
                          font_style="Yu Gothic UI Semibold", font_size=8)
        main_frame.children['copyright_label'].grid(row=2, column=2, columnspan=2, sticky='e', padx=10)

    main_frame = tk.Frame()
    main_frame.grid(row=0, sticky='news')
    widget_list = (create_cover_photo, create_new_game_widgets, create_load_game_button, create_copyright_label)
    [widget() for widget in widget_list]
    return main_frame


def create_bottom_frame():
    """
    Create a frame located at the bottom of the GUI to provide current date, time and game information for the player.

    :precondition: a tkinter root window must exist
    :postcondition: creates a frame at the bottom of the GUI to display the current date, time,
                    and game information for the player
    :return: a tkinter object that contains all three widgets located at the bottom frame of the GUI
    :raise KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                     if the widget name cannot be found in the specific frame after creation
    """
    def create_date_label():
        """
        Create a label with current date at the bottom of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create a label with current date at the bottom of the GUI
        :raise KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        current_date = datetime.now().strftime("%d %B %Y")
        create_text_label(frame_obj=bottom_frame, text_label_name='date_label', message=current_date)
        bottom_frame.children['date_label'].pack(side='left', padx=10)

    def create_time_label():
        """
        Create a label with current time at the bottom of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create a label with current time at the bottom of the GUI
        :raise KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        current_time = datetime.now().strftime("%H:%M:%S")
        create_text_label(frame_obj=bottom_frame, text_label_name='time_label', message=current_time)
        bottom_frame.children['time_label'].pack(side='right', padx=20)

    def create_game_info_label() -> None:
        """
        Create a label with useful game information for player at the bottom of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create a label with useful game information for player at the bottom of the GUI
        :raise KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                         if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=bottom_frame, text_label_name='event_bar',
                          message="Welcome to Oasis of the Lost Adventure !")
        bottom_frame.children['event_bar'].pack(side='left', padx=30)

    def update_time() -> None:
        """
        Update the date and clock widgets at the bottom of the GUI. with the current datetime every 200ms

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: labels with names "date_label" and "time_label" must exist in the frame
        :postcondition: update the date and clock widgets at the bottom of the GUI with the current datetime every 200ms
        :raise KeyError: if the widget name cannot be found in the specific frame
        """
        bottom_frame.children['date_label'].config(text=datetime.now().strftime("%d %B %Y"))
        bottom_frame.children['time_label'].config(text=datetime.now().strftime("%H:%M:%S"))
        bottom_frame.after(200, update_time)

    bottom_frame = tk.Frame(bd=1, relief='sunken', height=5)
    bottom_frame.grid(row=1, sticky='we')
    bottom_widget_list = (create_date_label, create_time_label, create_game_info_label, update_time)
    [bottom_widget() for bottom_widget in bottom_widget_list]
    return bottom_frame.children['event_bar']


def create_homepage():
    """
    Create and configure a GUI with size, menu bar, frames and widgets for a game

    :postcondition: create and configure a GUI with size, menu bar, frames and widgets for a game
    """
    def gui_setup():
        gui_default_setting(game_window=gui_frames['GUI'], game_title=GAME_NAME,
                            icon_path=GAME_ICON, window_size=GUI_WINDOW_SIZE)
        gui_menubar(gui_frames)

    def new_game_button():
        attach_button_function_call(button_name=gui_frames['Top Frame'].children['new_game'],
                                    callable_function=valid_player_name)

    def load_game_button():
        attach_button_function_call(button_name=gui_frames['Top Frame'].children['load_game'],
                                    callable_function=partial(load_file, gui_frames))

    def valid_player_name():
        """
        Make sure player's name is not an empty string or greater than 10 letters.

        :postcondition: check if the player's name is length of 1 to 10
        """
        name = gui_frames['Top Frame'].children['player_name'].get()
        confirmation = "Do you confirm to create a new game?"
        warning = "Whoa, hold up there! \n\nPlayer name cannot be empty or more than 10 letters!"
        if MIN_LEN_NAME < len(name.strip()) <= MAX_LEN_NAME and messagebox.askyesno(message=confirmation):
            new_player_page(name, gui_frames)
        else:
            messagebox.showinfo(title="Warning!", message=warning)

    gui_frames = {"GUI": tk.Tk(), "Top Frame": create_top_frame(), "Event Bar": create_bottom_frame()}
    gui_setup()
    new_game_button()
    load_game_button()
    print([stack[3] for stack in inspect.stack()])
    return gui_frames


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
