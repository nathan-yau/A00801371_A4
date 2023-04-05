from GUI.homepage import create_homepage


def main():
    """
    Drive the program.
    """
    game_gui = create_homepage()
    game_gui['GUI'].mainloop()


if __name__ == "__main__":
    main()
