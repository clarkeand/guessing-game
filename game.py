"""A number-guessing game."""
import random
name = input("Howdy what's your name?")
save_guesses = 100 

while True: 
    usernum = input("Do you want to set the range of numbers to guess? Y/N")
    if usernum == "Y" or usernum == "y":
       low_num = input("Whats the lowest number?")
       high_num = input("Whats the highest number?")
    else:
        low_num = 1
        high_num = 100
    print(f"{name} I'm thinking of a number between {low_num} and {high_num}.")
    print("Can you guess my number?")
    secretnum = random.randint(low_num,high_num)
    # print(secretnum)
    guesses = 0
    while guesses < 10:
        guess = input("Whats your guess?")
        if guess.isdigit():
            guess = int(guess)
            guesses = guesses + 1
            if guess <= high_num and guess >= low_num:
                if guess > secretnum:
                    print("Sorry, too high")
                elif guess < secretnum:
                    print("Sorry, too low")
                elif guess == secretnum:
                    print(f"Well done {name}, you got it in {guesses} tries!")
            else: 
                print("That is not within the range, don't cheat! Please enter a number between 1-100")
        else:
            print("Invalid input numbers only")
    if guesses == 10:
        print("You ran out of guesses sorry")

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
