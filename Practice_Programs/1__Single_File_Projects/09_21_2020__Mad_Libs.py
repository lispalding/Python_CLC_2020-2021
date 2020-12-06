# PROGRAM NAME: Lisette_Spalding__Mad_Libs__09-21-2020.py
# PROGRAM PURPOSE: To create a Mad Lib off of user input.
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 09-21-2020
# PYTHON VER. USED: 3.8

# CREDITS FOR MAD LIB LYRICS: The Shrek Trasnscript

# Getting user input for the Mad Lib
princess = input("Please enter whether you want a prince or princess: ")
she = input("Please enter a pronoun for your prince/princess: ")
her = input("Please enter the complementary pronoun: ")
enchantment = input("Please enter a magical ailment: ")
castle = input("Please enter something that you could lock someone in: ")
dragon = input("Please enter a type of monster: ")
knights = input("Please enter something chivalrous: ")
tower = input("Enter something tall that's in your prison: ")
laughing = input("Enter a sound a human can produce: ")
toilet = input("Enter something that can make a loud sound: ")
roll = input("Enter something that a bouncy ball can do: ")
tool = input("Enter something that is sharp: ")
dumb = input("Enter a way a person can look: ")
anL = input("Enter a letter: ")
runnin = input("Enter a way to move fast: ")
fun = input("Enter a reason to live: ")
glow = input("Enter a word to describe something bright: ")
play = input("State something that you do for fun: ")
paid = input("State something that you enjoy getting: ")
cool = input("Enter a word that means cold: ")
thin = input("Enter a word to describe something skeletal: ")

# Printing the Mad Lib

text = str.format('''Once upon a time there was a lovely {0}. But {1} had an {3} upon {2} of a fearful sort which could only be broken by love's first  kiss.
She was locked away in a {4} guarded by a terrible fire-breathing {5}.
Many brave {6} had attempted to free {2} from this dreadful prison, but none prevailed.
{1} waited in the {5}'s keep in the highest room of the tallest {7} for {2} true love and true love's first kiss.
[ {8} ]
Like that's ever gonna happen.
[ Paper rustling {9} flushing ]
What a load of -
Somebody once told me that the world is gonna {10} me
I ain't the sharpest {11} in the shed
She was lookin' kind of {12} with her finger and her thumb
In the shape of an {13} on her forehead
The years start comin' and they don't stop comin'
Fed to the rules and hit the ground {14}
Didn't make sense not to live for {15}
Your brain gets smart but your head gets {12}
So much to do so much to see
So what's wrong with takin' the backstreets
You'll never know if you don't go
You'll never shine if you dont {16}
Hey, now you're an all-star
Hey, now you're a rock star
Get the show on, get {17}
And all that glitter is gold
Only shootin' stars break the mold
It's a {18} place and they only say it gets {18}er
You're bundled up now but wait till you get older
But the meteor men beg to differ
judging by the hole in the satellite picture
The ice we skate is gettin' pretty {19}''',princess,she,her,enchantment,castle,dragon,knights,tower,laughing,toilet,roll,tool,dumb,anL,fun,glow,play,paid,cool,thin)
print(text)
print("\n")
print("CREDIT: The Shrek Transcript")

# Commenting out my previous code...
# I'm using commas because I don't want to add spaces...

##print("Once upon a time there was a lovely",princess,". But she had an",enchantment,"upon her of a fearful sort which could only be broken by love's first kiss.")
##print("She was locked away in a",castle," guarded by a terrible fire-breathing",dragon,".")
##print("Many brave",knights,"had attempted to free her from this dreadful prison, but none prevailed.")
##print("She waited in the",dragon+"'s","keep in the highest room of the tallest",tower," for her true love and true love's first kiss.")
##print("[",laughing,"]")
##print("Like that's ever gonna happen.")
##print("[ Paper rustling,",toilet,"flushing ]")
##print("What a load of -")
##print("Somebody once told me the world is gonna",roll,"me")
##print("I ain't the sharpest",tool,"in the shed")
##print("She was lookin' kind of",dumb,"with her finger and her thumb")
##print("In the shape of an",anL,"on her forehead")
##print("The years start comin' and they don't stop comin'")
##print("Fed to the rules and hit the ground",runnin)
##print("Didn't make sense not to live for",fun)
##print("Your brain gets smart but your head gets",dumb)
##print("""So much to do so much to see
##So what's wrong with takin' the backstreets
##You'll never know if you don't go""")
##print("You'll never shine if you don't",glow)
##print("Hey, now You're an all-star")
##print("Get your game on, go",play)
##print("Hey, now You're a rock star")
##print("Get the show on, get",paid)
##print("""And all that glitters is gold
##Only shootin' stars break the mold""")
##print("It's a",cool,"place and they say it gets",cool+"er")
##print("""You're bundled up now but wait till you get older
##But the meteor men beg to differ
##Judging by the hole in the satellite picture
##The ice we skate is gettin' pretty""",thin)
##print("\n")
##print("CREDIT: The Shrek Transcript")
