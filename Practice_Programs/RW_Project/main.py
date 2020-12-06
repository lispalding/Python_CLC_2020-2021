# PROGRAM NAME: main.py
# PROGRAM PURPOSE: To read a file
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 12-01-2020
# PYTHON VER. USED: 3.8

# Opening and closing files
## HOW TO: file = open("file location", "persmission")
## FILE LOCATION: C:\Users\lisette.spalding\Desktop\RW_Project\assets\saved_data\read_me.txt

print("Opening file...")
file = open("assets/saved_data/games_list.txt","w")

games = ["Zanki Zero: Last Beginning","Dangan Ronpa","Final Fantasy","End Roll","IB","Hiveswap & Hauntswitch",\
         "Fire Emblem: Three Houses","Kingdom Hearts","Zero Escape","Legend of Zelda"]
for i in range (len(games)):
    file.write(str(i+1)+" "+str(games[i])+"\n")
file.close()

file = open("assets/saved_data/games_list.txt","r")
text = file.readline()
if "Zanki Zero: Last Beginning" in text:
    print("Pass")
else:
    print("Big Fail.")

file.close()
