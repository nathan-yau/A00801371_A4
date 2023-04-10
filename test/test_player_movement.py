from unittest import TestCase
from events.movement import player_movement
from unittest.mock import patch


class PlayerMovementTest(TestCase):

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_game_player_is_not_dict(self, _, __, ___, ____):
        with self.assertRaises(TypeError):
            player_info = []
            result = player_movement(player_info, 1, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_missing_character_in_game_player(self, _, __, ___, ____):
        with self.assertRaises(KeyError):
            player_info = {'environment': {}}
            result = player_movement(player_info, 1, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_missing_environment_in_game_player(self, _, __, ___, ____):
        with self.assertRaises(KeyError):
            player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}}
            result = player_movement(player_info, 1, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_x_coordinate_in_character_of_game_player(self, _, __, ___, ____):
        with self.assertRaises(KeyError):
            player_info = {'character': {'Z-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
            result = player_movement(player_info, 1, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_y_coordinate_in_character_of_game_player(self, _, __, ___, ____):
        with self.assertRaises(KeyError):
            player_info = {'character': {'X-coordinate': 1, 'Z-coordinate': 1, 'Items': []}, 'environment': {}}
            result = player_movement(player_info, 1, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_item_in_character_of_game_player(self, _, __, ___, ____):
        with self.assertRaises(KeyError):
            player_info = {'character': {'X-coordinate': 1, 'y-coordinate': 1, 'Item': []}, 'environment': {}}
            result = player_movement(player_info, 1, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_heading_is_zero(self, _, __, ___, ____):
        with self.assertRaises(ValueError):
            player_info = {'character': {'X-coordinate': 1, 'y-coordinate': 1, 'Items': []}, 'environment': {}}
            result = player_movement(player_info, 0, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_heading_is_greater_than_4(self, _, __, ___, ____):
        with self.assertRaises(ValueError):
            player_info = {'character': {'X-coordinate': 1, 'y-coordinate': 1, 'Items': []}, 'environment': {}}
            result = player_movement(player_info, 5, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_heading_is_negative(self, _, __, ___, ____):
        with self.assertRaises(ValueError):
            player_info = {'character': {'X-coordinate': 1, 'y-coordinate': 1, 'Items': []}, 'environment': {}}
            result = player_movement(player_info, -15, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_heading_is_floating_point(self, _, __, ___, ____):
        with self.assertRaises(ValueError):
            player_info = {'character': {'X-coordinate': 1, 'y-coordinate': 1, 'Items': []}, 'environment': {}}
            result = player_movement(player_info, 1.2345, {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_heading_is_string(self, _, __, ___, ____):
        with self.assertRaises(ValueError):
            player_info = {'character': {'X-coordinate': 1, 'y-coordinate': 1, 'Items': []}, 'environment': {}}
            result = player_movement(player_info, "15", {})
            self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_three_criteria_all_valid(self, _, __, ___, ____):
        player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
        result = player_movement(player_info, 1, {})
        self.assertTrue(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=False)
    @patch("events.movement.key_validate_move", return_value=False)
    @patch("events.movement.display_invalid_move_reason")
    def test_board_checking_valid(self, _, __, ___, ____):
        player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
        result = player_movement(player_info, 1, {})
        self.assertFalse(result)

    @patch("events.movement.board_validate_move", return_value=False)
    @patch("events.movement.route_validate_move", return_value=False)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_required_item_checking_valid(self, _, __, ___, ____):
        player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
        result = player_movement(player_info, 1, {})
        self.assertFalse(result)

    @patch("events.movement.board_validate_move", return_value=False)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=False)
    @patch("events.movement.display_invalid_move_reason")
    def test_route_checking_valid(self, _, __, ___, ____):
        player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
        result = player_movement(player_info, 1, {})
        self.assertFalse(result)

    @patch("events.movement.board_validate_move", return_value=False)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_route_and_key_checking_valid(self, _, __, ___, ____):
        player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
        result = player_movement(player_info, 1, {})
        self.assertFalse(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=False)
    @patch("events.movement.key_validate_move", return_value=True)
    @patch("events.movement.display_invalid_move_reason")
    def test_board_and_required_item_checking_valid(self, _, __, ___, ____):
        player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
        result = player_movement(player_info, 1, {})
        self.assertFalse(result)

    @patch("events.movement.board_validate_move", return_value=True)
    @patch("events.movement.route_validate_move", return_value=True)
    @patch("events.movement.key_validate_move", return_value=False)
    @patch("events.movement.display_invalid_move_reason")
    def test_board_and_route_checking_valid(self, _, __, ___, ____):
        player_info = {'character': {'X-coordinate': 1, 'Y-coordinate': 1, 'Items': []}, 'environment': {}}
        result = player_movement(player_info, 1, {})
        self.assertFalse(result)
