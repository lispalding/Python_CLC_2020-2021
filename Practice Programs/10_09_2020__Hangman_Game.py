# PROGRAM NAME: 10_09_2020__Hangman_Game.py
# PROGRAM PURPOSE: To play a game of hangman
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-13-2020
# PYTHON VER. USED: Python 3.8

# Importing the "Random" package
import random

# Hangman ANSII Art
HANGMAN = (
    """
------------
||          |
||          |
||          |
||          o
||
||
||
||
||
||
||
||
||
||
||
____________________
""",
    """
------------
||          |
||          |
||          |
||        [x_x]
||          +
||
||
||
||
||
||
||
||
||
||
____________________
""",
"""
------------
||          |
||          |
||          |
||        [x_x]
||          +
||          |
||          |
||
||
||
||
||
||
||
____________________
""",
    """
------------
||          |
||          |
||          |
||        [x_x]
||          +
||         /|\\
||          |
||
||
||
||
||
||
||
____________________
""",
    """
------------
||          |
||          |
||          |
||        [x_x]
||          +
||         /|\\
||          |
||         /
||         |
||        --
||
||
||
||
____________________
""",
    """
------------
||          |
||          |
||          |
||        [x_x]
||          +
||         /|\\
||          |
||         / \\
||         | |
||        -- --
||
||
||
||
____________________
""")

# Stating how many guesses the player can get wrong
MAX_WRONG = len(HANGMAN)-1

# Stating ten (10) words relating to Python
WORDS = ("PEP","LOOPING","FLOAT","BOOLEAN","STRING","POP","APPEND","IDLE",\
         # Just dividing it...
         "CAMELCASE","NONVENOMOUS")

# Picking between ten (10) Python related words
word = random.choice(WORDS)
index = WORDS.index(word)

# Hangman variables
wrong = 0
used = []
soFar = "?"*len(word)

# Welcoming player
print("Welcome to Hangman! Good Luck!")

while wrong <= MAX_WRONG and soFar != word: # Starting the while loop so the game will work
    print(HANGMAN[wrong])
    print("So far, you have found this out:",soFar)
    print("So far, you have used:",used)

    guess = input("\tEnter a guess...\n\t\t-->  ")
    guess = guess.upper() # The .upper causes the input to be converted to uppercase

    while guess in used: # Will only run if a guess is in used
        print("You've already guessed this letter:",guess)
        guess = input("Please put in a different guess.\n\t\t-->  ")
        guess = guess.upper()

    used.append(guess) # Appends the guess to the "used" list

    if guess in word: # Will only run if the guess is in the word, and is not in used
        print("Congratulations!",guess,"is in the word!")

        # Create a new so_far to incluide guess in the correct location...
        new = ""
        for i in range(len(word)): # For the individual in word
            if guess == word[i]:
                new += guess
            else:
                new += soFar[i]
        soFar = new
        
    else:
        print("Sorry!!",guess,"Is not in the word...")
        wrong += 1 # Adding one to the wrong if this part is tripped
        
if wrong == MAX_WRONG: # Creating a win and a lose condition print out
    print(HANGMAN[wrong])
    print("You hung him!!")
else:
    print("You saved him!!")
print("\n")
print("The word was:",word,"\n")

# Providing definitions for the words based on index position in the WORDS list
if index == 0:
    print("\tPEP is the 'Unofficial' rulebook of Python.\
It's something that defines what the standard is for formatting, and other things. """)

elif index == 1:
    print("\tLOOOPING is a kind of function that you can use in Python.\
It's one of the most common functions in programming.")

elif index == 2:
    print("\tFLOAT is a data type in Python. It's the only data type in Python that can hold decimal numbers.")

elif index == 3:
    print("BOOLEAN is a data type in Python. It's used to define True or False.")

elif index == 4:
    print("STRING is a data type in Python. It's used to hold words and letters.")

elif index ==  5:
    print("POP is a list function in Python. pop deletes the value at the specified index\
position (EX. pop(0)) so you can do something with the value. pop can not be used with tuples.")

elif index == 6:
    print("APPEND is a list function in Python. append adds a new value to the end of the list. append can not be used \
with tuples.")

elif index == 7:
    print("IDLE is the bult-in text editor in Python.")

elif index == 8:
    print("CAMELCASE is a way to type variable names in Python. It's where you type likeThis.")

else:
    print("NONVENOMOUS is what the python snake is. A python is a large, suprisingly nonvenomous snake.")

input("\t\t\tPress the enter key to exit... ") # Making the player intentionally exit the game
