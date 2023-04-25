"""A number-guessing game."""
import random
name = input("Howdy what's your name?")
save_guesses = 100 

while True: 
    print(f"{name} I'm thinking of a number between 1 and 100.")
    print("Can you guess my number?")
    secretnum = random.randint(1,101)
    # print(secretnum)
    guesses = 0
    while True:
        guess = input("Whats your guess?")
        if guess.isdigit():
            guess = int(guess)
            guesses = guesses + 1
            if guess <= 100 and guess >=1:
                if guess > secretnum:
                    print("Sorry, too high")
                elif guess < secretnum:
                    print("Sorry, too low")
                elif guess == secretnum:
                    print(f"Well done {name}, you got it in {guesses} tries!")
                    break
            else: 
                print("That is not within the range, don't cheat! Please enter a number between 1-100")
        else:
            print("Invalid input numbers only")
            
    if guesses < save_guesses: 
        save_guesses = guesses      
    print(f"Your current high score is: {save_guesses}")

    playAgain = input("Do you want to play again? (Y/N)")
    if playAgain == 'N' or playAgain == 'n': 
        break
    elif playAgain == 'Y' or playAgain == 'y': 
        print("New Game Loading...")
    else:
        print("Invalid Character, starting the game again.")
