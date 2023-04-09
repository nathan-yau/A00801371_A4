from unittest import TestCase
from new_game.new_player import status_reset


class StatusResetTest(TestCase):
    def test_when_player_info_is_not_dict(self):
        player_info = "Hello"
        with self.assertRaises(TypeError):
            status_reset(player_info)

    def test_missing_strength_key_in_player_info(self):
        player_info = {"Intelligence": 1, "Dexterity": 1, "Magic Power": 1}
        with self.assertRaises(KeyError):
            status_reset(player_info)

    def test_missing_intelligence_key_in_player_info(self):
        player_info = {"Strength": 1, "Dexterity": 1, "Magic Power": 1}
        with self.assertRaises(KeyError):
            status_reset(player_info)

    def test_missing_dexterity_key_in_player_info(self):
        player_info = {"Strength": 1, "Intelligence": 1, "Magic Power": 1}
        with self.assertRaises(KeyError):
            status_reset(player_info)

    def test_missing_magic_power_key_in_player_info(self):
        player_info = {"Strength": 1, "Intelligence": 1, "Dexterity": 1}
        with self.assertRaises(KeyError):
            status_reset(player_info)

    def test_strength_key_with_non_numeric_value_in_player_info(self):
        player_info = {'Strength': "ok", 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32}
        with self.assertRaises(TypeError):
            status_reset(player_info)

    def test_intelligence_key_with_non_numeric_value_in_player_info(self):
        player_info = {'Strength': 32, 'Dexterity': "ok", 'Intelligence': 46, 'Magic Power': 32}
        with self.assertRaises(TypeError):
            status_reset(player_info)

    def test_dexterity_key_with_non_numeric_value_in_player_info(self):
        player_info = {'Strength': 32, 'Dexterity': 45, 'Intelligence': "ok", 'Magic Power': 32}
        with self.assertRaises(TypeError):
            status_reset(player_info)

    def test_magic_power_key_with_non_numeric_value_in_player_info(self):
        player_info = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': "ok"}
        with self.assertRaises(TypeError):
            status_reset(player_info)

    def test_create_new_keys(self):
        player = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32}
        expected = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32, 'Max HP': 80,
                    'Max MP': 80, 'Current HP': 80, 'Current MP': 80, 'Status': 'Healthy'}
        status_reset(player)
        self.assertEqual(expected, player)

    def test_replace_existing_keys(self):
        player = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32, 'Max HP': 100,
                  'Max MP': 200, 'Current HP': 300, 'Current MP': 400, 'Status': 'Poisoned'}
        expected = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32, 'Max HP': 80,
                    'Max MP': 80, 'Current HP': 80, 'Current MP': 80, 'Status': 'Healthy'}
        status_reset(player)
        self.assertEqual(expected, player)

    def test_no_changes_on_existing_keys(self):
        player = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32, 'Max HP': 80,
                  'Max MP': 80, 'Current HP': 80, 'Current MP': 80, 'Status': 'Healthy'}
        expected = {'Strength': 32, 'Dexterity': 45, 'Intelligence': 46, 'Magic Power': 32, 'Max HP': 80,
                    'Max MP': 80, 'Current HP': 80, 'Current MP': 80, 'Status': 'Healthy'}
        status_reset(player)
        self.assertEqual(expected, player)

