from unittest import TestCase
from events.movement import route_validate_move
from unittest.mock import patch
import io


class RouteValidateTest(TestCase):
    encoded_routes = '01230049005800320040004000510044003200480041004400320040005100440' \
                     '03200490041004400320040004900440032004800410044003200400049004400' \
                     '32005000410044003200400050004400320048004100440032004000510044003' \
                     '20050004100440032004000520044003200500041004400320040005000440032' \
                     '00500041004100440032005000580032004000400048004400320048004100440' \
                     '03200400048004400320050004100440032004000490044003200480041004400' \
                     '32004000490044003200500041004400320040005000440032004800410044003' \
                     '20040005000440032004900410044003200400050004400320050004100440032' \
                     '00400051004400320050004100410044003200510058003200400040004800440' \
                     '03200510041004400320040005000440032005100410044003200400052004400' \
                     '32005000410041004400320052005800320040004000520044003200490041004' \
                     '4003200400048004400320050004100440032004000500044003200500041004' \
                     '10125'
    incorrect_route = '01230049005800320040004000510044003200480041004400320040005100440' \
                      '03200490041004400320040004900440032004800410044003200400049004400' \
                      '32005000410044003200400050004400320048004100440032004000510044003' \
                      '20050004100440032004000500044003200500041004400320040005000440032' \
                      '00500041004100440032005000580032004000400048004400320048004100440' \
                      '03200400048004400320050004100440032004000490044003200480041004400' \
                      '32004000490044003200500041004400320040005000440032004800410044003' \
                      '20040005000440032004900410044003200400050004400320050004100440032' \
                      '00400051004400320050004100410044003200510058003200400040004800440' \
                      '03200510041004400320040005000440032005100410044003200400050004400' \
                      '32005000410041004400320050005800320040004000500044003200490041004' \
                      '4003200400048004400320050004100440032004000500044003200500041004' \
                      '10125'

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_when_avatar_is_not_dict(self, _):
        with self.assertRaises(TypeError):
            character = ["X-coordinate", "Y-coordinate"]
            route_validate_move("test_route_validate_move.py", character, 1)

    @patch('builtins.open', return_value=io.StringIO('00910093'))
    def test_when_next_move_is_not_dict(self, _):
        with self.assertRaises(TypeError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, 1)

    def test_when_file_is_not_found(self):
        with self.assertRaises(FileNotFoundError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("FileNotFound.py", character, 1)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_there_s_no_x_coordinate_in_avatar(self, _):
        with self.assertRaises(KeyError):
            character = {"Z-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, 1)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_there_s_no_y_coordinate_in_avatar(self, _):
        with self.assertRaises(KeyError):
            character = {"X-coordinate": 1, "Z-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, 1)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_heading_is_greater_than_4(self, _):
        with self.assertRaises(ValueError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, 200)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_heading_is_zero(self, _):
        with self.assertRaises(ValueError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, 0)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_heading_is_negative_integer(self, _):
        with self.assertRaises(ValueError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, -12)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_heading_is_floating_point(self, _):
        with self.assertRaises(ValueError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, 12.232)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_heading_is_not_integer(self, _):
        with self.assertRaises(ValueError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, "123")

    @patch('builtins.open', return_value=io.StringIO(incorrect_route))
    def test_heading_is_not_found_in_file(self, _):
        with self.assertRaises(KeyError):
            character = {"X-coordinate": 1, "Y-coordinate": 1}
            route_validate_move("test_route_validate_move.py", character, 4)

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_the_desired_travel_direction_is_valid(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 1}
        self.assertTrue(route_validate_move("test_route_validate_move.py", character, 4))

    @patch('builtins.open', return_value=io.StringIO(encoded_routes))
    def test_the_desired_travel_direction_is_not_valid(self, _):
        character = {"X-coordinate": 2, "Y-coordinate": 3}
        self.assertFalse(route_validate_move("test_route_validate_move.py", character, 3))
