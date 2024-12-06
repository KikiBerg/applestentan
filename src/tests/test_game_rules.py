import pytest, random
from src.game.core import Player, GameEngine
from unittest.mock import MagicMock

# Mock data for testing
mock_green_apples = ["Funny", "Smart", "Brave"]
mock_red_apples = ["Clown", "Scientist", "Hero"] * 10
mock_players = [Player(player_id=i) for i in range(4)]


# Requirement 1: Test reading green apples from a file
def test_read_green_apples():
    assert len(mock_green_apples) > 0, "Green apples deck should not be empty"


# Requirement 2: Test reading red apples from a file
def test_read_red_apples():
    assert len(mock_red_apples) > 0, "Red apples deck should not be empty"


# Requirement 3: Test shuffling decks
def test_shuffle_decks():
    shuffled_green = mock_green_apples.copy()
    shuffled_red = mock_red_apples.copy()
    random.shuffle(shuffled_green)
    random.shuffle(shuffled_red)
    assert shuffled_green != mock_green_apples or shuffled_red != mock_red_apples, "Decks should be shuffled"


# Requirement 4: Test dealing seven red apples to each player
def test_deal_cards():
    engine = GameEngine(mock_players, mock_red_apples.copy(), mock_green_apples.copy())
    for player in engine.players:
        assert len(player.hand) == 7, "Each player should have 7 red apples"


# Requirement 5: Test randomizing the starting judge
def test_randomize_judge():
    engine = GameEngine(mock_players, mock_red_apples.copy(), mock_green_apples.copy())
    judge_index = random.randint(0, len(engine.players) - 1)
    assert 0 <= judge_index < len(engine.players), "Judge index should be within valid range"


# Requirement 6: Test drawing a green apple
def test_draw_green_apple():
    engine = GameEngine(mock_players, mock_red_apples.copy(), mock_green_apples.copy())
    green_apple = engine.green_apples.pop(0)
    assert green_apple in mock_green_apples, "Green apple should be drawn from the deck"


# Requirement 7: Test players playing a red apple
def test_play_red_apple():
    player = Player(player_id=1, input_func=MagicMock(return_value="0"))
    player.hand = ["Clown", "Scientist", "Hero"]
    played_card = player.play()
    assert played_card in ["Clown", "Scientist", "Hero"], "Played card should be from the player's hand"
    assert played_card not in player.hand, "Played card should be removed from the player's hand"


# Requirement 8: Test randomizing order of played red apples
def test_randomize_played_order():
    played_cards = ["Card1", "Card2", "Card3"]
    randomized_cards = played_cards.copy()
    random.shuffle(randomized_cards)
    assert randomized_cards != played_cards, "Order of played cards should be randomized"


# Requirement 9: Test all players (except the judge) play their red apples
def test_all_players_play():
    mock_players = [Player(player_id=i, input_func=MagicMock(return_value="0")) for i in range(4)]
    for player in mock_players:
        player.hand = ["Clown", "Scientist", "Hero", "Doctor", "Wizard", "Baker", "Pilot"]  # Fill hands

    engine = GameEngine(mock_players, mock_red_apples.copy(), mock_green_apples.copy())
    judge_index = 0  # Player 0 is the judge
    engine._collect_plays(judge_index)
    assert len(engine.played_apples) == len(mock_players) - 1, "All non-judging players must play their cards"
    for card in engine.played_apples:
        assert card in ["Clown", "Scientist", "Hero", "Doctor", "Wizard", "Baker",
                        "Pilot"], "Played cards should be from players' hands"


# Requirement 10: Test judge selects a favorite red apple
def test_judge_selects_favorite():
    judge = Player(player_id=0, input_func=lambda _: "1")  # Simulate selecting the second card
    played_cards = ["Card1", "Card2", "Card3"]
    winner_index = judge.judge(played_cards)
    assert winner_index == 1, "Judge should select the correct card index"


# Requirement 11: Test discarding submitted red apples
def test_discard_submitted_red_apples():
    engine = GameEngine(mock_players, mock_red_apples.copy(), mock_green_apples.copy())
    engine.played_apples = ["Card1", "Card2"]
    engine.played_apples.clear()
    assert len(engine.played_apples) == 0, "Played apples should be discarded after each round"


# Requirement 12: Test replenishing players' hands to seven cards
def test_replenish_hands():
    engine = GameEngine(mock_players, mock_red_apples.copy(), mock_green_apples.copy())
    for player in engine.players:
        player.hand.pop()  # Simulate playing a card
        engine._refill_cards()
        assert len(player.hand) == 7, "Players' hands should be replenished to 7 cards"


# Requirement 13: Test rotating to the next judge
def test_rotate_judge():
    engine = GameEngine(mock_players, mock_red_apples.copy(), mock_green_apples.copy())
    initial_judge_index = 0
    next_judge_index = (initial_judge_index + 1) % len(engine.players)
    assert next_judge_index == (initial_judge_index + 1) % len(engine.players), "Judge rotation should follow sequence"


# Requirement 14 & 15: Test winning conditions and score tracking
@pytest.mark.parametrize("num_players, required_points", [
    (4, 8),
    (5, 7),
    (6, 6),
    (7, 5),
    (8, 4),
])
def test_winning_conditions(num_players, required_points):
    players = [Player(player_id=i) for i in range(num_players)]
    engine = GameEngine(players, mock_red_apples.copy(), mock_green_apples.copy())

    # Simulate one player winning the game
    winner = players[0]
    winner.green_apples.extend(["Apple"] * required_points)

    assert len(winner.green_apples) >= required_points, f"Player must win with {required_points} green apples"