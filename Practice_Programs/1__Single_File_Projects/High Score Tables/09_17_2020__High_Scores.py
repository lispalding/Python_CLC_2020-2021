# PROGRAM NAME: Lisette_Spalding__Player_High_Score__09-17-2020.py
# PROGRAM PURPOSE: To print (fake) player scores!
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 09-17-2020
# PYTHON VER. USED: Python 3.8.

# Declaring Variables

# Line Variables
highScoreLine = " ___________-<"
highScoreLine2 = ">-___________"
beforeGameLine = "|----------------+"
beforeGameLine2 = "+---------------|"
gameTitleLine = "|--------->>"
gameTitleLine2 = "<<----------|"
lineSplit = "|---------------------------------------|"
playerNameLine = "- SCORE: "
endLine = "|____________-<"
endLine2 = ">-____________|"

# Player Name Variables
# ... Yes I did use video game characters...
player0 = "Sho Terashima"
player1 = "Ryo Mikajime"
player2 = "Zen Kubota"
player3 = "Mamoru Ichiyo"
player4 = "Sachika Hirasaka"
player5 = "Haruto Higurashi"
player6 = "Minamo Setouchi"
player7 = "Rinko Susukino"
player8 = "Yuma Mashiro"
player9 = "Mirai"
#Goes all the way to 10

# Score Variables
score0 = 29869
score1 = 19362
score2 = 19061
score3 = 18552
score4 = 18511
score5 = 18300
score6 = 17956
score7 = 17505
score8 = 17400
score9 = 10600
# Goes all the way to 10

# Getting to the time-consuming way of doing things
# ...
print(highScoreLine,"High Scores",highScoreLine2)
print(lineSplit)
print(beforeGameLine,"For:",beforeGameLine2)
print(lineSplit)
# Hehe another reference -->
# (To same game that characters are from) -->
print(gameTitleLine,"Reckless Skies",gameTitleLine2)
print(lineSplit)
print(lineSplit)
print("| 1st)",player0,"---"+playerNameLine,str(score0),"|")
print(lineSplit)
print("| 2nd)",player1,"----"+playerNameLine,str(score1),"|")
print(lineSplit)
print("| 3rd)",player2,"------"+playerNameLine,str(score2),"|")
print(lineSplit)
print("| 4th)",player3,"---"+playerNameLine,str(score3),"|")
print(lineSplit)
print("| 5th)",player4,playerNameLine,str(score4),"|")
print(lineSplit)
print("| 6th)",player5,playerNameLine,str(score5),"|")
print(lineSplit)
print("| 7th)",player6,"-"+playerNameLine,str(score6),"|")
print(lineSplit)
print("| 8th)",player7,"--"+playerNameLine,str(score7),"|")
print(lineSplit)
print("| 9th)",player8,"----"+playerNameLine,str(score8),"|")
print(lineSplit)
print("| 10th)",player9,"----------"+playerNameLine,str(score9),"|")
print(lineSplit)
print(endLine,"See More?",endLine2) # I thought this would be a fun detail
