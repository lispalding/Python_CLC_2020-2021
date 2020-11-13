# PROGRAM NAME: 10_21_2020__Calculating_A_Factorial.py
# PROGRAM PURPOSE: To calculate a factorial !! This proram is LOOP practice !!
# MADE BY: Lisette Spalding
# PYTHON VER. USED: 3.8

# Getting target number from the user
number = int(input("Enter a positive integer:  "))

# Initalizing the variable to hold factorial total
factorial = 1

# Looping one up through target number
for i in range(1, number+1):
    # Multiply factorial by loop index value
    factorial = factorial*i
    
# Printing final results
print("Factorial =",factorial)
