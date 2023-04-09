from unittest import TestCase
from unittest.mock import patch
from events.movement import key_validate_move
import io


class Test(TestCase):
    encoded_required_item = "01230040004800440052004100580032003400790097011501050115003200690120011201080111011401" \
                            "01011400340044003200400049004400500041005800320034008300970110009901160117010900320075" \
                            "0101012100340125"

    incorrect_encode_item = "00910040004800440052004100440032003400790097011501050115003200690120011201080111011401" \
                            "01011400340044003200400049004400500041004400320034008300970110009901160117010900320075" \
                            "0101012100340093"

    def test_when_avatar_is_not_dict(self):
        with self.assertRaises(FileNotFoundError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            key_validate_move("FileNotFound.txt", character, {"Sanctum Key": 1})

    @patch('builtins.open', return_value=io.StringIO(encoded_required_item))
    def test_when_item_is_not_dict(self, _):
        with self.assertRaises(TypeError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            key_validate_move("test_key_validate_move.py", character, [])

    @patch('builtins.open', return_value=io.StringIO(encoded_required_item))
    def test_when_character_is_not_dict(self, _):
        with self.assertRaises(TypeError):
            key_validate_move("test_key_validate_move.py", [], {"Sanctum Key": 1})

    @patch('builtins.open', return_value=io.StringIO(encoded_required_item))
    def test_when_both_next_move_and_items_are_not_dict(self, _):
        with self.assertRaises(TypeError):
            key_validate_move("test_key_validate_move.py", [], [])

    @patch('builtins.open', return_value=io.StringIO(incorrect_encode_item))
    def test_when_decoded_message_is_not_a_dict(self, _):
        with self.assertRaises(TypeError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            key_validate_move("test_key_validate_move.py", character, {"Sanctum Key": 1})

    @patch('builtins.open', return_value=io.StringIO(encoded_required_item))
    def test_item_found_in_item_bag_but_not_in_the_designated_location(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        self.assertTrue(key_validate_move("test_key_validate_move.py", character, {"Sanctum Key": 1}))

    @patch('builtins.open', return_value=io.StringIO(encoded_required_item))
    def test_location_found_in_decoded_message_but_without_required_item(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 2}
        self.assertFalse(key_validate_move("test_key_validate_move.py", character, {"Not a Key": 1}))

    @patch('builtins.open', return_value=io.StringIO(encoded_required_item))
    def test_item_not_found_in_item_bag_also_not_in_the_designated_location(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        self.assertTrue(key_validate_move("test_key_validate_move.py", character, {"Not a Key": 1}))

    @patch('builtins.open', return_value=io.StringIO(encoded_required_item))
    def test_location_found_in_decoded_message_but_with_required_item(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 2}
        self.assertTrue(key_validate_move("test_key_validate_move.py", character, {"Sanctum Key": 1}))
