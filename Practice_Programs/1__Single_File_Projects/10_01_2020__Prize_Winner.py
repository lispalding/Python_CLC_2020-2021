# PROGRAM NAME: 10_01_2020__Prize_Winner.py
# PROGRAM PURPOSE: To print ticket winner (Project: Working with if/elif/else statements)
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-01-2020
# PYTHON VER. USED: 3.8

# Stating variables (Ticket Numbers)
numOne = 8
numTwo = 6
numThree = 7
numFour = 5
numFive = 3
numSix = 0

# Starting if statement
if (numOne > 6) and (numTwo * numThree > 20) and (numFour - (numFive * numOne) < 0):
    print("You are the winner of the Math Club prize!")
else:
    print("You are not the winner...")
    print("Thank you for your contribution to the Math Club!")
