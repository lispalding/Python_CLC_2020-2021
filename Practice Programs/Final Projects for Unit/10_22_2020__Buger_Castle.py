# PROGRAM NAME: 10_22_2020__Buger_Castle.py
# PROGRAM PURPOSE: To allow the user to order something from Burger Castle !! THIS IS A CLASS PROJECT FOR LOOPS AND LISTS !!
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-22-2020
# PYTHON VER. USED: 3.8

# Initalizing a tuple that contains valid orders
VALID_ORDERS = ("BURGER", "FRIES", "SALAD", "SODA", "MILKSHAKE")
# And now for item description...
ITEM_DESC = ("Half-Pound Burger", "Large Fries", "Side Salad", "Diet Root Beer", "Chocolate Shake")

# Initalizing an empty list for the user's order....
order = []

# Welcoming the user
print("\t\tWelcome to Burger Castle!")
print("Menu: ",VALID_ORDERS)
print("Please enter each item in your order seperately. Press 'Enter' or type 'Quit' on an empty line when done.")

while True:
    # Getting user input
    ordered = input("What would you like to order?  ")
    ordered = ordered.upper() # Converting that user input to UPPERCASE

    # Telling the program what to do with the order
    if ordered in VALID_ORDERS:
        order.append(ordered)
        print("\tYour current order is:",order)
    else:
        if (ordered == "") or ("Q" in ordered):
            print("\n")
            print("Order complete; you have ordered:")
            for item in order:
                index = VALID_ORDERS.index(item)
                description = ITEM_DESC[index]
                print("--",description)
            print("\nThank you for visiting Burger Castle!")
            break # This breaks the while True loop if ordered is an enter key, or any version of quit
        else:
            print("Sorry, we don't sell",ordered)
    
