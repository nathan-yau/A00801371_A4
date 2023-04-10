import tkinter as tk
from datetime import datetime
from functools import partial
from tkinter import messagebox
import pathlib

from GUI import GAME_COVER_PHOTO, GAME_NAME, GAME_ICON, GUI_WINDOW_SIZE, MAX_LEN_NAME, MIN_LEN_NAME
from GUI.interface_setting import gui_menubar, gui_default_setting
from GUI.create_widgets import create_click_button, create_text_label, create_image_label
from GUI.create_widgets import create_user_entry, attach_button_function_call
from GUI.new_player_page import create_new_player_page
from save_load.load_game_file import load_file


def create_top_frame() -> tk.Frame:
    """
    Create a frame at the top of a graphical user interface (GUI), containing a cover photo,
    a text field for player's name, a button to start a new game, and a button to load a saved game.

    :precondition: a tkinter root window must exist
    :postcondition: create a frame that contains a cover photo, text entry for player's name,
                    "NEW GAME" and "LOAD GAME" buttons, and a copyright label
    :return: a tkinter frame that contains three labels, two buttons and one entry located at the top frame of the GUI
    :raises KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                      if the widget name cannot be found in the specific frame after creation
    """

    def create_cover_photo() -> None:
        """
        Create a label containing a cover photo in the top frame of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame used in create_image_label() must be a tkinter frame in the tkinter root window
        :precondition: widget name used in create_image_label() must not currently exist in the specific frame
        :postcondition: create a label containing a cover photo that takes 4 columns width of the GUI
        :raises _tkinter.TclError: if the image represented by image_directory does not exist
                                  if the image_directory does not represent an image
        :raises KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                          if the widget name cannot be found in the specific frame after creation
        :raises FileNotFoundError: if GAME_COVER_PHOTO image cannot be found in the given path
        """
        if pathlib.Path(GAME_COVER_PHOTO).is_file():
            create_image_label(frame=main_frame, widget_name="cover_photo", image_path=GAME_COVER_PHOTO)
        else:
            raise FileNotFoundError("Cover image cannot be found! Please check the path!")
        main_frame.children['cover_photo'].grid(row=0, columnspan=4, sticky='we', padx=10)

    def create_new_game_widgets() -> None:
        """
        Create a text field with label for player to enter their character's name in the top frame
        of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used must not currently exist in the specific frame
        :postcondition: create a text field with label and button to enter and confirm the player's character name
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                          if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=main_frame, text_label_name="name_label", message="Create Profile: ",
                          font_size=15)
        main_frame.children['name_label'].grid(row=1, column=0, sticky='we', pady=10)

        create_user_entry(upper_frame=main_frame, box_width=30, widget_id="player_name", entry_font_size=12)
        main_frame.children['player_name'].grid(row=1, column=1, sticky='we', padx=10, pady=10)

        create_click_button(belonging_frame=main_frame, widget_name_id="new_game", message="NEW GAME")
        main_frame.children['new_game'].grid(row=1, column=2, sticky='we', pady=10)

    def create_load_game_button() -> None:
        """
        Create a load game button in the top frame of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_click_button() must not currently exist in the specific frame
        :postcondition: create a load game button in the top frame of a graphical user interface (GUI)
        :raises KeyError: if the proposed widget name in create_click_button() already exists in the specific frame
                          if the widget name cannot be found in the specific frame after creation
        """
        create_click_button(belonging_frame=main_frame, widget_name_id="load_game", message="LOAD GAME")
        main_frame.children['load_game'].grid(row=1, column=3, sticky='we', padx=10, pady=10)

    def create_copyright_label() -> None:
        """
        Create a copyright label in the top frame of a graphical user interface (GUI).

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create a copyright label in the top frame of a graphical user interface (GUI).
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                          if the widget name cannot be found in the specific frame after creation
        """
        create_text_label(frame_obj=main_frame, text_label_name="copyright_label", message="All rights reserved ©",
                          font_style="Yu Gothic UI Semibold", font_size=12)
        main_frame.children['copyright_label'].grid(row=2, column=2, columnspan=2, sticky='e', padx=10)

    main_frame = tk.Frame()
    main_frame.grid(row=0, sticky='news')
    widget_list = (create_cover_photo, create_new_game_widgets, create_load_game_button, create_copyright_label)
    [widget() for widget in widget_list]
    return main_frame


def create_bottom_frame() -> tk.Label:
    """
    Create a frame located at the bottom of the GUI to provide current date, time and game information for the player.

    :precondition: a tkinter root window must exist
    :postcondition: creates a frame at the bottom of the GUI to display the current date, time,
                    and game information for the player
    :return: a tkinter object that contains the text label located at the bottom frame of the GUI
    :raises KeyError: if the proposed widget name in create_image_label() already exists in the specific frame
                      if the widget name cannot be found in the specific frame after creation
    """
    def create_date_label() -> None:
        """
        Create a label with current date at the bottom of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create a label with current date at the bottom of the GUI
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
                          if the widget name cannot be found in the specific frame after creation
        """
        current_date = datetime.now().strftime("%d %B %Y")
        create_text_label(frame_obj=bottom_frame, text_label_name='date_label', message=current_date)
        bottom_frame.children['date_label'].pack(side='left', padx=10)

    def create_time_label() -> None:
        """
        Create a label with current time at the bottom of the GUI.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: widget name used in create_text_label() must not currently exist in the specific frame
        :postcondition: create a label with current time at the bottom of the GUI
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
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
        :raises KeyError: if the proposed widget name in create_text_label() already exists in the specific frame
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
        :raises KeyError: if the widget name cannot be found in the specific frame
        """
        bottom_frame.children['date_label'].config(text=datetime.now().strftime("%d %B %Y"))
        bottom_frame.children['time_label'].config(text=datetime.now().strftime("%H:%M:%S"))
        bottom_frame.after(200, update_time)

    bottom_frame = tk.Frame(bd=1, relief='sunken', height=5)
    bottom_frame.grid(row=1, sticky='we')
    bottom_widget_list = (create_date_label, create_time_label, create_game_info_label, update_time)
    [bottom_widget() for bottom_widget in bottom_widget_list]
    return bottom_frame.children['event_bar']


def create_homepage() -> dict:
    """
    Create and configure a GUI with size, menu bar, two frames and nine widgets for welcome page of a game.

    :postcondition: create and configure a GUI with size, menu bar, frames and widgets for welcome page of a game
    :return: a dictionary that contains all existing tkinter frames as values and their description as keys
    :raises NamError: if MAX_LEN_NAME, MIN_LEN_NAME, GAME_NAME, GAME_ICON and/or GUI_WINDOW_SIZE are not defined
    :raises _tkinter.TclError: if GAME_ICON is not an image path that represents an existing image or the image
                              does not exist in the path it represents
                              if GUI_WINDOW_SIZE must be a geometry specifier as string in the format like "100x120"
    """
    def gui_setup() -> None:
        """
        Configure a GUI with the window size and menu bar.

        :precondition: a tkinter root window must be defined
        :precondition: GAME_NAME, GAME_ICON and GUI_WINDOW_SIZE must be defined
        :precondition: GAME_ICON must be an image path that represents an existing image
        :precondition: GUI_WINDOW_SIZE must be a geometry specifier as string in the format like "100x120"
                       where 100 represents the width and 120 represents the height of the GUI
        :postcondition: configure a GUI with the window size and menu bar
        :raises NamError: if GAME_NAME, GAME_ICON and/or GUI_WINDOW_SIZE are not defined
        :raises _tkinter.TclError: if GAME_ICON is not an image path that represents an existing image or the image
                                  does not exist in the path it represents
                                  if GUI_WINDOW_SIZE must be a geometry specifier as string in the format like "100x120"

        """
        gui_default_setting(game_window=gui_frames['GUI'], game_title=GAME_NAME,
                            icon_path=GAME_ICON, window_size=GUI_WINDOW_SIZE, pause=gui_frames['pause'])
        gui_menubar(gui_frames)

    def attach_function_to_new_game_button() -> None:
        """
        Attach a callable function to button called new_game.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: a button called new_game must currently exist in the specific frame
        :precondition: function being attached to the button must be a callable function or None type
        :postcondition: attach a callable function to button called new_game
        :raises KeyError: if the button is not found in the frame
                         if the key of the frame cannot be found in the dictionary gui_frames
        :raises TypeError: if callable_function is not a callable function or None type
        """
        attach_button_function_call(button_name=gui_frames['Top Frame'].children['new_game'],
                                    callable_function=valid_player_name)

    def attach_function_to_load_game_button() -> None:
        """
        Attach a callable function to button called load_game.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: a button called load_game must currently exist in the specific frame
        :precondition: function being attached to the button must be a callable function
        :postcondition: attach a callable function to button called new_game
        :raises KeyError: if the button is not found in the frame
                         if the key of the frame cannot be found in the dictionary gui_frames
        :raises TypeError: if gui_frames is not a dictionary
                          if callable_function is not a callable function or None type
        """
        attach_button_function_call(button_name=gui_frames['Top Frame'].children['load_game'],
                                    callable_function=partial(load_file, gui_frames))

    def valid_player_name() -> None:
        """
        Make sure player's name is not an empty string or greater than 10 letters.

        :precondition: a tkinter root window must exist and contain at least one frame
        :precondition: frame must be an existing tkinter frame in the tkinter root window
        :precondition: an entry box called "plater_name" must exist in the tkinter frame
        :precondition: MAX_LEN_NAME and MIN_LEN_NAME must be defined
        :precondition: MAX_LEN_NAME and MIN_LEN_NAME must be integers
        :precondition: gui_frames must be a dictionary
        :postcondition: check if the player's name is length of 1 to 10
        :raises NameError: if MAX_LEN_NAME and/or MIN_LEN_NAME are not defined
        :raises TypeError: if gui_frames is not a dictionary
        :raises KeyError: if "Top Frame" key is not found under gui_frames dictionary
                         if player_name entry nox is not found in the frame stored in the gui_frames dictionary
                         with a key "Top Frame"
        """
        name = gui_frames['Top Frame'].children['player_name'].get()
        confirmation = "Do you confirm to create a new game?"
        warning = "Whoa, hold up there! \n\nPlayer name cannot be empty or more than 10 letters!"
        if MIN_LEN_NAME < len(name.strip()) <= MAX_LEN_NAME and messagebox.askyesno(message=confirmation):
            create_new_player_page(name, gui_frames)
        else:
            messagebox.showinfo(title="Warning!", message=warning)

    gui_frames = {"GUI": tk.Tk(), "Top Frame": create_top_frame(), "Event Bar": create_bottom_frame(),
                  "pause": tk.BooleanVar()}
    gui_level_list = (gui_setup, attach_function_to_new_game_button, attach_function_to_load_game_button)
    [gui_function() for gui_function in gui_level_list]
    return gui_frames


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
