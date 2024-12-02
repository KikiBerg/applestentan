#   Rule 5 (Judge Randomization): Test whether the judge is selected randomly and the logic can be modular.
def test_judge_randomization():
    players = [Player(i) for i in range(4)]
    judge = select_random_judge(players)
    assert judge in players


#   Rule 14 & 15 (Game-ending): These require modifying the existing code to decouple the logic.
def test_game_ending():
    players = [Player(i) for i in range(4)]
    players[0].green_apples = ["Adjective"] * 8
    assert is_game_over(players) == True
