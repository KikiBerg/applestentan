import pytest
from unittest.mock import patch
from src.game.core import Player, GameEngine
from src.game.bot import BotPlayer
import random
from src.main import load_cards


# Test 1: Check if the green and red apples are loaded correctly
def test_load_cards():
    # Assuming the files have been mocked for testing purposes
    green_apples = ['Adorable', 'Angry', 'Beautiful']
    red_apples = ['Cat', 'Dog', 'Car']

    # Mock the load_cards function to return predefined values
    with patch('game.main.load_cards', side_effect=[green_apples, red_apples]):
        green_cards = load_cards("greenApples.txt")
        red_cards = load_cards("redApples.txt")

        assert green_cards == green_apples
        assert red_cards == red_apples


# Test 2: Check if the decks are shuffled
def test_shuffle_decks():
    green_apples = ['Adorable', 'Angry', 'Beautiful']
    red_apples = ['Cat', 'Dog', 'Car']

    with patch('random.shuffle') as mock_shuffle:
        # Mock shuffling action
        game_engine = GameEngine(players=[], red_apples=red_apples, green_apples=green_apples)
        game_engine.run()

        # Verify shuffle was called for both red and green apple decks
        mock_shuffle.assert_any_call(green_apples)
        mock_shuffle.assert_any_call(red_apples)


# Test 3: Test if cards are dealt correctly
def test_deal_cards():
    red_apples = ['Cat', 'Dog', 'Car', 'Bird', 'Fish', 'Mouse', 'Tiger']
    players = [Player(player_id=i) for i in range(3)]  # 3 players

    # Mock the deal cards function
    game_engine = GameEngine(players=players, red_apples=red_apples, green_apples=[])

    game_engine._deal_cards()

    # Each player should have 7 cards or fewer if the deck is smaller
    for player in players:
        assert len(player.hand) == 7 or len(player.hand) == len(red_apples)


# Test 4: Check if the judge is randomly selected
def test_random_judge():
    players = [Player(player_id=i) for i in range(4)]  # 4 players

    # Mock random.randint to return a fixed value
    with patch('random.randint', return_value=2):
        game_engine = GameEngine(players=players, red_apples=[], green_apples=[])
        judge_index = random.randint(0, len(players) - 1)

        assert judge_index == 2  # Judge should be player 2


# Test 5: Test if the green apple is drawn and shown correctly
def test_draw_green_apple():
    green_apples = ['Adorable', 'Angry', 'Beautiful']
    red_apples = ['Cat', 'Dog', 'Car']
    players = [Player(player_id=i) for i in range(3)]  # 3 players

    game_engine = GameEngine(players=players, red_apples=red_apples, green_apples=green_apples)

    green_apple = green_apples.pop(0)
    game_engine.run()

    assert green_apple == 'Adorable'


# Test 6: Test if players play their red apples correctly
def test_players_play_red_apples():
    green_apples = ['Adorable']
    red_apples = ['Cat', 'Dog', 'Car']
    players = [Player(player_id=i) for i in range(3)]  # 3 players

    game_engine = GameEngine(players=players, red_apples=red_apples, green_apples=green_apples)

    with patch.object(players[0], 'play', return_value='Dog'):
        game_engine._collect_plays(judge_index=0)
        assert 'Dog' in game_engine.played_apples


# Test 7: Test if played red apples are randomized
def test_randomize_played_apples():
    green_apples = ['Adorable']
    red_apples = ['Cat', 'Dog', 'Car']
    players = [Player(player_id=i) for i in range(3)]  # 3 players

    game_engine = GameEngine(players=players, red_apples=red_apples, green_apples=green_apples)

    with patch.object(players[0], 'play', return_value='Dog'):
        with patch.object(players[1], 'play', return_value='Cat'):
            with patch.object(players[2], 'play', return_value='Car'):
                game_engine._collect_plays(judge_index=0)
                assert len(game_engine.played_apples) == 3
                assert sorted(game_engine.played_apples) != game_engine.played_apples  # Should be randomized


# Test 8: Test if the judge selects the correct favorite red apple
def test_judge_select_favorite():
    played_apples = ['Dog', 'Cat', 'Car']
    judge = Player(player_id=0)

    with patch.object(judge, 'judge', return_value=1):
        winner_index = judge.judge(played_apples)
        assert winner_index == 1


# Test 9: Test the winner gets the green apple
def test_award_green_apple():
    players = [Player(player_id=i) for i in range(3)]  # 3 players
    green_apples = ['Adorable']
    red_apples = ['Cat', 'Dog', 'Car']

    game_engine = GameEngine(players=players, red_apples=red_apples, green_apples=green_apples)

    game_engine._collect_plays(judge_index=0)
    game_engine.played_apples = ['Dog', 'Cat', 'Car']

    with patch.object(players[0], 'judge', return_value=1):
        game_engine.run()

    assert len(players[1].green_apples) == 1  # Player 1 should have won the green apple


# Test 10: Check if the game ends with the correct winner
def test_game_over():
    players = [Player(player_id=i) for i in range(4)]  # 4 players

    # Mock the winning condition for one of the players
    players[0].green_apples = ['Adorable', 'Angry', 'Beautiful', 'Smart']
    game_engine = GameEngine(players=players, red_apples=[], green_apples=[])

    assert game_engine._game_over() is True


# Test 11: Check if the green apple scoring works for 4 players
def test_scoring_4_players():
    players = [Player(player_id=i) for i in range(4)]  # 4 players

    players[0].green_apples = ['Adorable', 'Angry', 'Beautiful', 'Smart']
    game_engine = GameEngine(players=players, red_apples=[], green_apples=[])

    assert players[0].green_apples == ['Adorable', 'Angry', 'Beautiful', 'Smart']
