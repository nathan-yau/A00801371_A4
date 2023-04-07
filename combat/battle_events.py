import random
import inspect
import tkinter as tk
from GUI.create_widgets import attach_button_function_call
from functools import partial


def random_run_away_probability():
    return random.randint(0, 2) == 0


def damage_taken(player_info, all_widgets, damage):
    player_info['Current HP'] -= max(1, damage)
    check_if_alive(all_widgets, player_info)


def check_if_alive(gui_dict, player_info):
    def disable_buttons():
        button_frame_widgets = gui_dict['Buttons Frame'].winfo_children()
        [widget.config(state="disabled") for widget in button_frame_widgets if isinstance(widget, tk.Button)]
        gui_dict['Side Bar Frame'].children['items'].config(state="disabled")
        gui_dict['Side Bar Frame'].children['save'].config(state="disabled")
    if player_info['Current HP'] <= 0:
        disable_buttons()


def activate_battle_button(interface_views, game_info, opponent, var):
    attach_button_function_call(button_name=interface_views['Buttons Frame'].children['physical_attack'],
                                callable_function=partial(attack, 'physical', game_info['character'], interface_views,
                                                          opponent, var))
    attach_button_function_call(button_name=interface_views['Buttons Frame'].children['magic_attack'],
                                callable_function=partial(attack, 'magic', game_info['character'], interface_views,
                                                          opponent, var))
    attach_button_function_call(button_name=interface_views['Buttons Frame'].children['run'],
                                callable_function=partial(run_away, game_info['character'], interface_views,
                                                          opponent, var))


def attack(attack_type, player_info, all_widgets_dict, foe, var):
    if attack_type == "magic":
        player_attack = int((player_info['Magic Power']*0.6 - foe['Magic Resistance']*1.5) * (1+random.randint(0, 40)/100))
    else:
        player_attack = int((player_info['Strength'] * 0.6 - foe['Dexterity'] * 1.5) * (1 + random.randint(0, 40) / 100))

    foe_attack = int((foe['Strength'] * 1.5 - player_info['Dexterity'] * 1.0) * (1 + random.randint(10, 100) / 100))

    if random.randint(0, 1) == 0:
        foe['HP'] -= max(1, player_attack)
        damage_taken(player_info, all_widgets_dict, foe_attack)
        all_widgets_dict['Event Bar'].config(text=f"Physical Attack {foe['Name']}!")
    else:
        all_widgets_dict['Event Bar'].config(text=f"{foe['Name']} Attack First!")
        damage_taken(player_info, all_widgets_dict, foe_attack)
        foe['HP'] -= max(1, player_attack)
    var.set(True)


def run_away(game_info, all_widgets_dict, foe, var):
    foe_attack = int((foe['Strength']*1.5 - game_info['Dexterity']*1.0) * (1+random.randint(10, 100)/100))
    if random_run_away_probability():
        all_widgets_dict['Event Bar'].config(text=f"Run away from {foe['Name']}")
        all_widgets_dict['Script Frame'].children['script_display'].config(text="Run away", anchor="center", compound="center")
    else:
        damage_taken(game_info, all_widgets_dict, foe_attack)
        all_widgets_dict['Event Bar'].config(text=f"Failed to escape!")
    var.set(True)
