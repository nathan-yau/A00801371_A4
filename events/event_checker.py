import random


def encounter_confirmation(event_name, game_info):
    if event_name == "FINAL-BOSS":
        return 'Sanctum Key' in game_info['character']['Items']
    elif event_name == 'MID-BOSS':
        return 'The Amulet of Knowledge' in game_info['character']['Items']
    elif event_name == 'RANDOM':
        return random.randint(1, 10) <= 3
    else:
        return False


def check_for_predetermined_events(game_player):
    avatar = game_player['character']
    current_coordinate = (avatar["X-coordinate"], avatar["Y-coordinate"])
    predetermined_events = game_player['environment'][current_coordinate][1]
    if current_coordinate in game_player['environment']:
        key_encounter = "RANDOM" if not predetermined_events else predetermined_events
        return key_encounter
    else:
        raise KeyError("Invalid datapoint! Reload last save to continue!")


def pick_available_foe(happened_event, max_level_foe):
    sample_monster = {
        1: {'Name': 'Megalizard', 'EXP': 20, 'HP': 50, 'Items': ['Healing Potion'], 'PROBABILITY': 30, 'Strength': 23, 'Dexterity': 5,
            'Intelligence': 20, 'Magic Resistance': 999},
        2: {'Name': 'Skeletons ', 'EXP': 30, 'HP': 70, 'Items': ['Healing Potion'], 'PROBABILITY': 30, 'Strength': 25, 'Dexterity': 10,
            'Intelligence': 25, 'Magic Resistance': 26},
        3: {'Name': 'Venomweaver', 'EXP': 40, 'HP': 80, 'Items': ['Status Potion'], 'PROBABILITY': 30, 'Strength': 30, 'Dexterity': 30,
            'Intelligence': 30, 'Magic Resistance': 40},
        4: {'Name': 'Hydra', 'EXP': 80, 'HP': 100, 'Items': ['Healing Potion'], 'PROBABILITY': 30, 'Strength': 37, 'Dexterity': 50,
            'Intelligence': 46, 'Magic Resistance': 999},
        5: {'Name': 'Griffin', 'EXP': 100, 'HP': 120, 'Items': ['Attribute Potion'], 'PROBABILITY': 30, 'Strength': 37, 'Dexterity': 50,
            'Intelligence': 46, 'Magic Resistance': 26}}
    if happened_event == "RANDOM":
        picked_foe = random.randint(1, min(max_level_foe, len(sample_monster)))
        sample_monster[picked_foe]['EXP'] = int(random.uniform(1, 2) * sample_monster[picked_foe]['EXP'])
        return sample_monster[picked_foe]
    elif happened_event == "MID-BOSS":
        return {'Name': 'MID-BOSS', 'EXP': 500, 'HP': 80, 'Items': ['Sanctum Key'], 'PROBABILITY': 100, 'Strength': 30, 'Dexterity': 30,
                'Intelligence': 30, 'Magic Resistance': 40}
    elif happened_event == "FINAL-BOSS":
        return {'Name': 'FINAL-BOSS', 'EXP': 500, 'HP': 80, 'Items': ['Oasis Explorer'], 'PROBABILITY': 100, 'Strength': 30,
                'Dexterity': 30, 'Intelligence': 30, 'Magic Resistance': 40}
    else:
        return {}
