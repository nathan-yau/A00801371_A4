from functools import partial

from new_game.new_player import create_character
from GUI.create_widgets import create_click_button, create_text_label, create_image_label, attach_button_function_call
from save_load.load_game_file import load_file
from utilities.initialize_game import load_into_game
import inspect


def new_player_page(name, interface_frames):
    """
    Create a GUI page for creating a new player.

    :postcondition: create a GUI page for creating a new player
    """
    character_attribute = [{}]
    main_frame = interface_frames['Top Frame']
    interface_frames['Event Bar'].config(text="Creating New User - " + name)
    for widget in main_frame.winfo_children():
        widget.destroy()
    print([stack[3] for stack in inspect.stack()])

    def create_player_image():
        """
        Create an image label on the left side of the GUI as a player icon.

        :postcondition: create an image label on the left side of the GUI as a player icon
        """
        create_image_label(main_frame, "player_icon", "./images/player_icon.png")
        main_frame.children['player_icon'].grid(row=0, column=0, rowspan=4, ipady=120)

    def generate_attribute_text(random_attribute):
        """
        Generate some random generated attributes for the new player.

        :postcondition: generate some random generated attributes for the new player
        :return: a string that shows the generated attributes for the new player except for
                 character name, experience point, current hp and mp
        """
        display_message = ""
        for key, value in random_attribute.items():
            if key not in list(random_attribute.keys())[2:-6]:
                display_message += f"{str(key): <16}{str(value): >18}\n"
        return display_message

    def create_attribute_label(attribute):
        """
        Display some random generated attributes for the new player on the GUI as a label widget.

        :postcondition: display some random generated attributes for the new player on the GUI as a label widget
        """
        create_text_label(frame=main_frame, widget_name="attribute_label", message=attribute,
                          font_style="Cascadia Code", font_size=15, justify="left")
        main_frame.children['attribute_label'].grid(row=0, column=1, rowspan=4)

    def display_attribute():
        """
        Update some random generated attributes for the new player on the GUI as a label widget.

        :postcondition: update some random generated attributes for the new player on the GUI as a label widget
        """
        character_attribute.pop(0)
        generated_attributes = create_character(name)
        display_message = generate_attribute_text(generated_attributes)
        create_attribute_label(display_message)
        character_attribute.append(generated_attributes)
        print([stack[3] for stack in inspect.stack()])

    def attribute_buttons():
        """
        Create regenerate, accept and cancel buttons for user to interact with the randomly generated attributes.

        :postcondition: create regenerate, accept and cancel buttons for user to interact
                        with the randomly generated attributes
        """
        new_player_button = {'Regenerate': display_attribute,
                             'Accept': partial(load_into_game, interface_frames, character_attribute[-1]),
                             'Load Save': partial(load_file, interface_frames)}
        for index, (key, value) in enumerate(new_player_button.items()):
            button_name = key.lower().replace(" ", "_")
            create_click_button(frame=main_frame, widget_name=button_name, message=key)
            attach_button_function_call(button_name=main_frame.children[button_name],
                                        callable_function=value)
            main_frame.children[button_name].grid(row=index, column=3, sticky='e', ipady=20, pady=50, padx=(50, 0))

    create_player_image()
    display_attribute()
    attribute_buttons()
    print([stack[3] for stack in inspect.stack()])
