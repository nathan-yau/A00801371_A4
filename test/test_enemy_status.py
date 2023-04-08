from unittest import TestCase
from unittest.mock import patch
from combat.enemy_info import enemy_status


class TestEnemyStatus(TestCase):
    def test_type_error_with_non_dict_type_enemy_info(self):
        with self.assertRaises(TypeError):
            enemy_status("Hello")

    def test_key_error_with_name_exp_hp_with_wrong_order(self):
        with self.assertRaises(KeyError):
            enemy_status({"EXP": 100, "HP": 200, "Name": "Nathan"})

    def test_key_error_with_with_missing_one_element(self):
        with self.assertRaises(KeyError):
            enemy_status({"EXP": 100, "HP": 200})

    def test_key_error_with_with_missing_two_element(self):
        with self.assertRaises(KeyError):
            enemy_status({"EXP": 100})

    def test_key_error_with_with_empty_dict(self):
        with self.assertRaises(KeyError):
            enemy_status({})

    def test_key_error_with_with_unrelated_elements(self):
        with self.assertRaises(KeyError):
            enemy_status({"Hello": 1, "World": 1, "!": 1})

    def test_exactly_three_elements_in_enemy_info(self):
        result = "Enemy Information\n\nName        Nathan\nEXP            100\nHP             200"
        self.assertEqual(enemy_status({"Name": "Nathan", "EXP": 100, "HP": 200}), result)

    def test_more_than_three_elements_in_enemy_info(self):
        result = "Enemy Information\n\nName        Nathan\nEXP            100\nHP             200"
        self.assertEqual(enemy_status({"Name": "Nathan", "EXP": 100, "HP": 200, "MP": 120, "Hello": 200}), result)
