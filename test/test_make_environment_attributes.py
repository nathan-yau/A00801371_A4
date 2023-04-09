from unittest import TestCase
from new_game.new_environment import make_environment_attributes
from unittest.mock import patch
import io


class MakeEnvironmentAttributesTest(TestCase):

    def test_read_file_that_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            make_environment_attributes(2, 2, "FileDoNotExist.txt")

    def test_creating_board_less_than_2_rows(self):
        with self.assertRaises(ValueError):
            make_environment_attributes(3, 1, "FileDoNotExist.txt")

    def test_creating_board_less_than_2_columns(self):
        with self.assertRaises(ValueError):
            make_environment_attributes(1, 3, "FileDoNotExist.txt")

    def test_creating_board_less_than_2_rows_and_2_columns(self):
        with self.assertRaises(ValueError):
            make_environment_attributes(1, 1, "FileDoNotExist.txt")

    def test_creating_board_with_string_as_columns(self):
        with self.assertRaises(ValueError):
            make_environment_attributes("1", 2, "FileDoNotExist.txt")

    def test_creating_board_with_string_as_rows(self):
        with self.assertRaises(ValueError):
            make_environment_attributes(2, "1", "FileDoNotExist.txt")

    def test_creating_board_with_non_string_as_game_data(self):
        with self.assertRaises(OSError):
            make_environment_attributes(2, 2, 1234)

    @patch('builtins.open', return_value=io.StringIO('01230039011501120101009901050097010800950101011801010110011601150'
                                                     '03900580032009100400039006600790083008300390044003200390065006600'
                                                     '67003900410044003200400039007300840069007700390044003200390067006'
                                                     '80069003900410093004400390115011201010099010500970108009501120108'
                                                     '0097009901010115003900580032009100400049004400320048004100440032'
                                                     '00400048004400320049004100930044003901140101011501110117011400990'
                                                     '10100950108010501150116003900580032009100400039007300840069007700'
                                                     '39004400320039007201010097010801050110010300320080011101160105011'
                                                     '101100039004100930125'))
    @patch('random.randint', side_effect=[0, 0])
    def test_making_the_smallest_board(self, _, __):
        actual = make_environment_attributes(2, 2, "test_make_environment_attributes.py")
        expected = {(1, 0): ('BOSS', 'ABC'), (0, 1): ('ITEM', 'CDE'),
                    (0, 0): ('ITEM', 'Healing Potion'), (1, 1): ('RANDOM', '')}
        self.assertEqual(expected, actual)

    @patch('builtins.open', return_value=io.StringIO('01230039011501120101009901050097010800950101011801010110011601150'
                                                     '03900580032009100400039006600790083008300390044003200390065006600'
                                                     '67003900410044003200400039007300840069007700390044003200390067006'
                                                     '80069003900410093004400390115011201010099010500970108009501120108'
                                                     '0097009901010115003900580032009100400049004400320048004100440032'
                                                     '00400048004400320049004100930044003901140101011501110117011400990'
                                                     '10100950108010501150116003900580032009100400039007300840069007700'
                                                     '39004400320039007201010097010801050110010300320080011101160105011'
                                                     '101100039004100930125'))
    @patch('random.randint', side_effect=[0, 0])
    def test_making_the_large_board(self, _, __):
        actual = make_environment_attributes(5, 5, "test_make_environment_attributes.py")
        expected = {(0, 0): ('ITEM', 'Healing Potion'), (0, 1): ('ITEM', 'CDE'),
                    (0, 2): ('RANDOM', ''), (0, 3): ('RANDOM', ''), (0, 4): ('RANDOM', ''),
                    (1, 0): ('BOSS', 'ABC'), (1, 1): ('RANDOM', ''), (1, 2): ('RANDOM', ''),
                    (1, 3): ('RANDOM', ''), (1, 4): ('RANDOM', ''), (2, 0): ('RANDOM', ''),
                    (2, 1): ('RANDOM', ''), (2, 2): ('RANDOM', ''), (2, 3): ('RANDOM', ''),
                    (2, 4): ('RANDOM', ''), (3, 0): ('RANDOM', ''), (3, 1): ('RANDOM', ''),
                    (3, 2): ('RANDOM', ''), (3, 3): ('RANDOM', ''), (3, 4): ('RANDOM', ''),
                    (4, 0): ('RANDOM', ''), (4, 1): ('RANDOM', ''), (4, 2): ('RANDOM', ''),
                    (4, 3): ('RANDOM', ''), (4, 4): ('RANDOM', '')}
        self.assertEqual(expected, actual)