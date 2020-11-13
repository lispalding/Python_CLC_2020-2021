# PROGRAM NAME: Lisette.Spalding__High_Scores_2__09-23-2020.py
# PROGRAM PURPOSE: To print a high score chart
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 09-23-2020
# PYTHON VER. USED: Python 3.8

# Declairing players:
player0 = "| 1st) Sho Terashima"
player1 = "| 2nd) Ryo Mikajime"
player2 = "| 3rd) Zen Kubota"
player3 = "| 4th) Mamoru Ichiyo"
player4 = "| 5th) Sachika Hirasaka"
player5 = "| 6th) Haruto Higurashi"
player6 = "| 7th) Minamo Setouchi"
player7 = "| 8th) Rinko Susukino"
player8 = "| 9th) Yuma Mashiro"
player9 = "| 10th) Mirai"
# Goes all the way to ten (10)

# Declairing Score Variables
score0 = " SCORE: 29869 |"
score1 = " SCORE: 19362 |"
score2 = " SCORE: 19061 |"
score3 = " SCORE: 18552 |"
score4 = " SCORE: 18511 |"
score5 = " SCORE: 18300 |"
score6 = " SCORE: 17956 |"
score7 = " SCORE: 17505 |"
score8 = " SCORE: 17400 |"
score9 = " SCORE: 10600 |"
# Goes all the way to ten as well

# Declairing a line variable
line ="----------------------------------------------------------------"

# Printing the top of the table
print(str.format("{0:^63}","~ High Scores ~"))
print(str.format("{0:^65.50}",line))
print(str.format("{0:^23.10}{1:^10}{0:^23.10}",line,"GAME: Reckless Skies"))
print(str.format("{0:^65.57}",line))
print(str.format("{0:^28} | {1:>30}","| | | | Player Name","High Score |"))
print(str.format("{0:^65.57}",line))

# Printing the middle of the table

# Goes up to 20 Variables
# Each Player and Score are paired together
body = str.format("""{0:^28}{20:^.18}{1:^13}
{2:^28}{20:^.18}{3:^13}
{4:^25}{20:^.21}{5:^12}
{6:^28}{20:^.18}{7:^13}
{8:^31}{20:^.15}{9:^12}
{10:^31}{20:^.15}{11:^12}
{12:^31}{20:^.15}{13:^13}
{14:^29}{20:^.17}{15:^13}
{16:^28}{20:^.18}{17:^13}
{18:^21}{20:^.25}{19:^5}""",player0,score0,player1,score1,player2,score2,player3,score3,player4,score4,player5,score5,player6,score6,player7,score7,player8,score8,player9,score9,line)

print(body)

# Printing ending of table
print(str.format("{0:^65.57}",line))
