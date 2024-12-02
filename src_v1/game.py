from src_v1.player import Player
from src_v1.played_apple import PlayedApple
import random
import os


class Game:
    def __init__(self, num_players, red_apple_file="assets/redApples.txt", green_apple_file="assets/greenApples.txt"):
        self.num_players = num_players
        self.red_deck = self.load_cards(red_apple_file)
        self.green_deck = self.load_cards(green_apple_file)
        self.players = []
        self.played_apples = []
        self.judge_index = 0

    def load_cards(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return []

    def shuffle_deck(self, deck):
        random.shuffle(deck)

    def deal_hand(self):
        hand = [self.red_deck.pop(0) for _ in range(7)]
        return hand

    def initialize_players(self):
        # Add human and/or bot players
        for i in range(self.num_players - 1):
            is_bot = (i < self.num_players - 2)  # Last player is human
            hand = self.deal_hand()
            self.players.append(Player(player_id=i, hand=hand, is_bot=is_bot))

        # Add the server/human player
        self.players.append(Player(player_id=self.num_players - 1, hand=self.deal_hand(), is_bot=False))

    def play_round(self):
        print("Starting a new round...")
        self.shuffle_deck(self.red_deck)
        self.shuffle_deck(self.green_deck)

        # Display the green apple card for the round
        green_apple = self.green_deck.pop(0)
        print(f"Green Apple: {green_apple}")

        # Allow players to play their red apple
        self.played_apples = []
        for i, player in enumerate(self.players):
            if i != self.judge_index:  # Judge does not play
                played_apple = player.play()
                self.played_apples.append(played_apple)

        # Judge chooses the best red apple
        print("\nPlayed Red Apples:")
        for i, apple in enumerate(self.played_apples):
            print(f"[{i}] {apple.red_apple}")

        judge = self.players[self.judge_index]
        winning_apple = judge.judge(self.played_apples)
        print(f"\nWinning Card: {winning_apple.red_apple} by Player {winning_apple.player_id}")

        # Add the green apple to the winner's collection
        winner = self.players[winning_apple.player_id]
        winner.green_apples.append(green_apple)

        # Rotate judge
        self.judge_index = (self.judge_index + 1) % len(self.players)

    def play_game(self, winning_score=4):
        self.initialize_players()

        while True:
            self.play_round()

            # Check if any player has reached the winning score
            for player in self.players:
                if len(player.green_apples) >= winning_score:
                    print(f"\nPlayer {player.player_id} wins the game with {len(player.green_apples)} green apples!")
                    return
