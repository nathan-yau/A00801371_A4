from unittest import TestCase
from new_game.new_player import create_character
from unittest.mock import patch


class CreateCharacterTest(TestCase):

    def test_non_string_value_for_name(self):
        with self.assertRaises(TypeError):
            create_character(12345)

    def test_empty_string_for_name(self):
        with self.assertRaises(TypeError):
            create_character("")

    @patch("random.uniform", return_value=1.5)
    @patch("random.randint", side_effect=[30, 30, 30, 30, 30])
    def test_create_min_value_character(self, _, __):
        expected = {'Name': 'Nathan', 'Level': 1, 'NEXT LV (EXP)': 90, 'Status': 'Healthy', 'X-coordinate': 4,
                    'Y-coordinate': 4, 'Items': {'Sanctum Key': 1}, 'Escape': False, 'Current HP': 60,
                    'Current MP': 60, 'Max HP': 60, 'Max MP': 60, 'Strength': 30, 'Dexterity': 30,
                    'Intelligence': 30, 'Magic Power': 30, 'Magic Resistance': 30}
        self.assertEqual(expected, create_character("Nathan"))

    @patch("random.uniform", return_value=1.5)
    @patch("random.randint", side_effect=[50, 50, 50, 50, 50])
    def test_create_max_value_character(self, _, __):
        expected = {'Name': 'Nathan', 'Level': 1, 'NEXT LV (EXP)': 90, 'Status': 'Healthy', 'X-coordinate': 4,
                    'Y-coordinate': 4, 'Items': {'Sanctum Key': 1}, 'Escape': False, 'Current HP': 100,
                    'Current MP': 100, 'Max HP': 100, 'Max MP': 100, 'Strength': 50, 'Dexterity': 50,
                    'Intelligence': 50, 'Magic Power': 50, 'Magic Resistance': 50}
        self.assertEqual(expected, create_character("Nathan"))
