import random
random_number = random.randint(0, 10)
guess = 200
print("this is game, find the number between 0 and 10 to win.")



def you_win():
    print("Congratulations! \n"
              " ____    ____  ______    __    __     ____    __    ____  __  .__   __.\n"
              "\\   \\  /   / /  __  \\  |  |  |  |    \\   \\  /  \\  /   / |  | |  \\ |  |\n"
              " \\   \\/   / |  |  |  | |  |  |  |     \\   \\/    \\/   /  |  | |   \\|  |\n"
              "  \\_    _/  |  |  |  | |  |  |  |      \\            /   |  | |  . `  |\n"
              "    |  |    |  `--'  | |  `--'  |       \\    /\\    /    |  | |  |\\   |\n"
              "    |__|     \\______/   \\______/         \\__/  \\__/     |__| |__| \\__|")






while random_number != guess:
    guess = int(input("Please guess a number: "))
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
