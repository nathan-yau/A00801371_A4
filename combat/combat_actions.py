import random
from combat.player_info import check_if_alive


def damage_calculator(attack_type: str, attacker: dict, defender: dict) -> int:
    """
    Calculate the damage inflicted by a given attacker on a defender based on the attack type and their stats.

    :param attack_type: a string that is either 'magic' or 'physical'
    :param attacker: a dictionary containing keys named as ['Magic Power'], ['Strength'] and ['Current MP'],
                     each of which has an associated numeric value.
    :param defender: a dictionary containing keys named as ['Magic Resistance'] and ['Dexterity'],
                     each of which has an associated numeric value.
    :precondition: attack_type must a string that is either 'magic' or 'physical'
    :precondition: attacker must be a dictionary containing keys named as
                   ['Magic Power'], ['Strength'] and ['Current MP']
    :precondition: ['Magic Power'], ['Strength'] and ['Current MP'] keys from attacker
                   must have an associated numeric value
    :precondition: ['Magic Resistance'] and ['Dexterity'] keys from defender must have an associated numeric value
    :postcondition: calculate the damage inflicted by a given attacker on a defender
                    based on the attack type and their stats
    :return: a positive integer or zero representing the damage caused by an attacker to a defender
    :raise KeyError: if the keys ['Magic Power'], ['Strength'] and ['Current MP'] cannot be found inside attacker
                     if the keys ['Magic Resistance'], ['Dexterity'] cannot be found inside defender
    :raise TypeError: if the value of the keys ['Magic Power'], ['Strength'] and ['Current MP']
                      inside attacker is not number
                      if the value of the keys ['Magic Resistance'], ['Dexterity'] inside defender is not number
    :raise ValueError: if attack_type is a not string that containing either 'magic' or 'physical'
    """
    if type(attack_type) is not str or attack_type not in ["magic", "physical"]:
        raise ValueError("Attack Type must be a string that is either 'magic' or 'physical'")
    base_magic_damage = attacker['Magic Power'] * 2.0 - defender['Magic Resistance'] * 1.5
    magic_power_usage = min(random.randint(2, 8), attacker['Current MP'])
    basic_physical_damage = attacker['Strength'] * 2.0 - defender['Dexterity'] * 1.5
    if attack_type == "magic" and attacker['Current MP'] > 0:
        attacker['Current MP'] -= magic_power_usage
        return max(1, int(base_magic_damage * random.uniform(1.5, 1.9)))
    elif attack_type == "magic" and attacker['Current MP'] <= 0:
        return 0
    else:
        return max(1, int(basic_physical_damage * random.uniform(1.5, 1.9)))


def status_condition(player_info):
    """
    Randomly set the player's status to "Poisoned" with a probability of 1/6, otherwise it keeps the current status

    :param player_info: a dictionary containing key named as ['Status']
    :precondition: player_info must be a dictionary containing key named as ['Status']
    :postcondition: set the player's status to "Poisoned" with a probability of 1/6, or unchanged in other condition
    :raise KeyError: if the key ['Status'] cannot be found inside player_info
    """
    player_info['Status'] = "Poisoned" if random.randint(0, 5) == 1 else player_info['Status']


