from unittest import TestCase
from unittest.mock import patch

import combat.player_info
from combat.player_info import level_up


class Test(TestCase):

    @patch("combat.player_info.level_up_widget_update")
    @patch("random.uniform", return_value=1.5)
    @patch("random.randint", side_effect=[5, 5, 5, 5, 5])
    def test_no_level_up(self, _, __, ___):
        player_info = {'Name': 'Nathan Yau', 'Level': 1, 'NEXT LV (EXP)': 200, 'Status': 'Healthy', 'X-coordinate': 4,
                       'Y-coordinate': 4, 'Items': {'Sanctum Key': 1}, 'Escape': False, 'Current HP': 60,
                       'Current MP': 70, 'Max HP': 60, 'Max MP': 70, 'Strength': 32, 'Dexterity': 32,
                       'Intelligence': 31, 'Magic Power': 40, "Magic Resistance": 40}
        expected = {'Name': 'Nathan Yau', 'Level': 1, 'NEXT LV (EXP)': 200, 'Status': 'Healthy', 'X-coordinate': 4,
                    'Y-coordinate': 4, 'Items': {'Sanctum Key': 1}, 'Escape': False, 'Current HP': 60,
                    'Current MP': 70, 'Max HP': 60, 'Max MP': 70, 'Strength': 32, 'Dexterity': 32,
                    'Intelligence': 31, 'Magic Power': 40, 'Magic Resistance': 40}
        level_up({}, player_info)
        self.assertEqual(player_info, expected)

    @patch("combat.player_info.level_up_widget_update")
    @patch("random.uniform", return_value=1.5)
    @patch("random.randint", side_effect=[5, 5, 5, 5, 5])
    def test_level_up_by_one_level(self, _, __, ___):
        player_info = {'Name': 'Nathan Yau', 'Level': 1, 'NEXT LV (EXP)': -12, 'Status': 'Healthy', 'X-coordinate': 4,
                       'Y-coordinate': 4, 'Items': {}, 'Escape': False, 'Current HP': 60,
                       'Current MP': 70, 'Max HP': 60, 'Max MP': 70, 'Strength': 32, 'Dexterity': 32,
                       'Intelligence': 31, 'Magic Power': 40, "Magic Resistance": 40}
        expected = {'Name': 'Nathan Yau', 'Level': 2, 'NEXT LV (EXP)': 168, 'Status': 'Healthy', 'X-coordinate': 4,
                    'Y-coordinate': 4, 'Items': {}, 'Escape': False, 'Current HP': 70,
                    'Current MP': 80, 'Max HP': 70, 'Max MP': 80, 'Strength': 37, 'Dexterity': 37,
                    'Intelligence': 36, 'Magic Power': 45, 'Magic Resistance': 45}
        level_up({}, player_info)
        self.assertEqual(player_info, expected)

    @patch("combat.player_info.level_up_widget_update")
    @patch("random.uniform", return_value=1.5)
    @patch("random.randint", side_effect=[5, 5, 5, 5, 5])
    def test_level_up_by_one_level_with_0_as_next_lv_exp(self, _, __, ___):
        player_info = {'Name': 'Nathan Yau', 'Level': 1, 'NEXT LV (EXP)': 0, 'Status': 'Healthy', 'X-coordinate': 4,
                       'Y-coordinate': 4, 'Items': {}, 'Escape': False, 'Current HP': 60,
                       'Current MP': 70, 'Max HP': 60, 'Max MP': 70, 'Strength': 32, 'Dexterity': 32,
                       'Intelligence': 31, 'Magic Power': 40, "Magic Resistance": 40}
        expected = {'Name': 'Nathan Yau', 'Level': 2, 'NEXT LV (EXP)': 180, 'Status': 'Healthy', 'X-coordinate': 4,
                    'Y-coordinate': 4, 'Items': {}, 'Escape': False, 'Current HP': 70,
                    'Current MP': 80, 'Max HP': 70, 'Max MP': 80, 'Strength': 37, 'Dexterity': 37,
                    'Intelligence': 36, 'Magic Power': 45, 'Magic Resistance': 45}
        level_up({}, player_info)
        self.assertEqual(player_info, expected)

    @patch("combat.player_info.level_up_widget_update")
    @patch("random.uniform", return_value=1.5)
    @patch("random.randint", side_effect=[5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
    def test_level_up_by_multiple_levels(self, _, __, ___):
        player_info = {'Name': 'Nathan Yau', 'Level': 1, 'NEXT LV (EXP)': -400, 'Status': 'Healthy', 'X-coordinate': 4,
                       'Y-coordinate': 4, 'Items': {}, 'Escape': False, 'Current HP': 60,
                       'Current MP': 70, 'Max HP': 60, 'Max MP': 70, 'Strength': 32, 'Dexterity': 32,
                       'Intelligence': 31, 'Magic Power': 40, "Magic Resistance": 40}
        expected = {'Name': 'Nathan Yau', 'Level': 3, 'NEXT LV (EXP)': 50, 'Status': 'Healthy', 'X-coordinate': 4,
                    'Y-coordinate': 4, 'Items': {}, 'Escape': False, 'Current HP': 80, 'Current MP': 90,
                    'Max HP': 80, 'Max MP': 90, 'Strength': 42, 'Dexterity': 42, 'Intelligence': 41,
                    'Magic Power': 50, 'Magic Resistance': 50}
        level_up({}, player_info)
        self.assertEqual(player_info, expected)