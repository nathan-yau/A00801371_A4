from unittest import TestCase
from unittest.mock import patch
from combat.player_info import level_up


class Test(TestCase):

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_player_info_being_non_dict_object(self, _):
        with self.assertRaises(TypeError):
            player = 12
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_key_error_with_no_level_key_in_game_player_info(self, _):
        with self.assertRaises(KeyError):
            player = {'NEXT LV (EXP)': -100, "Strength": 1, "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_key_error_with_no_next_lv_exp_key_in_game_player_info(self, _):
        with self.assertRaises(KeyError):
            player = {'Level': 1, "Strength": 1, "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_key_error_with_no_strength_in_game_player_info(self, _):
        with self.assertRaises(KeyError):
            player = {'Level': 1, "NEXT LV (EXP)": -100, "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_key_error_with_no_dexterity_in_game_player_info(self, _):
        with self.assertRaises(KeyError):
            player = {'Level': 1, "NEXT LV (EXP)": -100, "Strength": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_key_error_with_no_intelligence_in_game_player_info(self, _):
        with self.assertRaises(KeyError):
            player = {'Level': 1, "NEXT LV (EXP)": -100, "Strength": 1, "Dexterity": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_key_error_with_no_magic_resistance_in_game_player_info(self, _):
        with self.assertRaises(KeyError):
            player = {'Level': 1, "NEXT LV (EXP)": -100, "Strength": 1, "Dexterity": 1,
                      "Intelligence": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_key_error_with_no_magic_power_in_game_player_info(self, _):
        with self.assertRaises(KeyError):
            player = {'Level': 1, "NEXT LV (EXP)": -100, "Strength": 1, "Dexterity": 1,
                      "Intelligence": 1, "Magic Resistance": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_no_level_key_in_game_player_info(self, _):
        with self.assertRaises(TypeError):
            player = {'Level': "a", 'NEXT LV (EXP)': -100, "Strength": 1, "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_no_next_lv_exp_key_in_game_player_info(self, _):
        with self.assertRaises(TypeError):
            player = {'Level': 1, 'NEXT LV (EXP)': "a", "Strength": 1, "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_no_strength_in_game_player_info(self, _):
        with self.assertRaises(TypeError):
            player = {'Level': 1, 'NEXT LV (EXP)': -100, "Strength": "a", "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_no_dexterity_in_game_player_info(self, _):
        with self.assertRaises(TypeError):
            player = {'Level': 1, 'NEXT LV (EXP)': -100, "Strength": 1, "Dexterity": "a", "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_no_intelligence_in_game_player_info(self, _):
        with self.assertRaises(TypeError):
            player = {'Level': 1, 'NEXT LV (EXP)': -100, "Strength": 1, "Dexterity": 1, "Intelligence": "a",
                      "Magic Resistance": 1, "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_no_magic_resistance_in_game_player_info(self, _):
        with self.assertRaises(TypeError):
            player = {'Level': 1, 'NEXT LV (EXP)': -100, "Strength": 1, "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": "a", "Magic Power": 1}
            level_up({}, player)

    @patch("combat.player_info.level_up_widget_update")
    def test_type_error_with_no_magic_power_in_game_player_info(self, _):
        with self.assertRaises(TypeError):
            player = {'Level': 1, 'NEXT LV (EXP)': -100, "Strength": 1, "Dexterity": 1, "Intelligence": 1,
                      "Magic Resistance": 1, "Magic Power": "a"}
            level_up({}, player)

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