def attack(attack_type, player_info, all_widgets_dict, foe):
    """
    Update the label on event bar after reducing the player and the foe's health points

    :param attack_type: a string that is either 'magic' or 'physical'
    :param player_info: a dictionary containing keys named as ['Magic Resistance'], ['Dexterity'],
                        ['Magic Power'], ['Strength'] and ['Current MP'] and ['Current HP'],
                        each of which has an associated numeric value
    :param all_widgets_dict: a dictionary containing keys named as ['Event Bar'] and ['Script Frame'],
                     each of which has an associated tkinter Frame or Label
    :param foe: a dictionary containing keys named as ['Name'], ['HP'], ['Magic Resistance'], ['Dexterity'],
                ['Magic Power'], ['Strength'] and ['Current MP'], which has an associated value of
                string literal or numeric value
    :precondition: attack_type must a string that is either 'magic' or 'physical'
    :precondition: player_info must be a dictionary containing keys named as ['Magic Resistance'], ['Dexterity'],
                   ['Magic Power'], ['Strength'] and ['Current MP'] and ['Current HP']
    :precondition: all_widgets_dict must be a dictionary containing keys named as ['Event Bar'] and ['Script Frame'],
                   each of which has an associated tkinter Frame or Label
    :precondition: foe must be a dictionary containing keys named as ['Name'], ['HP'], ['Magic Resistance'],
                   ['Dexterity'], ['Magic Power'], ['Strength'] and ['Current MP'], which has an associated value of
                   string literal or numeric value
    :precondition: ['Magic Resistance'], ['Dexterity'], ['Magic Power'], ['Strength'] and ['Current MP'] keys
                   from player_info and foe must have an associated numeric value
    :precondition: ['Current HP'] key from player_info must have an associated numeric value
    :precondition: ['HP'] key from foe must have an associated numeric value
    :precondition: ['Name'] key from foe must have an associated numeric value
    :precondition: ['Event Bar'] key from all_widgets_dict must have an associated tkinter label as value
    :precondition: ['Script Frame'] key from all_widgets_dict must have an associated tkinter frame as value
    :postcondition: update the label on event bar after reducing the player and the foe's health points
    :raise KeyError: if the keys ['Event Bar'] and/or ['Script Frame'] cannot be found inside all_widgets_dict
                     if the keys ['Name'] and/or ['HP'] cannot be found inside foe
                     if the key ['Current HP'] cannot be found inside game_player_info
                     if the keys ['Magic Resistance', ['Dexterity'], ['Magic Power'], ['Strength'] and ['Current MP']
                     inside game_player_info and/or foe cannot be found
    :raise TypeError: if the value of the keys ['Magic Resistance', ['Dexterity'], ['Magic Power'], ['Strength'],
                      and ['Current MP'] inside attacker inside game_player_info and/or foe is not number
                      if the value of the keys ['Current HP'] inside game_player_info is not number
                      f the value of the keys ['HP'] inside foe is not number
    :raise ValueError: if attack_type is a not string that containing either 'magic' or 'physical'
    :raise AttributeError: if the value of the key ['Event Bar'] inside all_widgets_dict is not a tkinter label
                           if the value of the key ['Script Frame'] inside all_widgets_dict is not a tkinter frame
    """
    player_hit = damage_calculator(attack_type, player_info, foe)
    foe_hit = damage_calculator(random.sample(["magic", "physical"], 1), foe, player_info)
    status_condition(player_info)

    if random.randint(0, 1) == 0:
        foe['HP'] -= max(random.randint(1, 15), player_hit)
        player_info['Current HP'] -= max(random.randint(1, 15), foe_hit)
        check_if_alive(all_widgets_dict, player_info)
        all_widgets_dict['Event Bar'].config(text=f"Physical Attack {foe['Name']}!")
    else:
        all_widgets_dict['Event Bar'].config(text=f"{foe['Name']} Attack First!")
        player_info['Current HP'] -= max(random.randint(1, 15), foe_hit)
        check_if_alive(all_widgets_dict, player_info)
        foe['HP'] -= max(random.randint(1, 15), player_hit)

    all_widgets_dict['pause'].set(False)


def random_run_away_probability():
    """
    Return True with a probability of 1/3.

    :postcondition: return a Boolean Value representing whether player can run away from the battle
    :return: a Boolean Value representing whether player can run away from the battle
    """
    return random.randint(0, 2) == 0


def run_away(game_player_info, all_widgets_dict, foe):
    """
    Update the GUI displays and player's HP based on the success of the player's attempt to run away from the foe.

    :param game_player_info: a dictionary containing keys named as ['Escape'] and ['Current HP'],
                     each of which has an associated Boolean, or numeric value
    :param all_widgets_dict: a dictionary containing keys named as ['Event Bar'] and ['Script Frame'],
                     each of which has an associated tkinter Frame or Label
    :param foe: a dictionary containing keys named as ['Name'], which has an associated value of string literal
    :precondition: game_player_info must be a dictionary containing keys named as ['Escape'] and ['Current HP']
    :precondition: ['Current HP'] key from game_player_info must have an associated numeric value
    :precondition: all_widgets_dict must be a dictionary containing keys named as ['Event Bar'] and ['Script Frame'],
                   each of which has an associated tkinter Frame or Label
    :precondition: ['Event Bar'] key from all_widgets_dict must have an associated tkinter label as value
    :precondition: ['Script Frame'] key from all_widgets_dict must have an associated tkinter frame as value
    :precondition: foe must be a dictionary containing keys named as ['Name']
    :postcondition: update the GUI displays and player's HP based on the success of the player's
                    attempt to run away from the foe.
    :raise KeyError: if the keys ['Escape'] and ['Current HP'] cannot be found inside game_player_info
                     if the keys ['Event Bar'] and ['Script Frame'] cannot be found inside all_widgets_dict
                     if the keys ['Name'] cannot be found inside foe
    :raise TypeError: if the value of the key ['Current HP'] inside game_player_info is not a numeric value
    :raise AttributeError: if the value of the key ['Event Bar'] inside all_widgets_dict is not a tkinter label
                           if the value of the key ['Script Frame'] inside all_widgets_dict is not a tkinter frame
    """
    if random_run_away_probability():
        all_widgets_dict['Event Bar'].config(text=f"Run away from {foe['Name']}")
        all_widgets_dict['Script Frame'].children['script_display'].config(text="Run away", anchor="center")
        game_player_info['Escape'] = True
    else:
        foe_attack = damage_calculator(random.sample(["magic", "physical"], 1), foe, game_player_info)
        game_player_info['Current HP'] -= max(random.randint(1, 15), foe_attack)
        check_if_alive(all_widgets_dict, game_player_info)
        all_widgets_dict['Event Bar'].config(text=f"Failed to escape!")
    all_widgets_dict['pause'].set(False)
