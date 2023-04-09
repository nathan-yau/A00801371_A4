from unittest import TestCase
from combat.player_info import drop_item


class TestDropItem(TestCase):

    def test_key_error_missing_key_probability(self):
        with self.assertRaises(KeyError):
            drop_item({}, {'Items': {}}, {'Items': []})

    def test_key_error_missing_key_items_in_picked_foe(self):
        with self.assertRaises(KeyError):
            drop_item({}, {'Items': {}}, {'Probability': 100})

    def test_key_error_missing_key_items_in_character_info(self):
        with self.assertRaises(KeyError):
            drop_item({}, {}, {'Items': [], 'Probability': 100})

    def test_type_error_if_character_info_is_not_a_dictionary(self):
        with self.assertRaises(TypeError):
            drop_item({}, "123", {'Items': [], 'Probability': 100})

    def test_type_error_if_picked_foe_is_not_a_dictionary(self):
        with self.assertRaises(TypeError):
            drop_item({}, {}, [])

    def test_attribute_error_if_items_in_character_info_is_not_associated_with_a_dictionary(self):
        with self.assertRaises(AttributeError):
            drop_item({}, {'Items': []}, {'Items': [], 'Probability': 100})

    def test_type_error_if_items_in_picked_foe_is_not_associated_with_a_list(self):
        with self.assertRaises(TypeError):
            drop_item({}, {'Items': {}}, {'Items': 123, 'Probability': 100})

    def test_value_error_if_probability_in_picked_foe_is_not_an_int(self):
        with self.assertRaises(ValueError):
            drop_item({}, {'Items': {}}, {'Items': [], 'Probability': "abc"})

    def test_value_error_if_probability_in_picked_foe_is_greater_than_100(self):
        with self.assertRaises(ValueError):
            drop_item({}, {'Items': {}}, {'Items': [], 'Probability': 101})

    def test_value_error_if_probability_in_picked_foe_is_less_than_or_equal_to_0(self):
        with self.assertRaises(ValueError):
            drop_item({}, {'Items': {}}, {'Items': [], 'Probability': 0})