# Define shared fixtures
import pytest
from src.game.core import Player, GameEngine
from src.game.bot import BotPlayer


@pytest.fixture
def red_apples():
    return ["apple1", "apple2", "apple3", "apple4", "apple5", "apple6", "apple7", "apple8"]


@pytest.fixture
def green_apples():
    return ["green1", "green2", "green3", "green4"]


@pytest.fixture
def players():
    return [Player(player_id=0), Player(player_id=1), BotPlayer(player_id=2)]


@pytest.fixture
def game_engine(players, red_apples, green_apples):
    red_apples = ['Red1', 'Red2', 'Red3', 'Red4', 'Red5', 'Red6', 'Red7']
    green_apples = ['Green1', 'Green2', 'Green3', 'Green4']
    return GameEngine(players, red_apples, green_apples)
