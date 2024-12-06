# Bot-specific logic can be extended or overridden here
from .core import Player


class BotPlayer(Player):
    """
    A bot with extended behavior, inheriting from Player.
    """
    def __init__(self, player_id: int):
        super().__init__(player_id, is_bot=True)

    def play(self) -> str:
        """Overrides the play method to ensure correct behavior for bots."""
        return self._bot_play()

    def _bot_play(self) -> str:
        """Advanced bot decision-making logic."""
        if not self.hand:
            print(f"Bot Player {self.player_id} has no cards to play!")
            return "No Card"  # Fallback if hand is empty
        return max(self.hand, key=len)
