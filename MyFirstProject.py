import numpy as np
print("Hello World! This is my first project with Git!\n\n")

def number_guesser():
    target = np.random.randint(1,11)
    print("Let's play a game!\nI've chosen a number between 1 and 10.")
    print("You're supposed to guess it!\n")
    guess = int(input("What is your guess?\n"))
    while guess != target:
        if (guess > 10 or guess < 1):
            print("Was that really an integer between 1 and 10?\n")
            guess = input("Try again!\n")
        else:
            if guess != target:
                guess = int(input("That was incorrect. Try again!\n"))
            else:
                continue
    print("You found the correct number! It was {}!".format(target))

number_guesser()