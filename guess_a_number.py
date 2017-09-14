import random

# config

low = 1
high = 1000
limit = 10

#start game
rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high)+ ". You have " + str(limit) + " tries to guess it.")

guess = -1
tries = 0

      
#play game 
while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
    tries += 1

#end game 
print("Game over")
if guess == rand:
    print("You win.")
else:
    print("You lose. The number was " + str(rand) + ".")  
