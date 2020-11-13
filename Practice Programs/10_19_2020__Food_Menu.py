# PROGRAM NAME: 10_19_2020_Food_Menu
# PROGRAM PURPOSE: To print a food menu !! THIS IS FUNCTION PRACTICE !!
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-19-2020
# PYTHON VER. USED: 3.8

# Creating a function to print menu choices
def get_menu_choice():
    options = ["Burger, Fries, Soda","Chicken Salad, Iced Tea", "Pizza, Soda"]
    cost = [6.99, 10.50, 5.72]

    print("The Menu Choices are:")
    for i in range(len(options)):
        print(str.format("{} - ${:5.2f} : {}",i,cost[i],options[i]))

    # Calculating the order cost
    choice = ask_number("What will you have? Please choose the number of the order...  ",0,3)
    order = options[choice]
    price = cost[choice]
    tax = 0.075
    total = (price*tax) + price

    # Telling the customer what they have ordered and the total cost
    print(str.format("Ok, you have ordered ----- {}", order))
    print(str.format("You are paying ----- ${:5.2f}", total))

# Getting a correct answer...
def ask_number(question,low,high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

def ask_yes_no(question):
    """Ask a yes or no question. And will only return yes or no"""
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

# Calling the "get_menu_choice" function
running = "y"
while running == "y":
    get_menu_choice()
    running = ask_yes_no("Do you want to order more? ")
