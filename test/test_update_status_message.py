from unittest import TestCase
from GUI_update.update_status_frame import update_status_message


class UpdateStatusMessageTest(TestCase):

    def test_when_player_info_is_not_dict(self):
        player_info = "Hello"
        with self.assertRaises(TypeError):
            update_status_message(player_info, 0, 0)

    def test_when_start_is_not_an_integer(self):
        player_info = {"Name": "Nathan", "Current HP": 100, "Current MP": 200, "Strength": 100}
        with self.assertRaises(TypeError):
            update_status_message(player_info, "abc", 0)

    def test_when_end_is_not_an_integer(self):
        player_info = {"Name": "Nathan", "Current HP": 100, "Current MP": 200, "Strength": 100}
        with self.assertRaises(TypeError):
            update_status_message(player_info, 0, "abc")

    def test_when_player_info_does_not_contain_current_hp_when_max_hp_occurs(self):
        player_info = {"Name": "Nathan", "Current MP": 200, "Max HP": 100}
        with self.assertRaises(KeyError):
            update_status_message(player_info, 4, 4)

    def test_when_player_info_does_not_contain_current_mp_when_max_mp_occurs(self):
        player_info = {"Name": "Nathan", "Current HP": 200, "Max MP": 100}
        with self.assertRaises(KeyError):
            update_status_message(player_info, 4, 4)

    def test_skip_all_elements(self):
        character_dict = {"Name": "Nathan", "Current HP": 100, "Current MP": 200, "Strength": 100}
        expected = ''
        actual = update_status_message(character_dict, 0, 4)
        self.assertEqual(expected, actual)

    def test_skip_name_element_only(self):
        character_dict = {"Name": "Nathan", "Current HP": 100, "Current MP": 200, "Strength": 100}
        expected = 'Current HP               100\nCurrent MP               200\nStrength                 100'
        actual = update_status_message(character_dict, 0, 0)
        self.assertEqual(expected, actual)

    def test_one_element_character_dict(self):
        character_dict = {"Current HP": 100}
        expected = 'Current HP               100'
        actual = update_status_message(character_dict, 0, 0)
        self.assertEqual(expected, actual)
