# Bot-specific logic can be extended or overridden here
from .core import Player


class BotPlayer(Player):
    """
    A bot with extended behavior, inheriting from Player.
    """
    def __init__(self, player_id: int):
        super().__init__(player_id, is_bot=True)

    def _bot_play(self) -> str:
        """Advanced bot decision-making logic."""
        # Example: Choose the longest card name for fun
        return max(self.hand, key=len)
