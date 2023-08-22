import random

print("\n")
print("We are going to play Rock, Paper, Scissors. Have fun!")
print("\n")

game = ["Rock", "Paper", "Scissors"]

players_choice = int(input('Type "0" for Rock, "1" for Paper, and "2" for Scissors\n'))

computers_choice = random.choice(game)

if computers_choice == "Rock":

    if players_choice == 0:
        print("You have TIED, Rock doesn't beat Rock.")

    elif players_choice == 1:
        print("You WIN, Paper beats Rock!")

    else:
        print("You LOSE, Scissors doesn't beat Rock")


if computers_choice == "Paper":

    if players_choice == 0:
        print("You LOSE, Paper beats Rock.")

    elif players_choice == 1:
        print("You TIED, Paper doesn't beat Paper")

    else:
        print("You WIN, Scissors beats Paper")


if computers_choice == "Scissors":

    if players_choice == 0:
        print("You WIN, Rock beats Scissors.")

    elif players_choice == 1:
        print("You LOSE, Scissors beats Paper.")

    else:
        print("You TIED, Scissors doesn't beat Scissors.")


