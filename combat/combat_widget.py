from GUI.create_widgets import attach_button_function_call
from functools import partial
from combat.combat_actions import attack, run_away


def toggle_battle_buttons(overall_gui: dict, action: str) -> None:
    """
    Toggle the active state of battle related buttons / keypress listeners in the GUI.

    :param overall_gui: a dictionary that contain the description of the tkinter objects in string as key and
                        their associated frame or widget objects as value
    :param action: a string that is either "enable" or "disable"
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: overall_gui must be a dictionary that contain the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: overall_gui must contain a key named as "Buttons Frame" and "Side Bar Frame"
    :precondition: "Buttons Frame" must be an existing tkinter frame in the tkinter root window
    :precondition: "Buttons Frame" must be a tkinter frame
    :precondition: "Buttons Frame" must contain buttons named as ['move_left'],
                   ['move_right'], ['move_up'], ['move_down'], ['search'], ['physical_attack'],
                   ['magic_attack'] and ['run']
    :precondition: "Side Bar Frame" must be an existing tkinter frame in the tkinter root window
    :precondition: "Side Bar Frame" must be a tkinter frame
    :precondition: "Side Bar Frame" must contain button named as ['save']
    :precondition: action must be a string that is either "enable" or "disable"
    :postcondition: toggle the active state of battle related buttons / keypress listeners in the GUI.
    :raises TypeError: if overall_gui is not a dict
    :raises KeyError: if overall_gui does not contain "Buttons Frame" or "Side Bar Frame"
                      if "Side Bar Frame" does not contain buttons named as ['save']
                      if "Buttons Frame" does not contain buttons named as ['move_left'],
                      ['move_right'], ['move_up'], ['move_down'], ['search'], ['physical_attack'],
                      ['magic_attack'] and ['run']
    :raises ValueError: if action is not a string that is either "enable" or "disable"
    """
    if type(action) is not str or action not in ["enable", "disable"]:
        raise ValueError("action parameter must be 'enable' or 'disable'")
    movement_state = "normal"
    battle_state = "disabled"
    if action == "enable":
        movement_state = "disabled"
        battle_state = "normal"
        overall_gui['Buttons Frame'].unbind("<KeyPress>")
    disable_button = ['move_left', 'move_right', 'move_up', 'move_down', 'search']
    [overall_gui['Buttons Frame'].children[button].config(state=movement_state) for button in disable_button]
    enable_button = ['physical_attack', 'magic_attack', 'run']
    [overall_gui['Buttons Frame'].children[button].config(state=battle_state) for button in enable_button]
    overall_gui['Side Bar Frame'].children['save'].config(state=movement_state)


def activate_battle_button(interface_views: dict, player_info: dict, opponent: dict) -> None:
    """
    Attach callable functions to buttons for battle (physical_attacked, magic_attack and run)

    :param player_info: a dictionary that contains the description of the character's attributes as key and
                        its corresponding data as values
    :param interface_views: a dictionary that contain the description of the tkinter objects in string as key and
                            their associated frame or widget objects as value
    :param opponent: a dictionary that contains the description of the enemy's attributes as key and
                     its corresponding data as values
    :precondition: player_info must be a dictionary that contains the description of the character's attributes as key
                   and its corresponding data as values
    :precondition: opponent must be a dictionary that contains the description of the enemy's attributes as key and
                   its corresponding data as values
    :precondition: a tkinter root window must exist and contain at least one frame
    :precondition: frame must be an existing tkinter frame in the tkinter root window
    :precondition: interface_views must be a dictionary that contain the description of the tkinter objects in
                   string as key and their associated frame or widget objects as value
    :precondition: interface_views must contain a key named as "Buttons Frame"
    :precondition: the value of the key "Buttons Frame" in interface_frame dictionary must be an existing frame
    :precondition: buttons called "physical_attack", "magic_attack", "run" must currently exist in the specific frame
    :precondition: function being attached to the button must be a callable function or None type
    :postcondition: attach callable functions to buttons (physical_attacked, magic_attack and run)
    :raise KeyError: if the buttons cannot be found in the frame
                     if the key of the frame cannot be found in the gui_dict
    :raise TypeError: if callable_function is not a callable function or None type
                      if interface_views, player_info and/or opponent is not a dictionary
    """
    attach_button_function_call(button_name=interface_views['Buttons Frame'].children['physical_attack'],
                                callable_function=partial(attack, 'physical', player_info, interface_views,
                                                          opponent))
    attach_button_function_call(button_name=interface_views['Buttons Frame'].children['magic_attack'],
                                callable_function=partial(attack, 'magic', player_info, interface_views, opponent))
    attach_button_function_call(button_name=interface_views['Buttons Frame'].children['run'],
                                callable_function=partial(run_away, player_info, interface_views, opponent))


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
