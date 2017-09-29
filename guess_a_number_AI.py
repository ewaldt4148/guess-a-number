
# Emma #1
# Guess a Number AI

import random

# config
import time
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

          
def get_guess(current_low, current_high):
    """
    Returens a truncate average of the current low and high
    """
    
    result = (current_low + current_high)//2
    return result

    print(get_guess(current_low, current_high))
    
    pass
 

def pick_number():
    """

    Ask player to pick a number and wait until the player
    comfirms they have a number by pressing enter
    """
    print("Take a moment to pick a number from " + str(low) + " to " + str(high) + ". ")
    time.sleep(1)
    input("Ready?(press enter)")
  
    pass 

def check_guess(result):
    """
    Ask player if the computers number was too high, too low,
    or just right.

    Returns -1 if guess was  too low
             0 if guess was correct
             1 if the guess was too high
             
    """
    total = input("Is your guess " + str(result) + "? If not is the number you are thinking of higher or lower? ")

    if total.lower() == 'higher' :
        return -1
    elif total.lower() == 'lower':
        return 1
    elif total.lower() == 'yes':
        return 0
    else:
        print( "Please type 'higher' or 'lower'. :D")
    
        
    pass
            

def show_result():
    print("You won!")
    
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
    current_low = low
    current_high = high
    result = -1 

    pick_number()
   
    
    while result != 0:
        guess = get_guess(current_low, current_high)
        result = check_guess(guess)

        if result == -1 :
            current_low = guess + 1
        
            pass
        elif result == 1:
            current_high = guess - 1

        
    show_result()
      
#game starts running
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



