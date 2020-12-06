# PROGRAM NAME: 10_21_2020__What_Is_In_Your_Pocket.py
# PROGRAM PURPOSE: To print the items contained in your pocket !! This is a practice program for while loops !!
# MADE BY: Lisette Spalding
# PYTHON VER. USED: 3.8

# Initalizing an empty list
items = []

# Looping until user is done...
while True:
    # Asking user for item, along with detailing instruction
    pocketItem = input("What is in your pocket? (Please only enter one item at a time...) \
\n\tPlease press ONLY enter once you're done..\n--->  ")

    # Creating a way for the loop to either break or continue
    if pocketItem != "":
        # Appending item
        items.append(pocketItem)
    else:
        break

# Printing final list...
print("Your pockets contain:",items)
