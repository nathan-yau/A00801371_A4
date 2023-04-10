# 1510-Assignment-04

Every program needs a README.md

This is written in markdown. Read about markdown here: [markdowncheatsheet](https://www.markdownguide.org/cheat-sheet/)

## Your name:
Nathan Yau

## Your student number:
A00801371

## Your GitHub account ID:
nathan-yau

## Any important comments you'd like to make about your work:

## Oasis of the Lost Adventure

### Scenario

Welcome to the world of Oasis of the Lost Adventure, an adventure game that will take you on a journey through a 
mystical land. In this game, you will play the role of an adventurer 
who is driven by a burning desire to uncover the mysteries of the lost city's Sanctum.

### Goal

In this game, your goal is to enter the Sanctum and defeat the final boss that guards the Sanctum.

### How to Play


#### Movement: 

Use keyword (A, W, S, D) or click buttons on GUI to move your character around the 5x5 game board. 

A - Move Left | D - Move Right

W - Move Up | S - Move Down

You will encounter different obstacles and enemies on your way to the Sanctum.

#### Searching: 

Look out for hidden treasures along the way. 

Use the search button to explore the surrounding areas and discover items that can help you on your journey.

#### Combat: 

When you encounter an enemy, use your "physical attack" and "magic attack" buttons to defeat them. 

Some enemies will be immune to physical attacks, while others will be immune to magic attacks.


#### Potions:

You can use different types of potions to heal yourself or increase your attributes:
- Healing Potion: Restores 50 health points. 
- Status Potion: Restores your status back to healthy. 
- Attribute Potion: Randomly increases one of your attributes by 5 to 20 points.

### Attributes:
Your character has five attributes: 
- "Strength", "Dexterity", "Intelligence", "Magic Power", "Magic Resistance", and "Intelligence". 

These attributes determine your character's combat skills, maximum HP and maximum MP to navigate through obstacles.

You can increase your attributes by using attribute potions or leveling up.

#### Leveling up:

You will gain experience points (EXP) for defeating enemies.

As you accumulate EXP, you will level up, which will increase your attributes and restore your status to full health.

#### Quests: 

Along the way, you will encounter a NPC who will offer you quests to complete. 

This quest will reward you with a valuable item.

## Mandatory Elements Table

| Mandatory Elements                                         | Function(s)                                                                                                 | Line             |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|------------------|
| Docstrings                                                 | Completed for each functions                                                                                |                  |
| Doctests                                                   | Completed for all functions, except for those that use the <br/>random or tkinter module                    |                  |
| Unit tests                                                 | Completed for all functions under test package, except for those that use tkinter module                    |                  |
| 5 x 5 grid-based environment                               | Module new_environment.py under new_game package                                                            | Line 67          |
| Gameplay ends correctly                                    | Module game_ending.py under events package                                                                  |                  |
| Character movement and  restrictions on character movement | Module movements.py under events package                                                                    |                  |
| Ecosystem of challenges                                    | Module item_events.py under events package<br/>Module combat_actions and combat_result under combat package |                  |
| Immutable data structures                                  | Function make_environment_attributes() inside Module new_environment.py under new_game package              | Line 67          |
| Mutable data structures                                    | Function player_movement() inside Module movement.py under events package                                   | Line 193         |
| Error Handling                                             | Function create_text_label() inside Module create_widgets.py under GUI package                              | Line 72 - 75     |
| Minimized scope of all variables                           | Function pick_available_foe() inside Module event_checker.py under events package                           | Line 65 - 66     |  
| Decomposition                                              | Decomposed move validation into three functions inside Module movements.py under events package             | Line 44, 79, 117 |
| Flat code                                                  | Function game() inside Module gameplay.py under events package                                              | Line 20          |
| Comprehensions                                             | Function check_if_alive() inside Module player_info.py under combat package                                 | Line 173         |
| If-statement                                               | Function create_save_file() inside Module save_game_file.py under save_load package                         | Line 18          |
| Repetition                                                 | Function level_up() inside Module player_info.py under combat package                                       | Line 36          |
| Membership operation                                       | Function damage_calculator() inside Module combat_actions.py under combat package                           | Line 31          |
| Range function                                             | Function decoder() inside Module uid_converter.py under save_load package                                   | Line 20          |
| Functions from itertools                                   | Function make_environment_attributes() inside Module new_environment.py under new_game package              | Line 67          |
| Random Module                                              | Function random_run_away_probability() inside Module combat_actions.py under combat package                 | Line 128         |
| Function Annotations                                       | Function encoder() inside Module uid_converter.py under save_load package                                   | Line 25          | 
| f-strings                                                  | Function load_into_game() inside Module initialize_game.py under utilities package                          | Line 36          | 
