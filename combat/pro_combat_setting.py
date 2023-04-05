import random
from GUI import DEFAULT_FONT


def battle_end_widget_update(gui_widgets_all, game_info, picked_foe):
    if game_info['character']['Current HP'] > 0 >= picked_foe['HP']:
        if random.randint(0, 1000) == 1:
            picked_foe['EXP'] *= 12
            gui_widgets_all['Script Frame'].children['script_display'].\
                config(text='Wow! Defeating it granted you an unexpected surge of experience points.',
                       font=(DEFAULT_FONT, 8))
        else:
            game_info['character']['EXP'] += picked_foe['EXP']
            gui_widgets_all['Script Frame'].children['script_display'].config(text='Won')

    else:
        gui_widgets_all['Script Frame'].children['script_display'].config(text='Escaped the fight! '
                                                                               'Live to fight another day',
                                                                          font=(DEFAULT_FONT, 8))

