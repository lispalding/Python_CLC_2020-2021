# PROGRAM NAME: 11_23_2020__Car.py
# PROGRAM PURPOSE: To build my dream(?) car !! This is Object Oriented Programming Practice !!
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 11-23-2020
# PYTHON VER. USED: 3.8

# Defining a class named Car
class Car():
    # Creating a function to define the make of the car
    def __init__(self):
        self.make = input("Make of your dream car?  ")
        self.model = input("What is the model of your dream car?  ")
        self.year = input("What is the year of your dream car?  ")
        self.color = input("What is the color of your dream car?  ")
        self.bodyStyle = input("What is the body style of your dream car? ")
        self.numberWheels = input("How many wheels does your dream car have?  ")
        self.engine = Engine()
        self.topSpeed = 0

    # Creating a method for the Car class
    def drive(self):
        if self.engine.cyl == "8":
            self.topSpeed = 120
        elif self.engine.cyl == "6":
            self.topSpeed = 100
        else:
            self.topSpeed = 65
        
        print("This car can drive.")
        print("It's top speed is",self.topSpeed)
        
# Defining a class named Engine
class Engine():
    # Creating a functiion to define the engine
    def __init__(self):
        self.cyl = input("How many cylinders in your engine does your dream car have?  ")
        self.cylAlignment = input("Configuration of your engine?  ")
        self.fuelType = input("Gas or Diesel?  ")

# Defining a class that will print your car stuff


def main():
    # Defining my dream car...
    myDreamCar = Car()
    # Printing if my dream car can drive
    myDreamCar.drive()

main()
