# PROGRAM NAME: 09_29_2020__Guess_A_Number__Ver_One.py
# PROGRAM PURPOSE: To play a numger guessing game
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 09-29-2020
# PYTHON VER. USED: 3.7

import random

theNumber = random.randint(1,maximumRange)

print(theNumber) # !! Remove before publishing final game !!

# Printing the welcome to the game & Game rules!
print("Welcome to 'Guess My Number!")
print("\nI'm thinking of a number between one and ten!  ")
print("Try to guess it in "+str(guessNum)+" attempts!\n")

# Win conditon
winner = False

# If statements for guesses

# Guess One
guess = int(input("Pick a number between one and ten!  "))

if guess == theNumber:
    winner = True
    
elif guess < theNumber:
    print("Guess higher!")
    
else:
    print("Guess Lower!")

# Guess Two
if winner == False:
    guess = int(input("Pick a number between one and ten!  "))

    if guess == theNumber:
        winner = True
        
    elif guess < theNumber:
        print("Guess higher!")
        
    else:
        print("Guess Lower!")

# Guess Three
if winner == False:
    guess = int(input("Pick a number between one and ten!"  ))

    if guess == theNumber:
        winner = True
        
    elif guess < theNumber:
        pass
    
    else:
        pass

# If they're a winner, then congragulate!
if winner == True:
    print("You're amazing! Good job, winner!")
    
else:
    print("You lost, better luck next time!")

print("The number was...",theNumber)
print("Your guess was...",guess)
