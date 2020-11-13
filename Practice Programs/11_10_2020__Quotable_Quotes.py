# PROGRAM NAME: 11_10_2020__Quotable_Quotes.py
# PROGRAM PURPOSE: To print a quote !! THIS PROGRAM IS FUNCTION PRACTICE !!
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 11-10-2020
# PYTHON VER. USED: 3.8

import random

def selectQuote():
    # Setting up a tuple that contains my quotes
    quotes = ("My fake plants died because I did not pretend to water them - Mitch Hedberg", \
              "There can not be a crisis next week. My schedule is already full. - Henery Kissinger", \
              "Weather forecast for tonight: Dark.  - George Carlin", \
              "All generalizations are false, including this one. - Mark Twain", \
              "Why do they call it rush hour when nothing moves? - Robin Williams")

    # Making a variable to number the quotes in the tuple "quotes" & Indexing that
    numQuotes = len(quotes)
    index = random.randrange(0,numQuotes)

    print(quotes[index])
    return

selectQuote()
selectQuote()
