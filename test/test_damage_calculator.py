from unittest import TestCase
from unittest.mock import patch
from combat.combat_actions import damage_calculator


class TestDamageCalculator(TestCase):

    def test_when_attacker_is_not_dict(self):
        player_info = "Magic Power"
        foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(TypeError):
            damage_calculator("magic", player_info, foe_info)

    def test_when_defender_is_not_dict(self):
        player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        foe_info = "Magic Resistance"
        with self.assertRaises(TypeError):
            damage_calculator("magic", player_info, foe_info)

    def test_when_attack_type_is_not_string(self):
        zero_player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        zero_foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(ValueError):
            damage_calculator(123, zero_player_info, zero_foe_info)

    def test_when_attack_type_is_not_magic_nor_physical(self):
        zero_player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        zero_foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(ValueError):
            damage_calculator("kick", zero_player_info, zero_foe_info)

    def test_when_magic_power_key_not_found_in_attacker(self):
        zero_player_info = {"Strength": 200, "Current MP": 0}
        zero_foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(KeyError):
            damage_calculator("magic", zero_player_info, zero_foe_info)

    def test_when_strength_key_not_found_in_attacker(self):
        zero_player_info = {"Magic Power": 200, "Current MP": 0}
        zero_foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(KeyError):
            damage_calculator("magic", zero_player_info, zero_foe_info)

    def test_when_current_mp_not_found_in_attacker(self):
        zero_player_info = {"Magic Power": 200, "Strength": 200}
        zero_foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(KeyError):
            damage_calculator("magic", zero_player_info, zero_foe_info)

    def test_when_magic_resistance_not_found_in_defender(self):
        zero_player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        zero_foe_info = {"Dexterity": 1}
        with self.assertRaises(KeyError):
            damage_calculator("magic", zero_player_info, zero_foe_info)

    def test_when_dexterity_not_found_in_defender(self):
        zero_player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        zero_foe_info = {"Magic Resistance": 1}
        with self.assertRaises(KeyError):
            damage_calculator("magic", zero_player_info, zero_foe_info)

    def test_when_magic_power_key_not_a_number_in_attacker(self):
        player_info = {"Magic Power": "Not", "Strength": 200, "Current MP": 0}
        foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(TypeError):
            damage_calculator("magic", player_info, foe_info)

    def test_when_strength_key_not_a_number_in_attacker(self):
        player_info = {"Magic Power": 200, "Strength": "Number", "Current MP": 0}
        foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(TypeError):
            damage_calculator("magic", player_info, foe_info)

    def test_when_current_mp_not_a_number_in_attacker(self):
        player_info = {"Magic Power": 200, "Strength": 200, "Current MP": "Not"}
        foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        with self.assertRaises(TypeError):
            damage_calculator("magic", player_info, foe_info)

    def test_when_magic_resistance_not_a_number_in_defender(self):
        player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        foe_info = {"Magic Resistance": "A", "Dexterity": 1}
        with self.assertRaises(TypeError):
            damage_calculator("magic", player_info, foe_info)

    def test_when_dexterity_not_a_number_in_defender(self):
        player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        foe_info = {"Magic Resistance": 1, "Dexterity": "Number"}
        with self.assertRaises(TypeError):
            damage_calculator("magic", player_info, foe_info)

    @patch("random.uniform", return_value=1.5)
    def test_current_mp_equals_to_zero_when_it_is_magic_attack(self, _):
        player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        damage = damage_calculator("magic", player_info, foe_info)
        self.assertEqual(damage, 0)

    @patch("random.uniform", return_value=1.5)
    def test_current_mp_equals_to_zero_when_it_is_physical_attack(self, _):
        second_player_info = {"Magic Power": 200, "Strength": 200, "Current MP": 0}
        second_foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        damage = damage_calculator("physical", second_player_info, second_foe_info)
        self.assertEqual(damage, 597)

    @patch("random.uniform", return_value=1.5)
    def test_magic_attack_that_should_be_1(self, _):
        player_info = {"Magic Power": 0, "Strength": 0, "Current MP": 100}
        foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        damage = damage_calculator("magic", player_info, foe_info)
        self.assertEqual(damage, 1)

    @patch("random.uniform", return_value=1.5)
    def test_physical_attack_that_should_be_1(self, _):
        second_player_info = {"Magic Power": 0, "Strength": 0, "Current MP": 100}
        second_foe_info = {"Magic Resistance": 1, "Dexterity": 1}
        damage = damage_calculator("physical", second_player_info, second_foe_info)
        self.assertEqual(damage, 1)

    @patch("random.uniform", return_value=1.5)
    def test_magic_attack_that_should_not_hit_lowest_attack(self, _):
        player_info = {"Magic Power": 2000, "Strength": 1, "Current MP": 100}
        foe_info = {"Magic Resistance": 200, "Dexterity": 1}
        damage = damage_calculator("magic", player_info, foe_info)
        self.assertEqual(damage, 5550)

    @patch("random.uniform", return_value=1.5)
    def test_physical_attack_that_should_not_hit_lowest_attack(self, _):
        second_player_info = {"Magic Power": 1, "Strength": 2000, "Current MP": 100}
        second_foe_info = {"Magic Resistance": 1, "Dexterity": 200}
        damage = damage_calculator("physical", second_player_info, second_foe_info)
        self.assertEqual(damage, 5550)
