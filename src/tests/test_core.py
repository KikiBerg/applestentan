import pytest
from src.game.core import Player, GameEngine
import random


# Test for Player class
def test_player_initialization():
    player = Player(player_id=1)
    assert player.player_id == 1
    assert player.hand == []
    assert player.green_apples == []


def test_player_add_card():
    player = Player(player_id=1)
    player.add_card('Red Apple')
    assert 'Red Apple' in player.hand


def test_player_play_local():
    mock_input = lambda _: "0"  # Simulates choosing the first card
    mock_output = lambda msg: None  # Suppresses output during testing

    player = Player(player_id=1, input_func=mock_input, output_func=mock_output)
    player.add_card('Red Apple')
    chosen_card = player.play()
    assert chosen_card == 'Red Apple'
    assert len(player.hand) == 0  # Ensure card is removed from hand


def test_player_play_bot():
    player = Player(player_id=2, is_bot=True)
    player.add_card('Red Apple')
    chosen_card = player.play()  # Simulating bot play
    assert chosen_card == 'Red Apple'


# Test for GameEngine class
@pytest.fixture
def game_engine():
    red_apples = ['Red1', 'Red2', 'Red3', 'Red4', 'Red5', 'Red6', 'Red7']
    green_apples = ['Green1', 'Green2', 'Green3', 'Green4']
    players = [Player(player_id=0), Player(player_id=1)]
    return GameEngine(players, red_apples, green_apples)


def test_game_engine_deal_cards():
    players = [Player(player_id=i) for i in range(2)]
    # Only 8 red apples are available, not enough for two players to receive 7 each
    red_apples = ["Card1", "Card2", "Card3", "Card4", "Card5", "Card6", "Card7", "Card8"]
    green_apples = ["Green1", "Green2"]
    game_engine = GameEngine(players, red_apples, green_apples)

    total_dealt_cards = sum(len(player.hand) for player in players)
    assert total_dealt_cards == 8  # Ensure all cards are distributed
    assert all(len(player.hand) <= 7 for player in players)  # No player has more than 7 cards


def test_game_engine_run():
    mock_input = lambda _: "0"  # Simulates always choosing the first card
    mock_output = lambda msg: None  # Suppresses output during testing

    players = [Player(player_id=i, input_func=mock_input, output_func=mock_output) for i in range(2)]
    red_apples = ["Card" + str(i) for i in range(20)]
    green_apples = ["Green" + str(i) for i in range(5)]
    game_engine = GameEngine(players, red_apples, green_apples)

    game_engine.run()
    assert any(len(player.green_apples) >= 4 for player in players)  # Ensure someone wins


def test_game_over_condition(game_engine):
    game_engine.players[0].green_apples = ['Green1', 'Green2', 'Green3', 'Green4']
    assert game_engine._game_over() == True
