# PROGRAM NAME: 10_05_2020__mr_roboto.py
# PROGRAM PURPOSE: To demonstrate my understanding of classes
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 12-05-2020
# PYTHON VER. USED: 3.8

# Defining my class
class Robot:
    # Defining class variables
    name = "Mr. Roboto"
    thankYou = "Domo arigato"

    # Defining a class method
    def thanks():
        print(Robot.thankYou + ", " + Robot.name)

# Calling my class method, thanks
Robot.thanks()

# Changing class variables
Robot.thankYou = "Thankee Kindly"
Robot.name = "T-1000"

# Calling the class method again
Robot.thanks()
