import os
import random
from pathlib import Path
from game.core import Player, GameEngine
from game.bot import BotPlayer


def load_cards(file_name: str):
    """
    Load cards from a text file, extracting only the card name.
    :param file_name: Name of the card file (e.g., 'redApples.txt')
    :return: List of card strings
    """
    full_path = Path(__file__).parent.parent / file_name
    print(f"Loading cards from: {full_path}")
    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            cards = []
            for line in file:
                line = line.strip()
                if line:
                    card_name = line.split(']')[0].strip('[')
                    if card_name:
                        cards.append(card_name)
            print(f"Loaded {len(cards)} cards from {file_name}")
            return cards
    except FileNotFoundError:
        print(f"Error: {full_path} not found.")
        return []


def initialize_players(num_human_players: int, num_bots: int):
    """
    Initialize the players for the game.
    :param num_human_players: Number of local human players
    :param num_bots: Number of bot players
    :return: List of Player objects
    """
    players = []
    for i in range(num_human_players):
        players.append(Player(player_id=i))  # Local human players

    for i in range(num_bots):
        players.append(BotPlayer(player_id=num_human_players + i))  # Bot players

    return players


def main():
    """
    Main entry point for the Apples2Apples game.
    """
    # Paths to the asset files
    red_apples_path = os.path.join("assets", "redApples.txt")
    green_apples_path = os.path.join("assets", "greenApples.txt")

    # Load the card decks
    red_apples = load_cards(red_apples_path)
    green_apples = load_cards(green_apples_path)

    if not red_apples or not green_apples:
        print("Error: Missing card assets. Ensure 'redApples.txt' and 'greenApples.txt' are in the 'assets' folder.")
        return

    # Shuffle the decks
    random.shuffle(red_apples)
    random.shuffle(green_apples)

    # Initialize players
    num_human_players = int(input("Enter the number of human players: "))
    num_bots = int(input("Enter the number of bot players: "))
    players = initialize_players(num_human_players, num_bots)

    # Initialize the game engine
    game_engine = GameEngine(players, red_apples, green_apples)

    # Start the game
    print("Starting Apples2Apples...")
    game_engine.run()
    print("Game over!")


if __name__ == "__main__":
    main()
