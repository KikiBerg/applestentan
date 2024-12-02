# Main game logic and core classes

import random
from typing import List


class Player:
    """
    Represents a player in the game. Can be a bot, online, or local player.
    """
    def __init__(self, player_id: int, is_bot: bool = False, connection=None):
        self.player_id = player_id
        self.is_bot = is_bot
        self.connection = connection
        self.hand: List[str] = []
        self.green_apples: List[str] = []

    def add_card(self, card: str):
        """Add a card to the player's hand."""
        self.hand.append(card)

    def play(self) -> str:
        """Plays a card based on the type of player."""
        if self.is_bot:
            return self._bot_play()
        elif self.connection:
            return self._online_play()
        else:
            return self._local_play()

    def _bot_play(self) -> str:
        """Simulates a bot selecting a random card."""
        return self.hand.pop(random.randint(0, len(self.hand) - 1))

    def _online_play(self) -> str:
        """Handles card selection for an online player."""
        try:
            return self.connection.recv(1024).decode().strip()
        except Exception:
            return ""

    def _local_play(self) -> str:
        """Handles card selection for a local player."""
        print("\n🍎 Your Red Apple Cards (Nouns):")
        for i, card in enumerate(self.hand):
            print(f"  {i}: {card}")
        while True:
            try:
                choice = int(input("\nChoose a Red Apple card number to play: "))
                if 0 <= choice < len(self.hand):
                    return self.hand.pop(choice)
                else:
                    print("Invalid choice. Please select a number within the range of your cards.")
            except ValueError:
                print("Please enter a valid number.")

    def judge(self, played_apples: List[str]) -> int:
        """Allows the player to select the winning card."""
        if self.is_bot:
            return random.randint(0, len(played_apples) - 1)
        elif self.connection:
            return int(self.connection.recv(1024).decode().strip())
        else:
            print("\n🍏 Green Apple (Adjective):", self.current_green_apple)
            print("\n🍎 Played Red Apple Cards (Nouns):")
            for i, card in enumerate(played_apples):
                print(f"  {i}: {card}")
            while True:
                try:
                    choice = int(input("\nAs the judge, choose the winning Red Apple card number: "))
                    if 0 <= choice < len(played_apples):
                        return choice
                    else:
                        print("Invalid choice. Please select a number within the range of played cards.")
                except ValueError:
                    print("Please enter a valid number.")


class GameEngine:
    """
    Handles the core gameplay loop and interactions between players.
    """
    def __init__(self, players: List[Player], red_apples: List[str], green_apples: List[str]):
        self.players = players
        self.red_apples = red_apples
        self.green_apples = green_apples
        self.played_apples = []

    def run(self):
        """Main game loop."""
        judge_index = random.randint(0, len(self.players) - 1)
        round_number = 1
        while not self._game_over():
            print(f"\n==== Round {round_number} ====")
            green_apple = self.green_apples.pop(0)
            print(f"\n🍏 Green Apple (Adjective): {green_apple}")
            print(f"👨‍⚖️ Judge: Player {self.players[judge_index].player_id}")
            self._collect_plays(judge_index, green_apple)
            winner = self.players[judge_index].judge(self.played_apples)
            winning_player = self.players[winner]
            winning_player.green_apples.append(green_apple)
            print(f"\n🏆 Winner: Player {winning_player.player_id} with '{self.played_apples[winner]}'")
            print(f"Player {winning_player.player_id} now has {len(winning_player.green_apples)} Green Apple(s)")
            self.played_apples.clear()
            judge_index = (judge_index + 1) % len(self.players)
            round_number += 1
            input("\nPress Enter to continue to the next round...")

    def _collect_plays(self, judge_index: int, green_apple: str):
        """Collects played cards from all non-judging players."""
        for i, player in enumerate(self.players):
            if i != judge_index:
                if not player.is_bot:
                    print(f"\nPlayer {player.player_id}, it's your turn to play a Red Apple card.")
                    print(f"Remember, the Green Apple (adjective) is: {green_apple}")
                card = player.play()
                self.played_apples.append(card)
                if not player.is_bot:
                    print(f"You played: {card}")

    def _game_over(self) -> bool:
        """Checks if any player has collected enough green apples to win."""
        for player in self.players:
            if len(player.green_apples) >= 4:
                print(f"\n🎉 Game Over! Player {player.player_id} wins with {len(player.green_apples)} Green Apples!")
                return True
        return False