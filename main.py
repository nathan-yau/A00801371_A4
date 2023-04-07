from GUI.homepage import create_homepage
from playsound import playsound


def main():
    """
    Drive the program.
    """
    playsound('./music/default.mp3', block=False)
    game_gui = create_homepage()
    game_gui['GUI'].mainloop()


if __name__ == "__main__":
    main()
