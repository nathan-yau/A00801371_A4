
def enemy_status(player_info):
    character_status = "Enemy Information\n\n"
    keys_print = set(list(player_info.keys())[:3])
    for key, value in player_info.items():
        if key not in keys_print:
            continue
        character_status += f"{key:<6}{value:>12}\n"
    return character_status.rstrip()
