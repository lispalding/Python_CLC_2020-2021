# PROGRAM NAME: 10_01_2020__Extra_lives.py
# PROGRAM PURPOSE: To give extra lives
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-01-2020
# PYTHON VER. USED: 3.8

# NOTE: This program is practice with if/elif/else statements

# Getting player input
score = int(input("What is your score?  "))
health = int(input("What is your current health?  "))
powerups = int(input("How many powerups do you have?  "))

# Stating how many lives player originally has
lives = 3

# Starting if statements
# Checking first requirement for extra life
if (score > 100 and health > 50):
    print("Good Job! You get an extra life!")
    lives = lives + 1
# Checking second requirement for extra life
elif (score > 1000 or powerups > 0):
    print("Good Job! You get an extra life!")
    lives = lives + 1

# Stating final number of lives
print("Final number of lives:",lives)
