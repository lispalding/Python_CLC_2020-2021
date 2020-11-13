# PROGRAM NAME: 09_29_2020__Guess_A_Number__Ver_One.py
# PROGRAM PURPOSE: To play a number guessing game
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 09-29-2020
# PYTHON VER. USED: 3.7

import random

# Printing the welcome to the game & Game rules!
print("Welcome to 'Guess My Number!")

difficulty = input("What difficulty would you like to play on: Easy, Medium, Hard; ")

# Difficulty level: Easy
if ("Ea" in difficulty) or ("ea" in difficulty) or ("EA" in difficulty) or ("Y" in difficulty) or ("y" in difficulty):
    difficultyLevel = 1
    maximumRange = 10
    guessNum = 3

#Difficulty: Medium
elif ("Me" in difficulty) or ("me" in difficulty) or ("ME" in difficulty) or ("M" in difficulty) or ("m" in difficulty):
    difficultyLevel = 2
    maximumRange = 50
    guessNum = 5

# Difficulty: Hard
else:
    difficultyLevel = 3
    maximumRange = 100
    guessNum = 10

theNumber = random.randint(1,maximumRange)

print("I'm thinking of a number between one and "+str(maximumRange)+"!  ")
print("Try to guess it in "+str(guessNum)+" attempts!\n")

# Win conditon
winner = False

# If statements for guesses

# Guess One
guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
if guess == theNumber:
    winner = True
elif guess < theNumber:
    print("Guess higher!")
else:
    print("Guess Lower!")

# Guess Two
if winner == False:
    guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
    if guess == theNumber:
        winner = True
    elif guess < theNumber:
        print("Guess higher!")
    else:
        print("Guess Lower!")


# Guess Three
if winner == False:
    if difficultyLevel  > 1:
        guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
        if guess == theNumber:
            winner = True
        elif guess < theNumber:
            print("Guess higher!")
        else:
            print("Guess Lower!")

# Guess Four
if winner == False:
    if difficultyLevel  > 1:
        guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
        if guess == theNumber:
            winner = True
        elif guess < theNumber:
            print("Guess higher!")
        else:
            print("Guess Lower!")


# Guess Five
if winner == False:
    if difficultyLevel  > 2:
        guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
        if guess == theNumber:
            winner = True
        elif guess < theNumber:
            print("Guess higher!")
        else:
            print("Guess Lower!")

# Guess Six
if winner == False:
    if difficultyLevel  > 2:
        guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
        if guess == theNumber:
            winner = True
        elif guess < theNumber:
            print("Guess higher!")
        else:
            print("Guess Lower!")

# Guess Seven
if winner == False:
    if difficultyLevel  > 2:
        guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
        if guess == theNumber:
            winner = True
        elif guess < theNumber:
            print("Guess higher!")
        else:
            print("Guess Lower!")

# Guess Eight
if winner == False:
    if difficultyLevel  > 2:
        guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
        if guess == theNumber:
            winner = True
        elif guess < theNumber:
            print("Guess higher!")
        else:
            print("Guess Lower!")

# Guess Nine
if winner == False:
    if difficultyLevel  > 2:
        guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
        if guess == theNumber:
            winner = True
        elif guess < theNumber:
            print("Guess higher!")
        else:
            print("Guess Lower!")

# Guess Ten
if winner == False:
    guess = int(input("Pick a number between one and "+str(maximumRange)+"!  "))
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

# Print number and guess to screen
print("The number was...",theNumber)
print("Your guess was...",guess)
