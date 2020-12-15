# PROGRAM NAME: main.py
# PROGRAM PURPOSE: To simulate an ATM !! THIS PROGRAM IS CLASS PRACTICE !!
# FILE NAME: input.py
# FILE PURPOSE: To create a function that will take input....
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 12-05-2020
# PYTHON VER. USED: 3.8

# Defining a class called Validator
class Validator:

    # Defining a function to get an integer
    def getInt(prompt,min,max):
        # This will loop until correct input is recieved
        while True:
            try:
                inputStr = input(prompt) # This will try to get user input
                inputInt = int(inputStr) # This will try to convert that input to an integer

                # Checking if the input doesn't exceed the max and isn't below the min
                if (inputInt >=  min) and (inputInt <= max):
                    return inputInt # Success

            except:
                continue # This will make the program try again

    # Defining a class to get a good input for a float
    def getFloat(prompt,min,max):
        # This will loop until correct input is recieved
        while True:
            try:
                inputStr = input(prompt) # This will try to get user input
                inputFloat = float(inputStr) # This will try to convert that input to an float

                # Checking if the input doesn't exceed the max and isn't below the min
                if (inputFloat >= min) and (inputFloat <= max):
                    return inputFloat # Success
                
            except:
                continue # This will make the program try again
