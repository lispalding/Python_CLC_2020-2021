# PROGRAM NAME: 10_23_2020__Alarm_Clock.py
# PROGRAM PURPOSE: To create an Alarm Clock
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-23-2020
# PYTHON VER. USED: 3.8

# Importing the modules needed
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound
import calendar
import time
import datetime

# Defining a function
def gmtnow(alarm): # GMT stands for Greenwich Mean Time
    """Getting Greenwich Mean Time -- This is based on Unix time (Also known as Epoch time) --
This is the number of seconds that have elapsed since the Unix Epoch, minus leap seconds; The Unix Epoch is 00:00:00 UTC on 1 January 1970"""
    # This gives uis the total seconds that have passed since the Unix Epoch
    seconds = calendar.timegm(time.gmtime())

    # We need to break this down to current seconds
    # So there are 60 seconds in a minute if we divide by 60
    # The remainder is the current second
    currentSecond = seconds%60
    # Now we need to figure out the minues that have passed since the Unix Epoch
    minutes = seconds//60
    currentMinute = minutes%60
    # Now we're calculating hours !! Make sure you don't use %60 becuase there isn't 60 hours in a day !!
    hour = minutes//60
    currentHour = hour%24 # This gives me the current hour in Greenwich

    # Setting time zone for Mountain Time (6 Hours behinnd Greenwich)
    currentHour -= 6

    # Now we figure out the AM or PM tag and set this to the 12 hour clock and not the 24 hour clock
    if currentHour >= 12:
        timeTag = "PM"
        currentHour -= 12
        if currentHour == 0:
            currentHour = 12
    else:
        if currentHour == 0:
            timeTag = "AM"
            currenHour = 12

    # Ajusting the hours/minutes/seconds so if it's less than two characters then I can put in a zero
    if currentHour < 10:
        adjustedHour = "0" + str(currentHour)
    else:
        adjustedHour = str(currentHour)

    if currentMinute < 10:
        adjustedMinute = "0" + str(currentMinute)
    else:
        adjustedMinute = str(currentMinute)

    if currentSecond < 10:
        adjustedSecond = "0" + str(currentSecond)
    else:
        adjustedSecond = str(currentSecond)

        

    # Formatting the time...
    timeString = str.format("{:2}:{:2}:{:2} {}",adjustedHour,adjustedMinute,adjustedSecond,timeTag)

    # Making it play a sound if the alarm time is met
    if alarm == timeString:
        alarmSound()

    return timeString

# Defining a second function for text
def showTime():
    time = gmtnow(alarm) # This will pull from what we are returning... The timeString
    txt.set(time) # This is showing the time...
    root.after(1000,showTime) # After 1000 milliseconds it will recall the showTime variable. This will keep us up to date

# Creating a third function for sound
def alarmSound():
    for i in range(5):
        winsound.Beep(750,1000)
        winsound.Beep(1000,500)
        winsound.Beep(750,1000)

def timeInput():
    """Get the alarm time that you want to set"""
    aHour = input("What hour?  ")
    aMinute = input("What minute?  ")
    aSecond = "00"
    aTag = input("AM or PM?  ").upper()
    if len(aHour) < 2:
        aMinute = "0" + aMinute

    # Formatting a alarm
    alarm = str.format("{:2}:{:2}:{:2} {}",aHour,aMinute,aSecond,aTag)
    
    return alarm

# Pulling in the sound
alarm = timeInput()
    
# Creating a user (GUI) window
root = Tk() # Pulling in the means to create a graphical program

# Stylizing the window...
root.geometry("800x200")
root.configure(background = "black")

root.bind("x",quit) # Making the "x" key quit the program
root.after(1000, showTime)

# Creating the text in the GUI
fnt = font.Font(family = "Century Gothic",size = 60, weight = "normal")
txt = StringVar()
label = ttk.Label(root,textvariable = txt,foreground = "#F3A9EC",background = "black",font = fnt)
label.place(relx = 0.5,rely = 0.5,anchor = CENTER)

root.mainloop() # Running the GUI
