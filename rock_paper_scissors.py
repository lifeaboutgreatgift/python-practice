import random

choices = ["rock", "paper", "scissors"]
choice_map = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
scores = {"player": 0, "computer": 0}

print("Welcome to Rock Paper Scissors. Type quit to exit.")

while True:
    player_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    if player_choice == "quit":
        break

    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        scores["player"] += 1
    else:
        print("Computer wins this round!")
        scores["computer"] += 1

    print(f"Score - You: {scores['player']} | Computer: {scores['computer']}")
    print()

print("Game over.")
print(f"Final score - You: {scores['player']} | Computer: {scores['computer']}")
