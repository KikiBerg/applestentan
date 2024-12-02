# Allow importing core components directly from the game package
from .core import Player, GameEngine
from .phases import Phase, BasicPhase
from .network import NetworkManager
from .bot import BotPlayer

# Specify what is accessible when using `from game import *`
__all__ = ["Player", "GameEngine", "Phase", "BasicPhase", "NetworkManager", "BotPlayer"]