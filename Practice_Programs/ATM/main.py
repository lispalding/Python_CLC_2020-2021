# PROGRAM NAME: main.py
# PROGRAM PURPOSE: To simulate an ATM !! THIS PROGRAM IS CLASS PRACTICE !!
# FILE NAME: main.py
# FILE PURPOSE: To run the program
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 12-05-2020
# PYTHON VER. USED: 3.8

# Importing the files needed
import Bank, Input

# Setting the balance
balance = Bank.ATM.getBalance()

# Printing the balance
print(str.format("Your starting balance is: {:.2f}",balance))

##################### DEPOSIT FUNC #####################

# Setting the amount to a good float
amount = Input.Validator.getFloat("Please enter deposit amount ($0.00 - $1000.00):   ",0.00,1000.00)

# Setting the new balance
balance = Bank.ATM.deposit(amount)

print(str.format("Your new balance is: {:.2f}",balance))

######################### FIN #########################

#################### WITHDRAWL FUNC ###################

# Setting the amount to a good float
amount = Input.Validator.getFloat("Please enter withdrawl amount ($0.00 - $1000.00):   ",0.00,1000.00)

# Setting the new balance

balance = Bank.ATM.withdraw(amount)

print(str.format("Your new balance is: {:.2f}",balance))

######################### FIN #########################
