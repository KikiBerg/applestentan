import unittest
from src.game import Game
from src.player import Player


class TestGame(unittest.TestCase):
    def test_card_loading(self):
        game = Game(num_players=2, red_apple_file="data/testRedApples.txt", green_apple_file="data/testGreenApples.txt")
        self.assertGreater(len(game.red_deck), 0)
        self.assertGreater(len(game.green_deck), 0)

    def test_hand_dealing(self):
        game = Game(num_players=2)
        game.red_deck = ["Card1", "Card2", "Card3", "Card4", "Card5", "Card6", "Card7"]
        hand = game.deal_hand()
        self.assertEqual(len(hand), 7)

    def test_judge_rotation(self):
        game = Game(num_players=3)
        game.judge_index = 0
        game.play_round()
        self.assertEqual(game.judge_index, 1)
