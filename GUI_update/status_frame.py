def update_status_message(player_info):
    character_status = ""
    keys_to_skip = set(list(player_info.keys())[4:-6])
    for key, value in player_info.items():
        if key in keys_to_skip or key == "Name":
            continue
        if key == "Max HP":
            current_hp = max(player_info["Current HP"],0)
            value = f"{current_hp}/{value}"
            key = "Current HP"
        elif key == "Max MP":
            current_mp = max(player_info["Current MP"],0)
            value = f"{current_mp}/{value}"
            key = "Current MP"
        character_status += f"{key:<16}{value:>12}\n"
    return character_status.rstrip()
