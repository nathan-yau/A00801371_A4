import random
import itertools
from save_load.uid_converter import decoder
from GUI import NEW_GAME_DATA_PATH


def make_environment_attributes(columns: int, rows: int, game_data: str = NEW_GAME_DATA_PATH) -> dict:
    """
    Create a dictionary that represents a game environment and the predetermined event in each room of a given
    column x row board.

    :param game_data: a string that refers to the path of the encoded game date needed for generating new environment
    :param columns: an integer value that must be greater than or equal to 2
    :param rows: an integer value that must be greater than or equal to 2
    :precondition: game_date must be a string that refers to the path of the encoded game date
                   needed for generating new environment
    :precondition: columns must be an integer value that must be greater than or equal to 2
    :precondition: rows must be an integer value that must be greater than or equal to 2
    :postcondition: create a dictionary that represents a game environment and the predetermined event in
                    each room of a given column x row board
    :return: a dictionary with tuples of (x, y) coordinates as keys and tuples of event categories and events as values
    :raises ValueError: if columns and/or rows is less than 2
    :raises FileNotFoundError: if file represented by game_data cannot be found in the directory
    :raise TypeError: if game_data is not a string
    """
    def create_items_locations() -> None:
        """
        Add the locations of resources to the list of special places and corresponding events to
        the list of special events.

        :precondition: special_events and special_places must exist in the outer function
        :postcondition: append item from resource_list to special_events and its corresponding
                        location to special_places
        :raises NameError: if special_events and special_places do not exist in the outer function
        :raises AttributeError: if special_events and special_places are not list
        """
        for item in resource_dict['resource_list']:
            resource_dict['special_events'].append(item)
            resource_dict['special_places'].append(roll_location())

    def roll_location() -> tuple:
        """
        Randomly select an unused location represented by a tuple of coordinate (x, y) inside a given column x row board

        :precondition: special_places must exist in the outer function
        :postcondition: randomly select an unused location represented by a tuple of coordinate (x, y) from
                        special_places inside a given column x row board
        :raises NameError: if special_places does not exist in the outer function
        :raises AttributeError: if special_events and special_places are not list
        """
        while (place := (random.randint(0, columns-1), random.randint(0, rows-1))) in resource_dict['special_places']:
            continue
        return place

    def fill_empty_location() -> None:
        """
        Append a tuple of coordinates (x, y) representing unassigned locations on a given column x row board
        to special_places, along with an empty event tuple in special_events.

        :precondition: special_events and special_places must exist in the outer function
        :postcondition: append empty event tuple to special_events and its corresponding
                        location to special_places
        :raises NameError: if special_events and special_places do not exist in the outer function
        :raises AttributeError: if special_events and special_places are not list
        """
        for room in list(itertools.product(range(columns), range(rows))):
            if room not in resource_dict['special_places']:
                resource_dict['special_events'].append(('RANDOM', ''))
                resource_dict['special_places'].append(room)

    if type(columns) is not int or type(rows) is not int or columns < 2 or rows < 2:
        raise ValueError("Columns and Rows must be an integer greater than or equal to 2.")
    if type(game_data) is not str:
        raise TypeError("game_data must be a string that refers to the path of the new game data.")
    with open(game_data) as obj:
        resource_dict = eval(decoder(obj.read()))
    create_items_locations()
    fill_empty_location()
    overall_dict = dict(zip(resource_dict['special_places'], resource_dict['special_events']))
    return overall_dict


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
