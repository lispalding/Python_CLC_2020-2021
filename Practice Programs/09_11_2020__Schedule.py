<<<<<<< HEAD
=======
<<<<<<< HEAD:09_11_2020__Schedule__Spalding_Lisette.py
>>>>>>> 946dbfaeb60afb76eaef4a6b9622f31d4dd810c3
# Program made by: Lisette Spalding
# Date created: 09-11-2020
# Date last modified: 09-12-2020
# File name: Lisette_Spalding__Schedule__09-11-2020.py
# Purpose: To print my school schedule

# NOTE: !! Please make sure to run this in Windows Command Prompt !!

# This will check to see if you have the appropriate module
# Because I wanted to add some colorful flair!
try:
   import colorama
except ImportError:
   print("!!Error!!")
   print("Module Colorama is required!! Please install Colorama from\
PyPI by using the command 'pip install colorama'. Thank you!")
   print("Please use the Window's Command Prompt as well...")

import sys
# This is importing necessary elements from the Python "Colorama" module
from colorama import init, AnsiToWin32, Fore, Back, Style
init(strip=False, convert=True)
# strip=False -->
# Is stating that the formatting will not be stripped at the command prompt
# convert=True -->
# Is stating that the ANSI Escape color codes are going to be converted to Windows Command Prompt Codes

print(Fore.RED + Style.DIM + "Lisette Spalding's School Schedule")
# I'm doing my School Schedule because my daily life is boring...
print(Fore.RED + Style.DIM + "Tooele High School & Community Learning\
 Center")

print(Fore.WHITE + "-------------------------")

print(Fore.GREEN + Style.BRIGHT + "Semester One")
print(Fore.WHITE + "----------------->>")
print(Fore.YELLOW + Style.NORMAL + "Purple Days (Hours 1-5)")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining variable table
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")


table = [["Hour", "Start Time to End Time", "Class", "Teacher"], # Content of table
         ["---", "---", "---", "---"],
         ["1st", "8:00 AM - 9:10 AM", "E.T.A. (Study Hall)", "Mr. VanDerwerken"],
         ["2nd", "9:15 AM - 10:25 AM", "Business Web Design", "Mr. Squire"],
         ["3rd", "10:30 AM - 11:40 AM", "Psychology 1010", "Ms. Perkova-Johnson"],
         ["4th & 5th", "11:45 AM - 2:15 PM", "Programming Python", "Mr. Broadbent"]]

print_table(table)

# These are to break up the tables -->
print(Fore.CYAN + Style.BRIGHT + "-------------------------")
print("-------------------------")

# Back to the table(s)!

print(Fore.YELLOW + Style.NORMAL + "White Days (Hours 6-10")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining table...
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")

table = [["Hour", "Start Time to End Time", "Class", "Teacher"], #Content of table
         ["---", "---", "---", "---"],
         ["6th", "8:00 AM - 9:10 AM", "Precalculus", "Ms. Bates"],
         ["7th", "9:15 AM - 10:25 AM", "Economics", "Mr. Nielson"],
         ["8th", "10:30 AM - 11:40 AM", "Honors Chemistry", "Mr. Comp"],
         ["9th & 10th", "11:45 AM - 2:15 PM", "A+ Computer Repair", "Mr. Thomsen"]]

print_table(table)

# Spacing things out for next Semester Schedule
print('\n') # '\n' defines a space
print(Fore.CYAN + Style.BRIGHT + "------------------------------")
print("--------------<>--------------")
print("------------------------------")
print('\n')

print(Fore.GREEN + Style.BRIGHT + "Semester Two")
print(Fore.WHITE + "----------------->>")
print(Fore.YELLOW + Style.NORMAL + "Purple Days (Hours 1-5)")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining table
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")

table = [["Hour", "Start Time to End Time", "Class", "Teacher"], #Content of table
         ["---", "---", "---", "---"],
         ["1st", "8:00 AM - 9:10 AM", "Business Management", "Ms. Jackson"],
         ["2nd", "9:15 AM - 10:25 AM", "English 1010", "Mr. Hamm"],
         ["3rd", "10:30 AM - 11:40 AM", "Political Science 1100", "Mr. Yonk (Presumably)"],
         ["4th & 5th", "11:45 AM - 2:15 PM", "Programming Python", "Mr. Broadbent"]]

print_table(table)

# These are to break up the tables -->
print(Fore.CYAN + Style.BRIGHT + "-------------------------")
print("-------------------------")

# Back to the table(s)!

print(Fore.YELLOW + Style.NORMAL + "White Days (Hours 6-10)")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining table again...
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")

table = [["Hour", "Start Time to End Time", "Class", "Teacher"], #Content of Table
         ["---", "---", "---", "---"],
         ["6th", "8:00 AM - 9:10 AM", "Precalculus", "Ms. Bates"],
         ["7th", "9:15 AM - 10:25 AM", "Civil Humanities 1320", "Unknown (USU Staff)"],
         ["8th", "10:30 AM - 11:40 AM", "Honors Chemistry", "Mr. Comp"],
         ["9th & 10th", "11:45 AM - 2:15 PM", "A+ Computer Repair", "Mr. Thomsen"]]

print_table(table)
<<<<<<< HEAD
=======
=======
# Program made by: Lisette Spalding
# Date created: 09-11-2020
# Date last modified: 09-12-2020
# File name: Lisette_Spalding__Schedule__09-11-2020.py
# Purpose: To print my school schedule

