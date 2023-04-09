from unittest import TestCase
from unittest.mock import patch
from combat.combat_actions import random_run_away_probability


class TestRandomRunAwayProbability(TestCase):

    @patch("random.randint", return_value=0)
    def test_return_true(self, _):
        self.assertTrue(random_run_away_probability())

    @patch("random.randint", return_value=1)
    def test_return_false_with_generated_1(self, _):
        self.assertFalse(random_run_away_probability())

    @patch("random.randint", return_value=2)
    def test_return_false_with_generated_2(self, _):
        self.assertFalse(random_run_away_probability())
