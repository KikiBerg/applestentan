from src_v1.played_apple import PlayedApple
import random
import time


class Player:
    def __init__(self, player_id, hand=None, is_bot=False, connection=None, in_from_client=None, out_to_client=None):
        self.player_id = player_id
        self.hand = hand if hand else []
        self.is_bot = is_bot
        self.online = connection is not None
        self.connection = connection
        self.in_from_client = in_from_client
        self.out_to_client = out_to_client

    def play(self):
        if self.is_bot:
            # Simulate random delay for the bot (to fix the "bug" in the Java code)
            time.sleep(random.randint(0, 500) / 1000)  # Convert milliseconds to seconds
            played_card = self.hand.pop(0)
            return PlayedApple(self.player_id, played_card)

        elif self.online:
            try:
                # Read the card played by the online player
                a_played_apple = self.in_from_client.readline().strip()
                return PlayedApple(self.player_id, a_played_apple)
            except Exception as e:
                print(f"Error reading from client: {e}")
                return None

        else:
            # Local player
            print("Choose a red apple to play:")
            for i, card in enumerate(self.hand):
                print(f"[{i}] {card}")
            choice = int(input("Enter your choice: "))
            played_card = self.hand.pop(choice)
            return PlayedApple(self.player_id, played_card)

    def judge(self, played_apples):
        if self.is_bot:
            # Bot simply selects the first played card
            return played_apples[0]

        elif self.online:
            try:
                played_apple_index = int(self.in_from_client.readline().strip())
                return played_apples[played_apple_index]
            except Exception as e:
                print(f"Error reading judge decision from client: {e}")
                return None

        else:
            # Local player
            print("Choose which red apple wins:")
            for i, apple in enumerate(played_apples):
                print(f"[{i}] {apple.red_apple}")
            choice = int(input("Enter your choice: "))
            return played_apples[choice]

    def add_card(self, red_apple):
        self.hand.append(red_apple)
        if self.online:
            try:
                self.out_to_client.write(f"{red_apple}\n")
                self.out_to_client.flush()
            except Exception as e:
                print(f"Error sending card to client: {e}")
