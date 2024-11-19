import unittest
from src.played_apple import PlayedApple


class TestPlayedApple(unittest.TestCase):
    def test_initialization(self):
        apple = PlayedApple(player_id=1, red_apple="TestCard")
        self.assertEqual(apple.player_id, 1)
        self.assertEqual(apple.red_apple, "TestCard")

    def test_string_representation(self):
        apple = PlayedApple(player_id=1, red_apple="TestCard")
        self.assertEqual(str(apple), "Player 1: TestCard")
