import random
import itertools


def make_environment_attributes(columns, rows) -> dict:
    special_events = [('BOSS', 'General Havoc'), ('BOSS', 'Sage Thorne'), ('ITEM', 'The Amulet of Knowledge')]
    special_places = [(1, 0), (4, 2), (4, 0)]
    resource_list = [('ITEM', 'Healing Potion'), ('ITEM', 'Status Potion'), ('ITEM', 'Attribute Potion'),
                     ('ITEM', 'Status Potion'), ('ITEM', 'Healing Potion'), ('ITEM', 'Attribute Potion'),
                     ('ITEM', 'Attribute Potion')]

    def create_items_locations():
        for item in resource_list:
            special_events.append(item)
            special_places.append(roll_location())

    def roll_location() -> tuple:
        while (place := (random.randint(0, columns-1), random.randint(0, rows-1))) in special_places:
            continue
        return place

    def fill_empty_location():
        for room in list(itertools.product(range(columns), range(rows))):
            if room not in special_places:
                special_events.append(('RANDOM',''))
                special_places.append(room)

    create_items_locations()
    fill_empty_location()
    overall_dict = dict(zip(special_places, special_events))
    return overall_dict


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
