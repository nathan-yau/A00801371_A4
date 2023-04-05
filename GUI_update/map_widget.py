import pathlib
import tkinter as tk
from GUI import GAME_MAP_PATH


def map_widget_update(avatar, overall_frames):
    coordinate = str(avatar["X-coordinate"])+str(avatar["Y-coordinate"])
    if pathlib.Path(GAME_MAP_PATH.format(coordinate)).is_file():
        map_image = tk.PhotoImage(file=GAME_MAP_PATH.format(coordinate))
        overall_frames['Status Frame'].children['current_map'].config(image=map_image)
        overall_frames['Status Frame'].children['current_map'].image = map_image
        overall_frames['Event Bar'].config(text=f"Current Coordinate - {str(avatar['X-coordinate'])}, "
                                                f"{str(avatar['Y-coordinate'])}")
    else:
        overall_frames['Event Bar'].config(text="Invalid Move!")
