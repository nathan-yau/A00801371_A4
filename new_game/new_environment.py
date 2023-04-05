import random
import itertools


def make_environment_attributes(columns, rows) -> dict:
    special_events = [('BOSS', 'FINAL-BOSS'), ('BOSS', 'MID-BOSS')]
    special_places = [(1, 0), (4, 2)]
    resource_list = [('ITEM', 'HEALING POTIONS'), ('ITEM','STATUS POTIONS'), ('ITEM','ATTRIBUTE POTION'),
                     ('ITEM', 'STATUS POTIONS'), ('ITEM', 'HEALING POTIONS'), ('ITEM','ATTRIBUTE POTION'),
                     ('ITEM', 'ATTRIBUTE POTION')]

    def create_items_locations():
        for item in resource_list:
            special_events.append(item)
            special_places.append(roll_location())

    def roll_location() -> tuple:
        while (place := (random.randint(0, columns-1), random.randint(0, rows-1))) in special_places:
            continue
        return place

    def fill_empty_location() -> list:
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
