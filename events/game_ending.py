from functools import partial

from GUI import GAME_MAP_PATH
from GUI.create_widgets import update_image_label, create_click_button, attach_button_function_call, create_text_label
import tkinter as tk
import pathlib


def game_over(overall_gui_info: dict) -> None:
    """
    Update the script display and map widget when the player's HP reaches 0 or below and the game is over.

    :param overall_gui_info: a dictionary that contain the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_interface_frame must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_interface_frame must contain a key named as 'Script Frame'
    :precondition: the value of key "Script Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :precondition: the frame represented by key "Script Frame" must contain a text label widget called "script_display"
    :postcondition: update the script display and map widget when the player's HP reaches 0 or below
                    and the game is over
    :raises TypeError: if overall_gui_info is not a dictionary
    :raises KeyError: if overall_gui_info does not contain 'Script Frame' as key
    """
    overall_gui_info['Script Frame'].children['script_display'].config(
        text="Game Over!\nReload Save to continue!", compound="center", anchor="center")
    if pathlib.Path(GAME_MAP_PATH.format("game_over")).is_file():
        update_image_label(frame_object=overall_gui_info['Status Frame'], label_name="current_map",
                           image_directory=GAME_MAP_PATH.format("game_over"))
    else:
        raise FileNotFoundError("Game map image cannot be found! Please check the path!")


def goal_achieve(progress_switch, environment_info, overall_gui_info):
    """
    Update the GUI script display and creates an "End Game" button with a congratulatory message
    if the player defeats the boss final in the game.

    :param overall_gui_info: a dictionary that contains the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :param environment_info: a dictionary that contains the information of the game environment
    :param progress_switch: a dictionary that contains the event progress inside the current coordinate
    :precondition: overall_gui_info must be a dictionary
    :precondition: environment_info must be a dictionary
    :precondition: progress_switch must be a dictionary
    :precondition: overall_gui_info must contain key named as ['Script Frame']
    :precondition: the value of ['Script Frame'] key must be a tkinter Frame
    :precondition: the tkinter Frame of overall_gui_info['Script Frame'] must contain a tkinter label named as
                   ['script display']
    :precondition: environment_info must contain keys of tuple of coordinates
    :precondition: progress_switch must contain keys named as ['result'] and ['opponent']
    :precondition: the value of ['opponent'] must be a dictionary that contains key named as ["Name"]
    :postcondition: update the GUI script display and creates an "End Game" button with a congratulatory message
    if the player defeats the boss final in the game.
    :raises KeyError: if overall_gui_info does not contain key ['Script Frame']
                      if ['Script Frame'] does not have a widget named as ['script display']
                      if progress_switch does not contain keys ['result'] and ['opponent']
    :raises TypeError: if overall_gui_info, progress_switch and/or environment_info is not a dictionary
    """
    if progress_switch['opponent']['Name'] == "General Havoc" and progress_switch['result'] == "win":
        overall_gui_info['Script Frame'].children['script_display'].config(
            text=f"Congratulation! you have won the game... Or have you? :P")
        environment_info[(1, 0)] = ('Random', '')
        create_click_button(belonging_frame=overall_gui_info['Script Frame'],
                            widget_name_id="end_game", message="End Game")
        overall_gui_info['Script Frame'].children['end_game'].grid(row=2, column=1, sticky="se")
        attach_button_function_call(button_name=overall_gui_info['Script Frame'].children['end_game'],
                                    callable_function=partial(congratulation_scene, overall_gui_info))


def congratulation_scene(overall_gui_info):
    """
    Create a congratulatory message on the top frame of the game GUI when the player wins the game.

    :param overall_gui_info: a dictionary that contain the description of the tkinter objects in string as keys
                             and their associated frame or widget objects as value
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_interface_frame must be a dictionary that contains the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_interface_frame must contain a key named as 'Top Frame'
    :precondition: the value of key "Top Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :postcondition: create a congratulatory message on the top frame of the game GUI when the player wins the game.
    :raises TypeError: if overall_gui_info is not a dictionary
    :raises KeyError: if overall_gui_info does not contain 'Top Frame' as key
    """
    [widget.destroy() for widget in overall_gui_info['Top Frame'].winfo_children()]
    create_text_label(frame_obj=overall_gui_info['Top Frame'], text_label_name="end_game",
                      message="Congratulation! \nYou have won the game!!!", font_size=40,
                      font_style="Amasis MT Pro Black")
    overall_gui_info['Top Frame'].children['end_game'].grid(row=0, sticky="we")


def easter_egg(overall_gui_info):
    """
    Update the frame upon player's discovery on the Easter Egg

    :param overall_gui_info: a dictionary that contain the description of the tkinter objects in string as key and
                     their associated frame or widget objects as value
    :precondition: a tkinter root window must exist
    :precondition: overall_gui_info must be a dictionary that contain the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_gui_info must contain two keys named as "Script Frame", "Buttons Frame" and "Side Bar Frame"
    :precondition: the value of the key "Buttons Frame" in interface_frame dictionary must be an existing frame
    :precondition: the value of the key "Side Bar Frame" in interface_frame dictionary must be an existing frame
    :precondition: the value of key "Script Frame" in overall_game_frame dictionary must be an existing tkinter frame
    :postcondition: update the frame upon player's discovery on the Easter Egg
    :raises KeyError: if overall_gui_info does not contain 'Script Frame' as key
                      if overall_gui_info does not have keys named as "Buttons Frame" and "Side Bar Frame"
                      if "items" and "save" do not exist in the sider bar frame indicated by gui_dict
    """
    overall_gui_info['Script Frame'].children['script_display'].config(
        text=f"Congratulation! \nYou have found the easter egg!!!\n "
             "THIS IS THE REAL ENDING! NICE JOB!")
    for widget in overall_gui_info['Buttons Frame'].winfo_children():
        if isinstance(widget, tk.Button):
            widget.config(state="disabled")
    overall_gui_info['Side Bar Frame'].children['items'].config(state="disabled")
    overall_gui_info['Side Bar Frame'].children['save'].config(state="disabled")
    overall_gui_info['Buttons Frame'].unbind("<KeyPress>")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
