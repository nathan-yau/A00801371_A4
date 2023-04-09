from unittest import TestCase
from save_load.uid_converter import encoder


class EncoderTest(TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            encoder("")

    def test_non_numeric_character(self):
        with self.assertRaises(TypeError):
            encoder(1234)

    def test_character_with_code_points_greater_than_4_digits(self):
        with self.assertRaises(ValueError):
            encoder("✐")

    def test_the_shortest_string_with_alphabet_for_encoding(self):
        self.assertEqual(encoder("a"), "0097")

    def test_a_long_string_with_alphabet_for_encoding(self):
        self.assertEqual(encoder("abcdefghi"), "009700980099010001010102010301040105")

    def test_the_shortest_string_with_number_for_encoding(self):
        self.assertEqual(encoder("1"), "0049")

    def test_a_long_string_with_number_for_encoding(self):
        self.assertEqual(encoder("1234567"), "0049005000510052005300540055")

    def test_the_shortest_string_with_special_character_for_encoding(self):
        self.assertEqual("0123", encoder("{"))

    def test_a_long_string_with_special_character_for_encoding(self):
        self.assertEqual("0123012500910093004000410045006100330064003500360037009400940038003800420125",
                         encoder("{}[]()-=!@#$%^^&&*}"))
