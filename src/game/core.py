from typing import List, Optional, Callable
import random


class Player:
    """
    Represents a player in the game. Can be a bot, online, or local player.
    """

    def __init__(self, player_id: int, is_bot: bool = False,
                 connection=None,
                 input_func: Optional[Callable] = input,
                 output_func: Optional[Callable] = print):
        self.player_id = player_id
        self.is_bot = is_bot
        self.connection = connection
        self.hand: List[str] = []
        self.green_apples: List[str] = []
        self.input_func = input_func
        self.output_func = output_func

    def add_card(self, card: str):
        """Add a card to the player's hand."""
        self.hand.append(card)

    def play(self) -> Optional[str]:
        """Plays a card based on the type of player."""
        if not self.hand:
            return None
        if self.is_bot:
            return self._bot_play()
        elif self.connection:
            return self._online_play()
        elif self._local_play():
            return self._local_play()
        else:
            while True:
                self.output_func(f"Your hand: {', '.join(self.hand)}")
                choice = self.input_func("Choose a card by index: ")
                if choice.isdigit():
                    idx = int(choice)
                    if 0 <= idx < len(self.hand):
                        return self.hand.pop(idx)
                self.output_func("Invalid choice. Try again.")

    def _bot_play(self) -> str:
        """Simulates a bot selecting a random card."""
        if not self.hand:
            self.output_func(f"🤖 Bot Player {self.player_id} has no cards to play! Skipping turn...")
            return "No Card"
        self.output_func(f"🤖 Bot Player {self.player_id} is thinking...")
        chosen_card = self.hand.pop(random.randint(0, len(self.hand) - 1))
        self.output_func(f"🤖 Bot Player {self.player_id} played: '{chosen_card}'")
        return chosen_card

    def _online_play(self) -> str:
        """Handles card selection for an online player."""
        try:
            return self.connection.recv(1024).decode().strip()
        except Exception:
            self.output_func("⚠️ Connection error for online player!")
            return ""

    def _local_play(self) -> str:
        """Handles card selection for a local player."""
        self.output_func("\n🃏 **[Your Turn to Play!]** 🃏")
        self.output_func(f"✨ Your hand contains the following Red Apples (Cards):")
        for index, card in enumerate(self.hand):
            self.output_func(f"  [{index}] {card}")
        self.output_func("🎯 Tip: Choose the card that best matches the Green Apple (judge's word/phrase)!")
        while True:
            try:
                choice = int(self.input_func("🌟 Enter the **index** of the card you'd like to play: "))
                if choice < 0 or choice >= len(self.hand):
                    raise ValueError
                chosen_card = self.hand.pop(choice)
                self.output_func(f"🎉 You played: '{chosen_card}'")
                return chosen_card
            except ValueError:
                self.output_func("🚫 Invalid input. Please enter a valid **card index**!")

    def judge(self, played_apples: List[str]) -> int:
        """Allows the player to select the winning card."""
        if self.is_bot:
            self.output_func(f"🤖 Bot Player {self.player_id} is judging the cards...")
            winner_index = random.randint(0, len(played_apples) - 1)
            self.output_func(f"🤖 Bot Player {self.player_id} selected card #{winner_index} as the winner!")
            return winner_index
        elif self.connection:
            return int(self.connection.recv(1024).decode().strip())
        else:
            self.output_func("\n👑 **[Judge's Turn]** 👑")
            self.output_func("You are the judge for this round! 🏅")
            self.output_func("✨ The Green Apple represents a concept. Pick the Red Apple card that you think matches it best!")
            self.output_func("Played Red Apples (Cards):")
            for index, card in enumerate(played_apples):
                self.output_func(f"  [{index}] {card}")
            while True:
                try:
                    choice = int(self.input_func("🌟 Enter the **index** of the card you think is the best match: "))
                    if choice < 0 or choice >= len(played_apples):
                        raise ValueError
                    self.output_func(f"🎖️ You selected card #{choice} as the winner!")
                    return choice
                except ValueError:
                    self.output_func("🚫 Invalid input. Please enter a valid **card index**!")


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
        """Distributes up to 7 cards to each player at the start of the game."""
        print("\n🍎 **[Dealing Cards]** 🍎")
        for player in self.players:
            cards_to_deal = min(len(self.red_apples), 7 - len(player.hand))
            for _ in range(cards_to_deal):  # Each player gets up to 7 cards
                player.add_card(self.red_apples.pop())
            if len(player.hand) < 7:
                print(f"⚠️ Player {player.player_id} received only {len(player.hand)} cards (not enough Red Apples).")

    def run(self):
        """Main game loop."""
        print("\n🎉 Welcome to **Apples to Apples**! 🎉")
        print("🟢 Goal: Be the **first player** to collect 4 Green Apples (Points)!")
        print("👑 Each round, one player is the **judge** and selects a Green Apple (adjective or phrase).")
        print("🍎 Other players play Red Apples (cards) from their hand that best match the Green Apple.")
        print("🏆 The judge picks the best match, and that player wins the round!\n")

        judge_index = random.randint(0, len(self.players) - 1)
        while not self._game_over():
            green_apple = self.green_apples.pop(0)
            print("\n🍏 **[New Round]** 🍏")
            print(f"🟢 The Green Apple (Judge's Word/Phrase) is: **{green_apple}**")
            print(f"👑 Player {self.players[judge_index].player_id} is the **judge** this round!\n")
            self._collect_plays(judge_index)
            print("\n📜 **All cards have been played!** 📜")
            print("👀 The judge is now deciding the **best match**...")
            # Judge selects the winning card
            winner_index = self.players[judge_index].judge(self.played_apples)
            winning_card = self.played_apples[winner_index]
            print(f"🎉 **The winning card is: '{winning_card}'**!")
            print(f"🏆 Player {winner_index} wins this round and collects the Green Apple: **{green_apple}**")
            self.players[winner_index].green_apples.append(green_apple)
            # Clear played cards for the next round
            self.played_apples.clear()
            # Refill players' hands up to 7 cards
            self._refill_cards()
            # Rotate the judge to the next player
            judge_index = (judge_index + 1) % len(self.players)

        self._announce_winner()

    def _collect_plays(self, judge_index: int):
        """Collects played cards from all non-judging players."""
        for i, player in enumerate(self.players):
            if i != judge_index:
                print(f"🎴 Player {player.player_id} is selecting their card...")
                card = player.play()
                self.played_apples.append(card)

        random.shuffle(self.played_apples)

    def _refill_cards(self):
        """Refills players' hands up to 7 cards after each round."""
        for player in self.players:
            while len(player.hand) < 7 and self.red_apples:
                player.add_card(self.red_apples.pop())

    def _game_over(self) -> bool:
        """Checks if any player has collected enough green apples to win."""
        return any(len(player.green_apples) >= 4 for player in self.players)

    def _announce_winner(self):
        """Announces the winner of the game."""
        winner = max(self.players, key=lambda p: len(p.green_apples))
        print("\n🏁 **[Game Over]** 🏁")
        print(f"🎉 **Player {winner.player_id}** is the winner with **{len(winner.green_apples)} Green Apples!**")
        print("🍏 Thank you for playing **Apples to Apples**! 🍎")
