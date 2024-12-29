import random
from define import clear_screen, you_win, game_over, title_art

clear_screen()

title_art()
print("By Lucas Jantz")
print("Play in full screen if the askii art is the small")



num_high = int(input("choose a maximum number : "))
random_number = random.randint(0, num_high)
guess = num_high + 200
difficulty = str(input("choose difficulty, easy = 25 attempts, medium = 10 attempts, hard = 5 attempt, custom = custom atempts: "))
if difficulty == "easy":
        attempts = 25
elif difficulty == "medium":
        attempts = 10
elif difficulty == "hard":
        attempts = 5
elif difficulty == "custom":
        attempts = int(input("choose attempt amounts "))

print(f"Find the number between 0 and {num_high} to win.")

clear_screen()




prev_guesses = []

while random_number != guess:
    attempts = attempts - 1
    guess = int(input(f"Please guess a number between 0 and {num_high}: "))
    clear_screen()
    if attempts < 1:
        game_over()
        break
    if guess == random_number:
        you_win()
    elif guess > random_number:
        print("guess is too big!")
        prev_guesses.append(f"{guess} is to high")
    elif guess < random_number:
        print("guess is to small!")
        prev_guesses.append(f"{guess} is to low")
    print(f"You have {attempts} attempts left.")
    print(f"Previous guesses:")
    for i in prev_guesses:
        print(f"  * {i}")
















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
