# PROGRAM NAME: 12_05_2020__best_friends.py
# PROGRAM PURPOSE: To run a "chat" program !! THIS PROGRAM IS CLASS PRACTICE !!
# FILE NAME: Friends.py
# FILE PURPOSE: To create a fuinction that creates a message
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 12-05-2020
# PYTHON VER. USED: 3.8

# Defining my class for this file
class Bestie:
    numMessages = 0

    def chat(input):
        # Setting a variable called numMessages to the numMessages out of the scope plus 1
        Bestie.numMessages = Bestie.numMessages + 1

        # Creating an if statement for if the messages go for more than 3
        if Bestie.numMessages > 3:
            print("I'm too tired...")
            return

        # Setting the input text to lowercase
        str.lower(input)

        if "ride" in input:
            print("Sure, I'll give you a ride")
        elif "call" in input:
            print("I'll call you later")
        else:
            print("You are a mystery to me")
