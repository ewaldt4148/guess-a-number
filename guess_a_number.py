import random

# config
import math
low = 1
high = 1000
rounded = math.log(100,2) 
limit = math.ceil(rounded) 

#helper functions
def show_start_screen():
    print("*************************************")
    print("""
 __          __  _                            _           _____                               _   _                 _               
 \ \        / / | |                          | |         / ____|                             | \ | |               | |              
  \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |  __ _   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | | |_ | | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
    \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |__| | |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |   
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \_____|\__,_|\___||___/___/  \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_| 
          """)
def show_credits():
    print("Thank you for playing! This game was made by Emma Waldthausen.")

          
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print("You have " + str(limit) + " guesses left.")
    return random.randint(low, high)

def check_guess(guess, rand, tries):

    remaining = limit - tries

    if guess < rand:
        print("You guessed too low. You have " + str(remaining) + " guesses.")
    elif guess > rand:
        print("You guessed too high. You have " + str(remaining) + " guesses.")

def show_result(guess, rand):
    if guess == rand:
        print("""__   __                     _       _ 
\ \ / /                    (_)     | |
 \ V /___  _   _  __      ___ _ __ | |
  \ // _ \| | | | \ \ /\ / / | '_ \| |
  | | (_) | |_| |  \ V  V /| | | | |_|
  \_/\___/ \__,_|   \_/\_/ |_|_| |_(_)""")
    else:
        print("You are such a loser! The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes':
            print()
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            print()
            return False
        else:
            print("Please enter 'y' or 'n'.")

def play():
    guess = 1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries <= limit:
        guess = get_guess()
        check_guess(guess, rand, tries)

        tries += 1

    show_result(guess, rand)
      
#game starts running
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

