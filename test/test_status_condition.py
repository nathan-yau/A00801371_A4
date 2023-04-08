from unittest import TestCase
from unittest.mock import patch
from combat.combat_actions import status_condition


class Test(TestCase):
    def test_when_status_key_not_found_in_player_info(self):
        zero_player_info = {"Current MP": 0}
        with self.assertRaises(KeyError):
            status_condition(zero_player_info)

    @patch("random.randint", return_value=0)
    def test_when_no_status_change_when_random_number_is_0(self, _):
        second_player_info = {"Status": "Healthy"}
        status_condition(second_player_info)
        self.assertEqual(second_player_info['Status'], "Healthy")

    @patch("random.randint", return_value=1)
    def test_when_status_change_when_random_number_is_1(self, _):
        second_player_info = {"Status": "Healthy"}
        status_condition(second_player_info)
        self.assertEqual(second_player_info['Status'], "Poisoned")

    @patch("random.randint", return_value=2)
    def test_when_no_status_change_when_random_number_is_2(self, _):
        second_player_info = {"Status": "Healthy"}
        status_condition(second_player_info)
        self.assertEqual(second_player_info['Status'], "Healthy")

    @patch("random.randint", return_value=3)
    def test_when_no_status_change_when_random_number_is_3(self, _):
        second_player_info = {"Status": "Healthy"}
        status_condition(second_player_info)
        self.assertEqual(second_player_info['Status'], "Healthy")

    @patch("random.randint", return_value=4)
    def test_when_no_status_change_when_random_number_is_4(self, _):
        second_player_info = {"Status": "Healthy"}
        status_condition(second_player_info)
        self.assertEqual(second_player_info['Status'], "Healthy")

    @patch("random.randint", return_value=5)
    def test_when_no_status_change_when_random_number_is_5(self, _):
        second_player_info = {"Status": "Healthy"}
        status_condition(second_player_info)
        self.assertEqual(second_player_info['Status'], "Healthy")