# NOTE: !! Please make sure to run this in Windows Command Prompt !!

# This will check to see if you have the appropriate module
# Because I wanted to add some colorful flair!
try:
   import colorama
except ImportError:
   print("!!Error!!")
   print("Module Colorama is required!! Please install Colorama from\
PyPI by using the command 'pip install colorama'. Thank you!")
   print("Please use the Window's Command Prompt as well...")

import sys
# This is importing necessary elements from the Python "Colorama" module
from colorama import init, AnsiToWin32, Fore, Back, Style
init(strip=False, convert=True)
# strip=False -->
# Is stating that the formatting will not be stripped at the command prompt
# convert=True -->
# Is stating that the ANSI Escape color codes are going to be converted to Windows Command Prompt Codes

print(Fore.RED + Style.DIM + "Lisette Spalding's School Schedule")
# I'm doing my School Schedule because my daily life is boring...
print(Fore.RED + Style.DIM + "Tooele High School & Community Learning\
 Center")

print(Fore.WHITE + "-------------------------")

print(Fore.GREEN + Style.BRIGHT + "Semester One")
print(Fore.WHITE + "----------------->>")
print(Fore.YELLOW + Style.NORMAL + "Purple Days (Hours 1-5)")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining variable table
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")


table = [["Hour", "Start Time to End Time", "Class", "Teacher"], # Content of table
         ["---", "---", "---", "---"],
         ["1st", "8:00 AM - 9:10 AM", "E.T.A. (Study Hall)", "Mr. VanDerwerken"],
         ["2nd", "9:15 AM - 10:25 AM", "Business Web Design", "Mr. Squire"],
         ["3rd", "10:30 AM - 11:40 AM", "Psychology 1010", "Ms. Perkova-Johnson"],
         ["4th & 5th", "11:45 AM - 2:15 PM", "Programming Python", "Mr. Broadbent"]]

print_table(table)

# These are to break up the tables -->
print(Fore.CYAN + Style.BRIGHT + "-------------------------")
print("-------------------------")

# Back to the table(s)!

print(Fore.YELLOW + Style.NORMAL + "White Days (Hours 6-10")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining table...
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")

table = [["Hour", "Start Time to End Time", "Class", "Teacher"], #Content of table
         ["---", "---", "---", "---"],
         ["6th", "8:00 AM - 9:10 AM", "Precalculus", "Ms. Bates"],
         ["7th", "9:15 AM - 10:25 AM", "Economics", "Mr. Nielson"],
         ["8th", "10:30 AM - 11:40 AM", "Honors Chemistry", "Mr. Comp"],
         ["9th & 10th", "11:45 AM - 2:15 PM", "A+ Computer Repair", "Mr. Thomsen"]]

print_table(table)

# Spacing things out for next Semester Schedule
print('\n') # '\n' defines a space
print(Fore.CYAN + Style.BRIGHT + "------------------------------")
print("--------------<>--------------")
print("------------------------------")
print('\n')

print(Fore.GREEN + Style.BRIGHT + "Semester Two")
print(Fore.WHITE + "----------------->>")
print(Fore.YELLOW + Style.NORMAL + "Purple Days (Hours 1-5)")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining table
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")

table = [["Hour", "Start Time to End Time", "Class", "Teacher"], #Content of table
         ["---", "---", "---", "---"],
         ["1st", "8:00 AM - 9:10 AM", "Business Management", "Ms. Jackson"],
         ["2nd", "9:15 AM - 10:25 AM", "English 1010", "Mr. Hamm"],
         ["3rd", "10:30 AM - 11:40 AM", "Political Science 1100", "Mr. Yonk (Presumably)"],
         ["4th & 5th", "11:45 AM - 2:15 PM", "Programming Python", "Mr. Broadbent"]]

print_table(table)

# These are to break up the tables -->
print(Fore.CYAN + Style.BRIGHT + "-------------------------")
print("-------------------------")

# Back to the table(s)!

print(Fore.YELLOW + Style.NORMAL + "White Days (Hours 6-10)")
print(Fore.BLUE + Style.BRIGHT)

def print_table(table): # Defining table again...
    col_width = [max(len(str(x)) for x in col) for col in zip(*table)]
    for line in table:
        print("| " + " | ".join("{:{}}".format(x, col_width[i])
                                for i, x in enumerate(line)) + " |")

table = [["Hour", "Start Time to End Time", "Class", "Teacher"], #Content of Table
         ["---", "---", "---", "---"],
         ["6th", "8:00 AM - 9:10 AM", "Precalculus", "Ms. Bates"],
         ["7th", "9:15 AM - 10:25 AM", "Civil Humanities 1320", "Unknown (USU Staff)"],
         ["8th", "10:30 AM - 11:40 AM", "Honors Chemistry", "Mr. Comp"],
         ["9th & 10th", "11:45 AM - 2:15 PM", "A+ Computer Repair", "Mr. Thomsen"]]

print_table(table)
>>>>>>> a3c346b5b89239e7ca7f733f2e3674ccffe3fb31:Lisette_Spalding__Schedule__09-11-2020.py
>>>>>>> 946dbfaeb60afb76eaef4a6b9622f31d4dd810c3
