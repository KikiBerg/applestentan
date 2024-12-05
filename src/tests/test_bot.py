import pytest
from src.game.bot import BotPlayer


@pytest.mark.rules
def test_bot_decision_logic():
    bot = BotPlayer(player_id=2)
    bot.hand = ["apple1", "longer_card_name", "short"]
    played_card = bot.play()
    assert played_card == "longer_card_name"  # Bot prefers longest card


def test_bot_play():
    bot = BotPlayer(player_id=0)
    bot.add_card('Red Apple')
    bot.add_card('Big Red Apple')
    chosen_card = bot.play()  # Bot should choose the longer card
    assert chosen_card == 'Big Red Apple'


def test_bot_no_cards():
    bot = BotPlayer(player_id=1)
    chosen_card = bot.play()
    assert chosen_card == 'No Card'  # Bot should return "No Card" if no cards are available