# PROGRAM NAME: 11_09_2020__Scope_Practice.py
# PROGRAM PURPOSE: To experiment with the scope of a program...
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 11-09-2020
# PYTHON VER. USED: 3.7.8

##x = 10
##y = 100

##def test1 ():
##    x1 = x+1000
##    y1 = y+1000

##def test2():
##    global x
##    global y
##
##    x+=1000
##    y+=1000

##def test3():
##    x1 = x+1000
##    return x1

##def test4(x,y):
##    x = x+1000
##    return x

##def test5(x=42,y=52):
##    x = x+1000
##    y = y+1000
##    return x,y

##print(x,y)

##x = test5()
##x = test5(57)

##x, y = test5(y=57, x=12)

import datetime

def getDayOfTheWeek(target):
    try:
        thisDate = datetime.datetime.strptime(target,"%Y-%m-%d")
        dayOfWeek = thisDate.strftime("%A")
        return dayOfWeek
    except:
        return "Invalid YYYY-MM-DD date!"

print(getDayOfTheWeek("2002-11-05"))
