import unittest
from src.player import Player
from src.played_apple import PlayedApple


class TestPlayer(unittest.TestCase):
    def test_bot_play(self):
        player = Player(player_id=1, hand=["Card1", "Card2"], is_bot=True)
        played_card = player.play()
        self.assertEqual(played_card.red_apple, "Card1")
        self.assertEqual(len(player.hand), 1)

    def test_human_play(self):
        player = Player(player_id=2, hand=["Card1", "Card2"], is_bot=False)
        # Simulate user input
        with unittest.mock.patch('builtins.input', return_value="1"):
            played_card = player.play()
        self.assertEqual(played_card.red_apple, "Card2")
        self.assertEqual(len(player.hand), 1)

    def test_add_card(self):
        player = Player(player_id=1, hand=[])
        player.add_card("NewCard")
        self.assertIn("NewCard", player.hand)
