# PROGRAM NAME: main.py
# PROGRAM PURPOSE: To simulate an ATM !! THIS PROGRAM IS CLASS PRACTICE !!
# FILE NAME: bank.py
# FILE PURPOSE: To create a function that will do a balance check.... and take care of ATM things
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 12-05-2020
# PYTHON VER. USED: 3.8

# Creating a class called ATM
class ATM:
    # Creating a variable for $20.00
    balance = 20.00

    # Creating a function called deposit
    def deposit(amount):
        # Formatting a string to print that it is depositing the money
        print(str.format("Depositing ${:.2f}",amount))

        # Adding to the original balance
        ATM.balance = ATM.balance + amount
        # Returning the balance
        return ATM.balance

    # Creating a function called withdraw
    def withdraw(amount):
        # Starting a if statement to check if the balance is greater than or equal to the amount being withdrawn
        if (ATM.balance >= amount):
            # Printing the withdrawl statement
            print(str.format("Withdrawing ${:.2f}",amount))

            # Subtracting the funds from the balance
            ATM.balance = ATM.balance - amount
        else: #Setting the else statement.. This will only be triggered if you don't have enough funds
            print("Insufficent funds")

        # Returning the balance no matter what
        return ATM.balance

    def getBalance():
        return ATM.balance
