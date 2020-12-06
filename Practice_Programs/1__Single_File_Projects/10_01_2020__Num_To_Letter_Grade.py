# PROGRAM NAME: 10_01_2020__Num_To_Letter_Grade.py
# PROGRAM PURPOSE: To give a letter grade based on a numeric grade
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-01-2020
# PYTHON VER. USED: 3.8

# NOTE: !! This does not work for actual grades !!
# NOTE: !! This is for practice with if, elif, and else statements !!

grade = int(input("Please enter your numeric grade...  "))

# Starting grade if statements
if grade >= 90:
    print("You have an A!")
    print("Congratulations! Good job!!")
elif grade >= 80:
    print("You have a B!")
    print("Congratulations!")
elif grade >= 70:
    print("You have a C!")
    print("Don't stress, you got this!")
elif grade >= 60:
    print("You have a D!")
    print("Don't stress, you got this!")
else:
    print("You have an F...")
    print("If you work hard, you can get there!")
# End of grade if statements
