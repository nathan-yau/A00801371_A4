from unittest import TestCase
from events.event_checker import check_for_predetermined_events


class CheckForPredeterminedEventsTest(TestCase):

    def test_key_error_caused_by_missing_character_in_game_player(self):
        with self.assertRaises(KeyError):
            player = {'characters': {'X-coordinate': 1, 'Y-coordinate': 2},
                      'environment': {(1, 2): ('BOSS', 'Nathan')}}
            check_for_predetermined_events(player)

    def test_key_error_caused_by_missing_environment_in_game_player(self):
        with self.assertRaises(KeyError):
            player = {'character': {'X-coordinate': 1, 'Y-coordinate': 2},
                      'environments': {(1, 2): ('BOSS', 'Nathan')}}
            check_for_predetermined_events(player)

    def test_key_error_caused_by_missing_x_coordinate_in_character(self):
        with self.assertRaises(KeyError):
            player = {'character': {'X-coordinates': 1, 'Y-coordinate': 2},
                      'environment': {(1, 2): ('BOSS', 'Nathan')}}
            check_for_predetermined_events(player)

    def test_key_error_caused_by_missing_y_coordinate_in_character(self):
        with self.assertRaises(KeyError):
            player = {'character': {'X-coordinate': 1, 'Y-coordinates': 2},
                      'environment': {(1, 2): ('BOSS', 'Nathan')}}
            check_for_predetermined_events(player)

    def test_key_error_caused_by_no_predetermined_event(self):
        with self.assertRaises(KeyError):
            player = {'character': {'X-coordinate': 5, 'Y-coordinate': 2},
                      'environment': {(1, 2): ('BOSS', 'Nathan')}}
            check_for_predetermined_events(player)

    def test_there_is_predetermined_non_random_event(self):
        player = {'character': {'X-coordinate': 1, 'Y-coordinate': 2},
                  'environment': {(1, 2): ('BOSS', 'Nathan'), (1, 1): ('Random', '')}}
        self.assertEqual('Nathan', check_for_predetermined_events(player))

    def test_there_is_predetermined_random_event(self):
        player = {'character': {'X-coordinate': 1, 'Y-coordinate': 1},
                  'environment': {(1, 2): ('BOSS', 'Nathan'), (1, 1): ('Random', '')}}
        self.assertEqual('Random', check_for_predetermined_events(player))
