# Masoud Taghipour
# 99121014

import random

options = ["Rock", "Paper", "Scissors"]

def strategy_static_rock():
    return "Rock"

def strategy_random_all():
    return random.choice(options)

def strategy_rock_paper():
    return random.choice(["Rock", "Paper"])

strategy_map = {
    1: strategy_static_rock,
    2: strategy_random_all,
    3: strategy_rock_paper
}

def get_winner(player, computer):
    if player == computer:
        return "draw"
    if (player == "Rock" and computer == "Scissors") or \
       (player == "Paper" and computer == "Rock") or \
       (player == "Scissors" and computer == "Paper"):
        return "player"
    return "ai"

def simulate_game(mode, total_games=100):
    strategy = strategy_map.get(mode)
    wins = 0

    for _ in range(total_games):
        player_choice = strategy()
        computer_choice = random.choice(options)
        result = get_winner(player_choice, computer_choice)
        if result == "player":
            wins += 1

    return wins

for mode_id in range(1, 4):
    total_wins = simulate_game(mode_id)
    win_rate = total_wins / 100
    print(f"Strategy Mode {mode_id}:")
    print(f"Win Rate: {win_rate:.2f}\n")
