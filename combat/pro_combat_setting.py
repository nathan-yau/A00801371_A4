import random
from GUI import DEFAULT_FONT


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

