"""A number-guessing game."""
import random
name = input("Howdy what's your name?")
print(f"{name} I'm thinking of a number between 1 and 100.")
print("Can you guess my number?")
secretnum = random.randint(1,101)
guesses = 0
while True:
    guess = input("Whats your guess?")
    guess = int(guess)
    guesses = guesses + 1
    if guess > secretnum:
        print("Sorry, too high")
    elif guess < secretnum:
        print("Sorry, too low")
    elif guess == secretnum:
        print(f"Well done {name}, you got it in {guesses} tries!")
        break