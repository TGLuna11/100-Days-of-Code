# This is the final project for day 4: Rock, Paper, Scissors
# This project is a rock, paper, scissors game that asks the user to choose
# between rock, paper, and scissors to play against the computer.

import random

print("Welcome to Rock, Paper, Scissors")

user_choice = input("What do you choose? Type 'rock', 'paper', or 'scissors': ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"You chose {user_choice}")
print(f"Computer chose {computer_choice}")

if user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose.")
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose.")
