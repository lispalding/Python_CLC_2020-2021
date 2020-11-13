# PROGRAM NAME: 11_09_2020__Day_Of_The_Week.py
# PROGRAM PURPOSE: To print the day of any given date !! THIS PROGRAM IS FUNCTION PRACTICE !!
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 11-09-2020
# PYTHON VER. USED: 3.8

import datetime

def getDayOfTheWeek(target):
    try:
        thisDate = datetime.datetime.strptime(target,"%Y-%m-%d")
        dayOfWeek = thisDate.strftime("%A")
        return dayOfWeek
    except:
        return "Invalid YYYY-MM-DD date!"

print(getDayOfTheWeek("2002-11-05"))
