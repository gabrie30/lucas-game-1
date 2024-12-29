import random
import sys
import os
def clear_screen():
    sys.stdout.flush()
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
num_high = int(input("choose between 0 and #: "))
random_number = random.randint(0, num_high)
guess = num_high + 200
difficulty = str(input("choose difficulty, easy = 25 attempts, medium = 10 attempts, hard = 5 attempt, custom = custom atempts:    "))
if difficulty == "easy":
        attempts = 25
elif difficulty == "medium":
        attempts = 10
elif difficulty == "hard":
        attempts = 5
elif difficulty == "custom":
        attempts = int(input("choose attempt amounts"))

print(f"Find the number between 0 and {num_high} to win.")

clear_screen

def you_win():
    print("Congratulations! \n"
              " ____    ____  ______    __    __     ____    __    ____  __  .__   __.\n"
              "\\   \\  /   / /  __  \\  |  |  |  |    \\   \\  /  \\  /   / |  | |  \\ |  |\n"
              " \\   \\/   / |  |  |  | |  |  |  |     \\   \\/    \\/   /  |  | |   \\|  |\n"
              "  \\_    _/  |  |  |  | |  |  |  |      \\            /   |  | |  . `  |\n"
              "    |  |    |  `--'  | |  `--'  |       \\    /\\    /    |  | |  |\\   |\n"
              "    |__|     \\______/   \\______/         \\__/  \\__/     |__| |__| \\__|")




prev_guesses = []

while random_number != guess:
    attempts = attempts - 1
    guess = int(input("Please guess a number:"))
    clear_screen()
    prev_guesses.append(guess)
    print(f"You have {attempts} attempts left.")
    print(f"Previous guesses: {prev_guesses}")
    if attempts < 1:
        print("You've run out of attempts! Game over.")
        break
    if guess == random_number:
        you_win()
    elif guess > random_number:
        print("guess is too big!")
    elif guess < random_number:
        print("guess is to small!")













# Game loop
# perform game actions
# whos turn is it
# prompt the user with where do you want to go
# give us some data
# check if the move is valid
# if yes
#   places the icon
    # check if someone has won the game
        # if they have show a screen on who won
# if no
