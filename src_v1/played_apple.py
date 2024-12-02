class PlayedApple:
    def __init__(self, player_id, red_apple):
        self.player_id = player_id
        self.red_apple = red_apple

    def __str__(self):
        return f"Player {self.player_id}: {self.red_apple}"
