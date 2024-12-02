import socket
import threading
import random
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import time


class Player:
    def __init__(self, player_id, hand=None, is_bot=False, connection=None, in_from_client=None, out_to_client=None):
        self.player_id = player_id
        self.is_bot = is_bot
        self.online = connection is not None
        self.connection = connection
        self.in_from_client = in_from_client
        self.out_to_client = out_to_client
        self.hand = hand or []
        self.green_apples = []

    def play(self):
        if self.is_bot:
            # Simulating delay for bots
            time.sleep(random.randint(0, 500) / 1000)
            # Continue with non-buggy code
            Apples2Apples.played_apples.append(PlayedApple(self.player_id, self.hand.pop(0)))
        elif self.online:
            try:
                a_played_apple = self.in_from_client.readline().strip()
                Apples2Apples.played_apples.append(PlayedApple(self.player_id, a_played_apple))
            except Exception:
                pass
        else:
            print("Choose a red apple to play:")
            for i, card in enumerate(self.hand):
                print(f"[{i}] {card}")
            try:
                choice = int(input("Your choice: "))
                Apples2Apples.played_apples.append(PlayedApple(self.player_id, self.hand.pop(choice)))
            except (ValueError, IndexError):
                print("Invalid choice.")
                self.play()

    def judge(self):
        if self.is_bot:
            return Apples2Apples.played_apples[0]
        elif self.online:
            try:
                played_apple_index = int(self.in_from_client.readline().strip())
                return Apples2Apples.played_apples[played_apple_index]
            except Exception:
                return None
        else:
            print("Choose which red apple wins:")
            try:
                choice = int(input("Your choice: "))
                return Apples2Apples.played_apples[choice]
            except (ValueError, IndexError):
                print("Invalid choice.")
                return self.judge()

    def add_card(self, red_apple):
        if self.is_bot or not self.online:
            self.hand.append(red_apple)
        else:
            try:
                self.out_to_client.write(f"{red_apple}\n")
            except Exception:
                pass


class PlayedApple:
    def __init__(self, player_id, red_apple):
        self.player_id = player_id
        self.red_apple = red_apple


class Apples2Apples:
    played_apples = []

    def __init__(self, *args):
        if len(args) == 0:
            self.initialize_server()
        elif isinstance(args[0], int):
            self.initialize_server(args[0])
        elif isinstance(args[0], str):
            self.initialize_client(args[0])

    def initialize_client(self, ip_address):
        try:
            connection = socket.create_connection((ip_address, 2048))
            out_to_server = connection.makefile('w')
            in_from_server = connection.makefile('r')

            # Receive the initial hand
            hand = in_from_server.readline().strip().split(";")

            while True:
                judge_str = in_from_server.readline().strip()
                is_judge = judge_str == "JUDGE"
                if judge_str.startswith("FINISHED"):
                    print(judge_str)
                    break

                print("** NEW ROUND **" if not is_judge else "** NEW ROUND - JUDGE **")

                green_apple = in_from_server.readline().strip()
                print(f"Green apple: {green_apple}")

                if not is_judge:
                    for i, card in enumerate(hand):
                        print(f"[{i}] {card}")
                    choice = int(input("Choose a red apple to play: "))
                    out_to_server.write(f"{hand.pop(choice)}\n")
                    out_to_server.flush()

                played_apples_str = in_from_server.readline().replace("#", "\n")
                print(f"Played apples:\n{played_apples_str}")

                if is_judge:
                    choice = int(input("Choose the winning red apple: "))
                    out_to_server.write(f"{choice}\n")
                    out_to_server.flush()

                winning_apple = in_from_server.readline().strip()
                print(f"Winning apple: {winning_apple}")

                if not is_judge:
                    hand.append(in_from_server.readline().strip())
        except Exception as e:
            print(f"Error: {e}")

    def initialize_server(self, num_online_players=0):
        red_apples = Path("redApples.txt").read_text(encoding="ISO-8859-1").splitlines()
        green_apples = Path("greenApples.txt").read_text(encoding="ISO-8859-1").splitlines()
        random.shuffle(red_apples)
        random.shuffle(green_apples)

        players = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('', 2048))
            server_socket.listen()

            for i in range(num_online_players):
                connection, _ = server_socket.accept()
                in_from_client = connection.makefile('r')
                out_to_client = connection.makefile('w')

                hand = [red_apples.pop(0) for _ in range(7)]
                out_to_client.write(";".join(hand) + "\n")
                out_to_client.flush()

                players.append(Player(i, hand, False, connection, in_from_client, out_to_client))

            while len(players) < 4:
                bot_hand = [red_apples.pop(0) for _ in range(7)]
                players.append(Player(len(players), bot_hand, True))

            server_player_hand = [red_apples.pop(0) for _ in range(7)]
            players.append(Player(len(players), server_player_hand))

        judge_index = random.randint(0, len(players) - 1)

        while True:
            print("** NEW ROUND **")
            green_apple = green_apples.pop(0)
            print(f"Green apple: {green_apple}")

            with ThreadPoolExecutor(max_workers=len(players) - 1) as executor:
                for i, player in enumerate(players):
                    if i != judge_index:
                        executor.submit(player.play)

            Apples2Apples.played_apples.sort(key=lambda _: random.random())
            print("Played apples:")
            for i, apple in enumerate(Apples2Apples.played_apples):
                print(f"[{i}] {apple.red_apple}")

            winning_apple = players[judge_index].judge()
            players[winning_apple.player_id].green_apples.append(green_apple)

            if any(len(player.green_apples) >= 4 for player in players):
                print("Game finished!")
                break

            judge_index = (judge_index + 1) % len(players)


if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        Apples2Apples()
    elif sys.argv[0].isdigit():
        Apples2Apples(int(sys.argv[0]))
    else:
        Apples2Apples(sys.argv[0])
