# Main game logic and core classes

import random
from typing import List


class Player:
    """
    Represents a player in the game. Can be a bot, online, or local player.
    """

    def __init__(self, player_id: int, is_bot: bool = False, connection=None):
        self.player_id = player_id  # Unique ID for the player
        self.is_bot = is_bot  # Whether the player is a bot
        self.connection = connection  # Connection for online players
        self.hand: List[str] = []  # List of red apples (cards) in the player's hand
        self.green_apples: List[str] = []  # Collected green apples (points)

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
        if not self.hand:
            print(f"Bot Player {self.player_id} has no cards to play!")
            return "No Card"  # Fallback for empty hand
        print(f"Bot Player {self.player_id} is choosing a card...")
        chosen_card = self.hand.pop(random.randint(0, len(self.hand) - 1))
        print(f"Bot Player {self.player_id} chose: {chosen_card}")
        return chosen_card

    def _online_play(self) -> str:
        """Handles card selection for an online player."""
        try:
            return self.connection.recv(1024).decode().strip()  # Receive choice
        except Exception:
            return ""

    def _local_play(self) -> str:
        """Handles card selection for a local player."""
        print("\n[Your Turn to Play]")
        print(f"Your hand contains the following Red Apples (Cards):")
        for index, card in enumerate(self.hand):
            print(f"[{index}] {card}")
        print("Tip: Choose a card that best matches the Green Apple (judge's word/phrase)!")
        while True:
            try:
                choice = int(input("Enter the index of the card you'd like to play: "))
                if choice < 0 or choice >= len(self.hand):
                    raise ValueError
                chosen_card = self.hand.pop(choice)
                print(f"You played: {chosen_card}")
                return chosen_card
            except ValueError:
                print("Invalid input. Please enter a valid card index.")

    def judge(self, played_apples: List[str]) -> int:
        """Allows the player to select the winning card."""
        if self.is_bot:
            print(f"Bot Player {self.player_id} is judging...")
            winner_index = random.randint(0, len(played_apples) - 1)
            print(f"Bot Player {self.player_id} chose card index {winner_index} as the winner.")
            return winner_index
        elif self.connection:
            return int(self.connection.recv(1024).decode().strip())
        else:
            print("\n[Judge's Turn]")
            print("You are the judge this round!")
            print("The Green Apple word/phrase is meant to evoke a concept. Pick the best match!")
            print("Played Red Apples (Cards):")
            for index, card in enumerate(played_apples):
                print(f"[{index}] {card}")
            while True:
                try:
                    choice = int(input("Enter the index of the card you think best matches the Green Apple: "))
                    if choice < 0 or choice >= len(played_apples):
                        raise ValueError
                    print(f"You selected card index {choice} as the winner.")
                    return choice
                except ValueError:
                    print("Invalid input. Please enter a valid card index.")


class GameEngine:
    """
    Handles the core gameplay loop and interactions between players.
    """

    def __init__(self, players: List[Player], red_apples: List[str], green_apples: List[str]):
        self.players = players  # List of players in the game
        self.red_apples = red_apples  # Red apple cards (deck)
        self.green_apples = green_apples  # Green apple cards (deck)
        self.played_apples = []  # Cards played during the current round

        # Deal 7 cards to each player at the start of the game
        self._deal_cards()

    def _deal_cards(self):
        """Distributes 7 cards to each player at the start of the game."""
        print("\n[Dealing Cards]")
        for player in self.players:
            for _ in range(7):  # Each player gets 7 cards
                if self.red_apples:
                    player.add_card(self.red_apples.pop())
                else:
                    print("Warning: Not enough red apples to distribute full hands.")

    def run(self):
        """Main game loop."""
        print("Welcome to Apples to Apples!")
        print("Goal: Be the first player to collect 4 Green Apples!")
        print("Each round, one player is the judge and selects a Green Apple (adjective or phrase).")
        print("The other players play Red Apples (cards) from their hand that best match the Green Apple.")
        print("The judge picks the best match, and that player wins the round.\n")

        judge_index = random.randint(0, len(self.players) - 1)
        while not self._game_over():
            green_apple = self.green_apples.pop(0)
            print("\n[New Round]")
            print(f"The Green Apple (Judge's Word/Phrase) is: {green_apple}")
            print(f"Player {self.players[judge_index].player_id} is the judge this round.\n")
            self._collect_plays(judge_index)
            print("\nAll cards have been played!")
            print("The judge will now choose the best match...")
            winner = self.players[judge_index].judge(self.played_apples)
            winning_card = self.played_apples[winner]
            print(f"The winning card is: {winning_card}")
            print(f"Player {winner} wins this round and collects the Green Apple: {green_apple}")
            self.players[winner].green_apples.append(green_apple)
            self.played_apples.clear()
            judge_index = (judge_index + 1) % len(self.players)

        self._announce_winner()

    def _collect_plays(self, judge_index: int):
        """Collects played cards from all non-judging players."""
        for i, player in enumerate(self.players):
            if i != judge_index:
                print(f"Player {player.player_id} is selecting their card...")
                card = player.play()
                self.played_apples.append(card)

    def _game_over(self) -> bool:
        """Checks if any player has collected enough green apples to win."""
        return any(len(player.green_apples) >= 4 for player in self.players)

    def _announce_winner(self):
        """Announces the winner of the game."""
        winner = max(self.players, key=lambda p: len(p.green_apples))
        print("\n[Game Over]")
        print(f"Player {winner.player_id} is the winner with {len(winner.green_apples)} Green Apples!")
        print("Thank you for playing Apples to Apples!")
