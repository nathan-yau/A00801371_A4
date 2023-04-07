import random
from GUI import DEFAULT_FONT
from GUI_update.status_frame import update_status_message


def level_up(overall_gui_frame, game_info):
    player_info = game_info['character']
    if player_info['NEXT LV (EXP)'] <= 0:
        player_info['Level'] += 1
        player_info['NEXT LV (EXP)'] = int(player_info['Level']*60*(random.uniform(1.5, 1.9)))
        for attribute in ["Strength", "Dexterity", "Intelligence", "Magic Power"]:
            player_info[attribute] += random.randint(5, 15)
        player_info['Max HP'] = max(round(player_info['Strength'] + player_info['Intelligence'], -1), 60)
        player_info['Max MP'] = max(round(player_info['Dexterity'] + player_info['Magic Power'], -1), 60)
        player_info['Current HP'] = player_info['Max HP']
        player_info['Current MP'] = player_info['Max MP']
        overall_gui_frame['Status Frame'].children['character_status'].config(
            text=update_status_message(game_info['character']))
        overall_gui_frame['Script Frame'].children['script_display'].config(text='Level Up!')


def drop_item(gui_widgets_all, game_info, picked_foe):
    pass


def battle_end_widget_update(gui_widgets_all, game_info, picked_foe):
    if game_info['character']['Current HP'] > 0 >= picked_foe['HP']:
        if random.randint(1, 20) == 1:
            EXP = int(picked_foe['EXP'] * 1.5)
            game_info['character']['NEXT LV (EXP)'] -= EXP
            gui_widgets_all['Script Frame'].children['script_display'].\
                config(text=f'Wow! Defeating it granted you an unexpected surge of {EXP} experience points.',
                       font=(DEFAULT_FONT, 8))
        else:
            EXP = picked_foe['EXP']
            game_info['character']['NEXT LV (EXP)'] -= EXP
            gui_widgets_all['Script Frame'].children['script_display']. \
                config(text=f'Gained {EXP} experience points by defeating {picked_foe["Name"]}',
                       font=(DEFAULT_FONT, 8))
        gui_widgets_all['Status Frame'].children['character_status'].config(
            text=update_status_message(game_info['character']))
        level_up(gui_widgets_all, game_info)
    else:
        gui_widgets_all['Script Frame'].children['script_display'].config(text='Escaped the fight! '
                                                                               'Live to fight another day',
                                                                          font=(DEFAULT_FONT, 8))

