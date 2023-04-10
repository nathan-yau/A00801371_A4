import pathlib
from GUI import GAME_MAP_PATH
from GUI.create_widgets import update_image_label


def map_widget_update(avatar: dict, overall_frames: dict, map_path: str = GAME_MAP_PATH) -> None:
    """
    Update the game map on the GUI based on the player's current position.

    :param avatar: a dictionary containing keys named as ['X-coordinate'] and ['Y-coordinate'],
                   each of which has a value representing the current coordinate of the player in the game map.
    :param overall_frames: a dictionary containing keys named as ['Event Bar'] and ['Status Frame'],
                           which represents a tkinter Label widget and tkinter Frame widget
    :param map_path: a file path referring to the game map image
    :precondition: avatar must be a dictionary
    :precondition: avatar must contain keys named as ['X-coordinate'] and ['Y-coordinate']
    :precondition: the values of ['X-coordinate'] and ['Y-coordinate'] must be an integer value
    :precondition: overall_frames must be a dictionary
    :precondition: overall_frames must contain key named as ['Event Bar']
    :precondition: the value of ['Event Bar'] must be a tkinter Label widget
    :precondition: the value of ['Status Frame'] must be a tkinter Frame widget
    :precondition: the Frame represented by ['Status Frame'] must contain a label called current_map
    :precondition: map_path must be a file path referring to the game map image
    :postcondition: update the game map on the GUI based on the player's current position
    :raises KeyError: if avatar does not contain keys named as ['X-coordinate'] and ['Y-coordinate']
                      if overall_frames does not contain keys named as ['Event Bar'] and ['Status Frame']
                      if ['Status Frame'] does not contain a label called current_map
    :raises TypeError: if avatar and/or overall_frames is not dictionary
    :raises FileNotFoundError: if game map image cannot be found
    """
    coordinate = str(avatar["X-coordinate"])+str(avatar["Y-coordinate"])
    if pathlib.Path(map_path.format(coordinate)).is_file():
        update_image_label(frame_object=overall_frames['Status Frame'], label_name="current_map",
                           image_directory=map_path.format(coordinate))
        overall_frames['Event Bar'].config(text=f"Current Coordinate - {str(avatar['X-coordinate'])}, "
                                                f"{str(avatar['Y-coordinate'])}")
    else:
        raise FileNotFoundError("Game map image cannot be found! Please check the path!")


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
