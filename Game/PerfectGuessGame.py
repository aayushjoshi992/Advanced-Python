import random

randNum = random.randint(1, 100)
def guess():
    noGuess = 0
    while True:
        guessedNum = int(input("Enter a number: "))
        noGuess += 1
        if guessedNum == randNum:
            print(f"Congratulations! You guessed it right after {noGuess} guesses.")
            break
        elif guessedNum < randNum:
            print("Higher!")
        else:
            print("Lower!")
guess()