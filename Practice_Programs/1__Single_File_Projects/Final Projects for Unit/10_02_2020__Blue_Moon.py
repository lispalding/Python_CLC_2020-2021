# PROGRAM NAME: 01_02_2020__Blue_Moon.py
# PROGRAM PURPOSE: To tell the user to play a specific song based on three things. (!! This program is if/elif/else statement practice !!)
# MADE BY: Lisette Spalding
# PYTHON VER. USED: Python 3.8

# Getting user input
blueMoon = input("\tIs there a Blue Moon tonight?\n\tPlease respond with Yes/No\n-->  ")
# \t enters a tab space that allows the text to be somewhat centered
# \n is an enter space, it moves the text to the next line

# Creating a varible for the phrase "Play the song:"
playSong = "Play the song:"

# Starting if statements

# if statement for Blue Moon
# The backslash breaks up the code, while still reading it as one line
if ("Yes" in blueMoon) or ("Y" in blueMoon) or ("y" in blueMoon) or ("Ye" in blueMoon) or \
("ye" in blueMoon) or ("Yeah" in blueMoon) or ("yeah" in blueMoon) or \
("Yea" in blueMoon) or ("yea" in blueMoon): # If user puts any "yes" for if there's a Blue Moon then always display this
    print(playSong,"Once in a Blue Moon")

# if statements for days of the week
else: # This will only go if blue moon is "no"
    # Getting user input
    monthDay = int(input("\tWhat day of the month is it tonight?\n\tPlease respond with a numeric value (1 through 31)\n-->  "))
    # \t enters a tab space that allows the text to be somewhat centered
    # \n is an enter space, it moves the text to the next line
    if (monthDay <= 7) and (monthDay > 0): # This will only run if the response to the day of the month is less than or equal to seven but also greater than zero
        # Gettting user input
        weekDay = input("\tWhat day of the week is it tonight?\n\tPlease respond with Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday\n-->  ")
        # \t enters a tab space that allows the text to be somewhat centered
        # \n is an enter space, it moves the text to the next line
        if ("M" in weekDay) or ("m" in weekDay):
            print(playSong,"Manic Monday")
        elif ("Tu" in weekDay) or ("tu" in weekDay) or ("TU" in weekDay) or ("Tw" in weekDay) or ("tw" in weekDay) or ("TW" in weekDay):
            print(playSong,"Tuesday's Gone")
        elif ("W" in weekDay) or ("w" in weekDay):
            print(playSong,"Just Wedneday")
        elif ("Th" in weekDay) or ("th" in weekDay) or ("TH" in weekDay):
            print(playSong,"Sweet Thursday")
        elif ("F" in weekDay) or ("f" in weekDay):
            print(playSong,"Friday I'm in Love")
        elif ("Sa" in weekDay) or ("sa" in weekDay) or ("SA" in weekDay):
            print(playSong,"Saturday in the Park")
        elif ("Su" in weekDay) or ("su" in weekDay) or ("SU" in weekDay):
            print(playSong,"Lazing on a Sunday Afternoon")
        else:
            print(playSong,"Days of the Week")
    else:
        print(playSong,"Day Dream Believer")
