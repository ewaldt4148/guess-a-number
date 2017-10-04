
# Emma #1
# Guess a Number AI

import random

# config
import time
import math



 

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
    print("Thank you for playing, " + name + " This game was made by Emma #1 on 9/29/2017.")

          
def get_guess(current_low, current_high):
    """
    Returens a truncate average of the current low and high
    """
    
    result = (current_low + current_high)//2
    return result

    print(get_guess(current_low, current_high))
    
    pass
 
def get_range():
    low = -1
    high = -1

    print("What would you like to guess between, " + name + "?")
    print("")
    while low < 1:
        low = input("Enter the lowest possible number, " + name + ".")
        print("")
        if low.isnumeric():
            low = int(low) 

        else:
            print("")
            print("Please enter a number, " + name + ".")
            print("")
            low = 0

    while high < 0 and high < low:
        high = input("Enter the highest possible number, " + name + ".")
        print("")
        if high.isnumeric():
            if int(high) > low:
                high = int(high)
            else:
                print("You number must be higher than you lowest possible number, " + name + ".")

        else:
            print("")
            print("Please enter a number, " + name + ".")
            print("")
            high < low
    
    return low, high          
def pick_number(current_low, current_high, limit):
    """

    Ask player to pick a number and wait until the player
    comfirms they have a number by pressing enter
    """
  
    print(name + " take a moment to pick a number from " + str(current_low) + " to " + str(current_high) + ". ")
    time.sleep(5)
    print()
    input("I have " + str(limit) + " guesses. Ready, " + name + "?(press enter)")
  
    pass 

def check_guess(result):
    """
    Ask player if the computers number was too high, too low,
    or just right.

    Returns -1 if guess was  too low
             0 if guess was correct
             1 if the guess was too high
             
    """
    total = input(name + " is your guess " + str(result) + "? If not is the number you are thinking of higher(h) or lower(l)? ")
    print()

    if total.lower() == 'higher' or total.lower() == 'h' :
        print()
        return -1

    elif total.lower() == 'lower' or total.lower() == 'l' : 
        print()
        return 1
    elif total.lower() == 'yes' or total.lower() == 'y':
        return 0
    else:
        print( "Please type 'h' or 'l'. :D")
    
        
    pass
            

def show_result(tries, limit):
    if tries < limit :
        print(name +" you won! It took me " + str(tries) + " tries to get it!")
        print("")
    else:
        print("I lost :(")   
    
def play_again():
    while True:
        decision = input(name + " would you like to play again? (y/n) ")

        if decision.lower() == 'y' or decision.lower() == 'yes':
            print()
            return True
        elif decision.lower() == 'n' or decision.lower() == 'no':
            print()
            return False
        else:
            print("Please enter 'y' or 'n'.")

def play():

    current_low, current_high = get_range()
    result = -1
    tries = 0
    rounded = math.log(current_high,2) 
    limit = math.ceil(rounded)
    pick_number(current_low, current_high, limit)
   
    
    while result != 0 and tries <= limit:
        guess = get_guess(current_low, current_high)
        result = check_guess(guess)

        if result == -1 :
            current_low = guess + 1
            pass
        elif result == 1:
            current_high = guess - 1
            
        tries += 1
    show_result(tries, limit)
      
#game starts running
show_start_screen()
print("Hello, what's youre name?")
name = input("")
playing = True

while playing:
    play()
    playing = play_again()

show_credits()



