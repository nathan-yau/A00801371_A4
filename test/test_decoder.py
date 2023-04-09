from unittest import TestCase
from save_load.uid_converter import decoder


class DecoderTest(TestCase):
    def test_non_numeric_character(self):
        with self.assertRaises(ValueError):
            decoder("ABCDE")

    def test_numeric_character_that_is_not_a_length_of_multiple_of_four(self):
        with self.assertRaises(ValueError):
            decoder("123455467892324")

    def test_numeric_character_with_length_of_3(self):
        with self.assertRaises(ValueError):
            decoder("123")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            decoder("")

    def test_the_shortest_string_with_number_character_with_length_of_multiple_of_four(self):
        self.assertEqual(decoder("0097"), "a")

    def test_a_considerably_long_string_with_number_character_with_length_of_multiple_of_four(self):
        self.assertEqual(decoder("009700980099010001010102010301040105"), "abcdefghi")

