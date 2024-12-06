import pytest
from src.game.core import Player, GameEngine


def test_player_add_card():
    player = Player(player_id=1)
    player.add_card("Card1")
    assert player.hand == ["Card1"], "Card should be added to the player's hand."


def test_player_play_no_cards():
    player = Player(player_id=1)
    played_card = player.play()
    assert played_card is None, "Player should return None when there are no cards to play."


def test_bot_play():
    player = Player(player_id=1, is_bot=True)
    player.add_card("Card1")
    played_card = player.play()
    assert played_card == "Card1", "Bot should play the only card in its hand."


def test_judge_bot():
    player = Player(player_id=1, is_bot=True)
    cards = ["Card1", "Card2", "Card3"]
    winner = player.judge(cards)
    assert 0 <= winner < len(cards), "Bot should select a valid card index."


def test_game_engine_deal_cards():
    players = [Player(player_id=i) for i in range(3)]
    red_apples = ["Card1", "Card2", "Card3", "Card4", "Card5", "Card6", "Card7"]
    green_apples = ["Green1"]
    engine = GameEngine(players, red_apples, green_apples)
    for player in players:
        assert len(player.hand) <= 7, "Players should receive up to 7 cards."


def test_game_over():
    players = [Player(player_id=1)]
    players[0].green_apples = ["Green1", "Green2", "Green3", "Green4"]
    engine = GameEngine(players, [], [])
    assert engine._game_over(), "Game should end when a player collects 4 green apples."


def test_announce_winner(capsys):
    players = [Player(player_id=1), Player(player_id=2)]
    players[0].green_apples = ["Green1", "Green2", "Green3", "Green4"]
    engine = GameEngine(players, [], [])
    engine._announce_winner()
    captured = capsys.readouterr()
    assert "Player 1" in captured.out, "Winner should be announced correctly."


def test_player_online_play(monkeypatch):
    class MockConnection:
        def recv(self, _):
            return b"0\n"

    player = Player(player_id=1, connection=MockConnection())
    played_card = player._online_play()
    assert played_card == "0", "Online play should correctly handle input from connection."
