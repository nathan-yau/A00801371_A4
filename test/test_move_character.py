from unittest import TestCase
from events.movement import move_character


class TestMoveCharacter(TestCase):

    def test_when_game_player_is_not_dict(self):
        with self.assertRaises(TypeError):
            current_spot = ["X-coordinate", "Y-coordinate"]
            move_character(current_spot, 1)

    def test_when_game_player_does_not_have_x_coordinate_key(self):
        with self.assertRaises(TypeError):
            current_spot = {"Y-coordinate": 1}
            move_character(current_spot, 1)

    def test_when_game_player_does_not_have_y_coordinate_key(self):
        with self.assertRaises(TypeError):
            current_spot = {"X-coordinate": 4}
            move_character(current_spot, 1)

    def test_when_path_is_not_an_integer(self):
        with self.assertRaises(ValueError):
            current_spot = {"X-coordinate": 1, "Y-coordinate": 1}
            move_character(current_spot, "abc")

    def test_when_path_is_a_negative_integer(self):
        with self.assertRaises(ValueError):
            current_spot = {"X-coordinate": 1, "Y-coordinate": 1}
            move_character(current_spot, -123)

    def test_when_path_is_zero(self):
        with self.assertRaises(ValueError):
            current_spot = {"X-coordinate": 1, "Y-coordinate": 1}
            move_character(current_spot, 0)

    def test_when_path_is_a_float(self):
        with self.assertRaises(ValueError):
            current_spot = {"X-coordinate": 1, "Y-coordinate": 1}
            move_character(current_spot, 1.23)

    def test_when_path_is_greater_than_4(self):
        with self.assertRaises(ValueError):
            current_spot = {"X-coordinate": 1, "Y-coordinate": 1}
            move_character(current_spot, 5)

    def test_move_character_left(self):
        current_location = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(current_location, 1)
        expected_location = {"X-coordinate": 0, "Y-coordinate": 1}
        self.assertEqual(expected_location, current_location)

    def test_move_character_right(self):
        current_position = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(current_position, 2)
        expected_position = {"X-coordinate": 2, "Y-coordinate": 1}
        self.assertEqual(expected_position, current_position)

    def test_move_character_up(self):
        character_in_game = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(character_in_game, 3)
        expected = {"X-coordinate": 1, "Y-coordinate": 0}
        self.assertEqual(expected, character_in_game)

    def test_move_character_down(self):
        current_coordinate = {"X-coordinate": 1, "Y-coordinate": 1}
        move_character(current_coordinate, 4)
        expected_coordinate = {"X-coordinate": 1, "Y-coordinate": 2}
        self.assertEqual(expected_coordinate, current_coordinate)