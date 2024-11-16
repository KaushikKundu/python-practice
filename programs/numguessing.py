import random

def game():
    secret = random.randint(1,30)
    numOfGuesses = 0
    totalGuesses = 5
    while numOfGuesses < totalGuesses:
        numOfGuesses += 1
        guess = int(input("guess a number between 1 and 50: "))
        if guess < secret:
            print("too low")
        elif guess > secret:
            print("too high")
        else:
            print("you win!")
            break
    if numOfGuesses == totalGuesses:
        print("guesses over!")
        print("the number was: ", secret)
        print("you lost")

while True:
    game()
    restart = input("do you want to play again? y/n")
    if restart == "y":
        game()
    else:
        print("goodbye")
        break