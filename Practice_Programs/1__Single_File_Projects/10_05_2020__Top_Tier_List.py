# PROGRAM NAME: 10_05_2020__Top_Tier_List.py
# PROGRAM PURPOSE: To print almost all of my favorite media (Video Games and Books)
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 10-07-2020
# PYTHON VER. USED: 3.8

# Making a list of my top games and books
topMedia = ["End Roll [Video Game]",
    "Fire Emblem: Three Houses [Video Game]",
    "Zanki Zero: Last Beginning [Video Game]",
    "Kingdom Hearts (Series) & The World Ends With You [Video Games]",
    "IB [Video Game]",
    "Dangan Ronpa (Series) [Video Game]",
    "Legend of Zelda (Series) [Video Game]",
    "Final Fantasy (Series) [Video Game]",
    "Resident Evil (Series) [Video Game]",
    "Mad Father & Miaso [Video Games]",
    "Borderlands (Series) [Video Game]",
    "Catherine: Full Body [Video Game]",
    "Zero Escape (Series) [VIdeo Game]",
    "Eragon (Series) [Book]",
    "Bioshock (Series) [Video Game]",
    "Witch's House [Video Game]",
    "Night Circus [Book]",
    "Your Turn To Die [Video Game]",
    "Horizon Zero Dawn [Video Game]",
    "HiveSwap: Act 1 [Video Game]",
    "Persona (Series) [Video Game]",
    "Lord of The Rings (Series) & The Hobbit [Books]",
    "Stiens;Gate [Video Game]",
    "Our World is Ended [Video Game]",
    "World of Warcraft [Video Game]"]

topMedia.append("World of Warcraft [Video Game]") # Appending (Adding) World of Warcraft to the end of the list

topMedia.sort() # Sorting the list alphabetically
topMedia.reverse() # Reversing the sort, so instead of smallest to largest it's largest to smallest.

# Adding two LoZ:Link to the Past
topMedia.insert(0, "Legend of Zelda: Link to the Past [Video Game]")
topMedia.insert(6, "Legend of Zelda: Link to the Past [Video Game]")

##print(topMedia.count("Legend of Zelda: Link to the Past")) # Counting how many LoZ: Link to the Past I have

game = topMedia.index("Legend of Zelda: Link to the Past [Video Game]",True) # Removes the last index position of LoZ:Link to the Past
removeGame = topMedia.pop(int(game)) # "Poping" out the Legend of Zelda: Link to the Past, and removing it

##print(topMedia.count("Legend of Zelda: Link to the Past")) # Counting how many LoZ: Link to the Past I have

newList = topMedia.copy() # Copying new list over to the variable newList

topMedia.clear() # Clearing old list...

# Printing both old list and new list
##print(topMedia)
##print(newList)

# !! GETTING TO GRADING PART !!

points = 0
if len(newList) >= 25:
    points += 25
    # print("Points added 1")
else:
    points -= 25

if not topMedia:
    points += 10
    # print("Points added 2")
else:
    points -= 10

if "World of Warcraft [Video Game]" in newList:
    points += 10
    # print("Points added 3")
else:
    points -= 10

if newList.count("Legend of Zelda: Link to the Past [Video Game]") > 1:
    points -= 5
else:
    points += 5
    # print("Points added 4")

if newList.index("Legend of Zelda: Link to the Past [Video Game]") == 0:
    points += 25
    # print("Points added 5")
else:
    points -= 25

if newList.count("World of Warcraft [Video Game]") > 1:
    points += 25
    # print("Points added 6")
else:
    points -= 25

for i in newList:
    if ("pokemon" in i) or ("Pokemon" in i):
        points -= 100
    if ("halo" in i) or ("Halo" in i):
        points -= 100
    if ("fortnite" in i) or ("Fortnite" in i):
        points -= 100000000
    if ("smash" in i) or ("Smash" in i):
        points -= 50
        
# Printing my score...
print(points)

# Creating If statements for letter grade
if points >= 90:
    print("You got an A")
elif points >= 80:
    print("You got a B")
elif points >= 70:
    print("You got a C")
elif points >= 60:
    print("You got a D")
else:
    print("You got a F")
