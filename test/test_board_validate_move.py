from unittest import TestCase
from events.movement import board_validate_move


class Test(TestCase):

    def test_when_next_move_is_not_dict(self):
        with self.assertRaises(TypeError):
            board_layout = {(0, 0): "Room 1", (0, 1): "Room 2", (1, 0): "Room 3", (1, 1): "Room 4"}
            player = ["X-coordinate", "Y-coordinate"]
            board_validate_move(player, board_layout)

    def test_when_environment_is_not_dict(self):
        with self.assertRaises(TypeError):
            game_layout = [(0, 0), (0, 1), (1, 0), (1, 1)]
            avatar_in_game = {"X-coordinate": 0, "Y-coordinate": 0}
            board_validate_move(avatar_in_game, game_layout)

    def test_when_both_next_move_and_environment_is_not_dict(self):
        with self.assertRaises(TypeError):
            game_layout = [(0, 0), (0, 1), (1, 0), (1, 1)]
            player_in_game = ["X-coordinate", "Y-coordinate"]
            board_validate_move(player_in_game, game_layout)

    def test_player_s_desired_location_is_valid_on_board(self):
        game_board_layout = {(0, 0): "Room 1", (0, 1): "Room 2", (1, 0): "Room 3", (1, 1): "Room 4"}
        avatar_in_game = {"X-coordinate": 0, "Y-coordinate": 0}
        self.assertTrue(board_validate_move(avatar_in_game, game_board_layout))

    def test_player_s_desired_location_is_not_valid_on_board(self):
        board = {(0, 0): "Room 1", (0, 1): "Room 2", (1, 0): "Room 3", (1, 1): "Room 4"}
        avatar = {"X-coordinate": 2, "Y-coordinate": 0}
        self.assertFalse(board_validate_move(avatar, board))
