import pytest
from src_v1.game import Apples2Apples, Player

def test_card_deck_setup():
    red_apples, green_apples = setup_game_decks()  # Mock file reading
    assert len(red_apples) > 0
    assert len(green_apples) > 0
    assert len(red_apples) != len(green_apples)  # Expect varied deck sizes

def test_card_distribution():
    players = [Player(i) for i in range(4)]
    distribute_cards(players, red_apples)  # Mock setup
    for player in players:
        assert len(player.hand) == 7
