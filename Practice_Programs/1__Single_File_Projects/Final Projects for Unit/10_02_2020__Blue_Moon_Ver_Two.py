# PROGRAM NAME: 01_02_2020__Blue_Moon.py
# PROGRAM PURPOSE: To tell the user to play a specific song based on three things. (!! This program is if/elif/else statement practice !!)
# MADE BY: Lisette Spalding
# PYTHON VER. USED: Python 3.8

# Getting user input
blueMoon = input("Is there a blue moon tonight (Yes/No)?  ")
dayOfWeek = input("What is the day of the week (Monday-Sunday)?  ")
dayOfMonth = int(input("What is the day of the month (1 - 31)?  "))

# Stating "Play song" variable
playSong = "Play song"

# Starting if statements
if ("Y" in blueMoon) or ("y" in blueMoon): # This will only run if there is a "y" in the blueMoon input
    print(playSong,"'Once in a Blue Moon'")
elif (dayOfMonth <= 7): # This will only run if there is a "No" in the blueMoon input
    if ("M" in dayOfWeek) or ("m" in dayOfWeek):
        print(playSong,"'Manic Monday'")
    elif ("Tu" in dayOfWeek) or ("tu" in dayOfWeek) or ("TU" in dayOfWeek) or ("Tw" in dayOfWeek) or ("tw" in dayOfWeek) or ("TW" in dayOfWeek):
        print(playSong,"'Tuesday's Gone'")
    elif ("W" in dayOfWeek) or ("w" in dayOfWeek):
        print(playSong,"'Just Wednesday'")
    elif ("Th" in dayOfWeek) or ("th" in dayOfWeek) or ("TH" in dayOfWeek):
        print(playSong,"'Sweet Thursday'")
    elif ("F" in dayOfWeek) or ("f" in dayOfWeek):
        print(playSong,"'Friday I'm in Love'")
    elif ("Sa" in dayOfWeek) or ("sa" in dayOfWeek) or ("SA" in dayOfWeek):
        print(playSong,"'Saturday in the Park'")
    elif ("Su" in dayOfWeek) or ("su" in dayOfWeek) or ("SU" in dayOfWeek):
        print(playSong,"'Lazing on a Sunday Afternoon'")
    else: # This will only run if the dayOfMonth input is less than or equal to 7 but the dayOfWeek input isn't a day
        print(playSong,"Days of the Week")
else: # This will only run if the dayOfMonth input is greater than 7
     print(playSong,"'Day Dream Believer'")
