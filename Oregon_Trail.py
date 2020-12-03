# PROGRAM NAME: Oregon_Trail.py
# PROGRAM PURPOSE: To play Oregon Trail
# MADE BY: Lisette Spalding, Danson Coats, Hanna Kraemer
# DATE LAST MODIFIED: 12-03-2020
# PYTHON VER. USED: 3.8

def logoScreen():
    title = '''
   ___                     __ _                            _____                     _       _    
  / _ \     _ _    ___    / _` |   ___    _ _       o O O |_   _|    _ _   __ _     (_)     | |   
 | (_) |   | '_|  / -_)   \__, |  / _ \  | ' \     o        | |     | '_| / _` |    | |     | |   
  \___/   _|_|_   \___|   |___/   \___/  |_||_|   TS__[O]  _|_|_   _|_|_  \__,_|   _|_|_   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' '''
    
    logo = """
MMMMMMMMMMMMMMMMWNKxlc:;;,,;:dXWMMMMMMMMMMMMMMWXl,,cKWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWN0d:,,,;;cONWMMMMMMMMMMWWWWO;.';lONMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMWXo,,,;;:oKWMMMMWKkkkxl;;:;..''c0WMMMMMMMMMWWWWWWWWWWWWWWWW
MMMMMMMMMMMMMMMMMMMMMMXo,,,;;:ckNKkxo;.     'oOOl,,,c0WWMWWWNNK0Oxoooooooooooooo
MMMMMMMMMMMMMMMMMMMMMNk:,,,:l:'''.        'dXWWXl,,,;lkOOOxoolcccc:ccodddddddddd
MMMMMMMMMMMMMMMMMMMMMNd,,,',;.         .;l0XNNXkc,,,,;:ccldxxxkKKKKKKNWWWWWWWWWW
MMMMMMMMMMMMMMMMMMMMWNd,,..            ....',;;;,,;;,cOKKNWWWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMWXl..                       ...',c0WMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWXl.                             ..,oKWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMXc                                   ,OWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWo         .c;.     ....              ;KWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWWXc        ,oddo;.    .......      ... ;XMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWWXkdl'  ......lxddddoc;'.   .;lo:,,''',,' ;XMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWWXkol:::'..,,,,,;:llodddxddoc::;;::;;;,,,,,' ;XMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMWXkol::::::' .',,,,,,,,;:::lodoc::;,,,,,,,,,,,. ;XMMMMMMMMMMMMWK0XMMMMMM
MMMMMMWXkl:::::::lk:  .,,,,,,,,,,,,,cdl;,,,,,,,,,,,,,'. ,KMMMMMMMMMMMW0;,0MMMMMM
MMMMWXkl:::::::lkXWl  .,,,,,,,,,,,,,cdl;,,,,,,,,,,,,,'.  lNMMMMMMMMWXd'.lXMMMMMM
MMWXkl:::::::okXWMWO'  .,,,,,,,,,;;;cdoc:;;,,,,,,,,,,'.  :XMMMMMMMNx'  ;0MMMMMWN
WXkl:::::::oOXWMMMMWl  .,,,,,;;:cloddddddoolclc::;,''.   :XMMMMMWKo.  .xWMWWNKOo
Ol:;:::::ckXWMMMMMMWl  .''',:lodddddddddddddddddo,.      :XMMMMKo.   .lXMWN0dc::
c:::::::oONMMMMMMMMWl       .cddddddddddddddddc,.        :NMMWK;     ;0NKOdc::::
:::::::dKWMMMMMMMMMWl         .':::ldddddl::,..          :XWKo.     .d0dc:::::::
:::::ckXWMMMMMMMMMMWl              .......               :0o.      .;lc:::::::::
::::ckNWMMMMMMMMMMMWl                     ....           ',        .,::::::::::l
::::xNMMMMMMMMMMMMMWl             .,;,;cc;'''...                   ';:::::::clkX
:::l0WMMMMMMMMMMMMMWl             'oo;..'.';coxd;.                .;::::::lx0XWM
:::kNWMMMMMMMMMNKKK0:              ..';cooxkkkkkxd:.              ':::::lkKWWWMM
...;cclllllllll;....               'oxxkkkkkxollllc:'.           .;:::lkXWMMMMMM
.                                  ,dkkkkkxo::cllllc:,..        .,::lkXWMMMMMMMM
,'...                              .cxkkkkxc;okkkkkxdol:'..     .,,:dkOOOOOOOOOO
:::ldd:'.                           ,dkkkkxc;lxkkkxkkkkxlll;.           .....'''
::::xXWNOdc'.                       .:xkxkxo;;lxkkkxkkkkxxkdc.        ...'',,,,,
::::cOWMMMWNOOd:'.                   .lxxxdl:;:oxkkkkkkxdol:;.    ...',,,,,,,,,,
:::::lkNWMMMMMMMX0Ok,                 'clcccodxxxkkxdolc::clc. ...,,,,,,,,,,,,,,
::::::cxKNWMMMMMMNO:.                 .;odxkxkxxdolc:;:ldxko,..,,,,,,,,,,,,,,,,,
::::::::cokKXXXXk:.                    ,odkkxdo:;;:lddxxxxo:,,,,,,,,,,,,,,,,,,,,
:::::::::::clc;'.                      ..;do:::cldxxkxdlc:;,,,,,,,,,:oc;,,,,,,,,
::::::::::;,'.                           .,:cdxxkkxdlc;,,,,,,,,,,,:dKNXklccc:,,,
::::::::;;'.                              ;xxxkxdlc;,,,,,,,,,,,:lxKWWMMWNNNNKx:,
::::::::,.                 .              'okxdl:,,,,,,,,,,,,,;dXWWMMMMMMMMMWWx;"""
    companyName = '''Radical Cookies'''
    trademark = "TM"

    print("\t\t\t",title)
    print(logo)
    print("\t\t\t\t",companyName,trademark)

logoScreen()

def mainDisplay():
    """Creates the main display. To use: mainDisplay() """
    
title = '''
   ___                     __ _                            _____                     _       _    
  / _ \     _ _    ___    / _` |   ___    _ _       o O O |_   _|    _ _   __ _     (_)     | |   
 | (_) |   | '_|  / -_)   \__, |  / _ \  | ' \     o        | |     | '_| / _` |    | |     | |   
  \___/   _|_|_   \___|   |___/   \___/  |_||_|   TS__[O]  _|_|_   _|_|_  \__,_|   _|_|_   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' '''
         # This is the main Display Screen
print(title)

def menuChoices(options):
    """Creates a menu. To use: menuChoices(options) """
    
    # Creating a choice menu base that we can call to
    index = 1
    print("\n")
    for i in options:
        print(str.format("{}................{}",index,i))
        index+=1
        
    while True:
        userChoice = input("What do you wish to do?  ")
        if userChoice.isnumeric():
            userChoice = int(userChoice)
            if userChoice >= 1 and userChoice <= len(options):
                return userChoice
            else:
                print("Not valid...")
        else:
            print("Enter a number...")
    

def mainMenu():
    """ Runs the main menu. To use: mainMenu() """

    mainDisplay()

    while True:
        options = ["Play Game","Learn About Oregon Trail","Quit"]   # Defining what will go into the menu 
        userChoice = menuChoices(options) # Calling to menuChoices

        if userChoice == 1:
            play()
            break
        elif userChoice == 2:
            learn()
        else:
            quit
            break

def learn():
    """ Learning about the trail. To use: learn() """
    
    page =  ("Take a journey by covered wagon across 2000 miles of plains, rivers, and mountains. \
On the plains you will slosh your oxen through mud and water filled ruts or will you plod through dust six inches deep", \
             "How will you cross the rivers, how will you spend yoru money? How will you use supplies? \
It's all up to you to make the choice..."\
             , "You will face many challenges from theives to disease, and many other challenges.\
If you fail, try and try again til you succeed.")
    for i in page:
        print(i)
        input("\nPress enter to go on...\n")
    
def charCreate():
    """ Runs and creates the Wagon Leader. Determines profession and money. To use: charCreate() """
    
    options = ["Banker", "Carpenter", "Farmer", "Display Differences"] # Listing the menu options

    while True:
        userChoice = menuChoices(options)
        # Defining what each choice will do! Becuase each choice affects the game.
        if userChoice == 1:
             prof = "Banker"
             money = 1600
             return prof, money
             break
        elif userChoice == 2:
             prof = "Carpenter"
             money = 800
             return prof, money
             break
        elif userChoice == 3:
            prof = "Farmer"
            money = 400
            return prof, money
            break
        elif userChoice == 4:
            # This is the "Display Differences" option
            print('''\n\t\tA banker is rich and has $1600.
            \tA Carpenter is middle class and has $800.
            \tA Farmer is poor and has $400.''')
            
        else:
            print("Sorry, that is not an option.")

def getName(question):
    """ Runs and gets names. To use: getName() """
    
    while True:
        name = input(question) # Getting family memeber names
        if name == name.isnumeric: # Making sure that the name is numeric
             print("Not valid!!")
        elif len(name) > 1:
            return name
            break 
        else:
            print("Not valid!!")

def familySetup(): # Setting up the family
    """ Runs and gets family members' names. To use: familySetup() """
    
    familyMembers = []
    wagonLeader = getName(question="What is the name of your wagon leader?  ")
    familyMem = getNumber(high=7,low=5,question="You need at 5-7 family memebers... How many do you have?  ")
    for i in range(familyMem):
        name = getName(question="What is the name of your family members?  ")
        familyMembers.append(name)
    return familyMembers, wagonLeader
    

def getNumber(high,low,question): # Defining the high and low values with high=7 and low=5
    """ Runs and gets a good number. To use: getNumber(high,low,question) """
    
    while True:
        number = input(question)
        if number.isnumeric():
            number = int(number)
            if (number >= low) and (number <= high):
                # Making sure that the number is greater than or equal to 5
                # Making sure that the number is less than or equal to 7
                return number
                break
            else:
                print("Not valid input!")
        else: 
            print("Not valid!")

def  shop(money,food,ammo,clothes,oxen,parts):
    """ Runs the shop. To use: shop(money,food,ammo,clothes,oxen,parts) """
    
    # Defining the things needed in the stores
    ammo = 0
    food = 0
    clothes = 0
    oxen = 0
    parts = []
    bill = 0
    items = ["Oxen","Food","Clothes","Ammunition","Wagon Parts","Check Out"]
    moneySpent = [0.00,0.00,0.00,0.00,0.00,bill]

    while True:
        moneySpent[len(items)-1] = bill
        print("\n Welcome to the store!")
        print("Here is the list of things you can buy:")

        print("=====================================================")
        for i in range(len(items)):
            print(str.format("\t{}:     {:20}     ${:.2f}",i+1,items[i],moneySpent[i]))
            
        print(str.format("Total bill so far:     ${:.2f}",bill))
        print(str.format("Total funds available: ${:.2f}",money-bill))
        print("=====================================================")
        
        choice = getNumber(len(items),1,question="What do you want to buy?")

        if choice == 1:
            # Resetting the money spent on this if the menu is acessed twice
            bill -= moneySpent[0]
            oxen = 0
            moneySpent[0] = 0.00

            # Printing the menu
            print('''There are two oxek in a yoke; I reccomend at least three yokes. I charge 40$ a yoke.''')
            print(str.format("Total bill so far:     ${:.2f}", bill))

            # Updating variables
            answer = getNumber(high=5,low=1,question="\nHow many yokes do you want?")
            cost = answer*40
            bill += cost
            oxen = answer*2
            moneySpent[0] = cost
            
        elif choice == 2:
            # Resetting the money spent on this if the menu is acessed twice
            bill -= moneySpent[1]
            food = 0
            moneySpent[1] = 0.00

            # Printing menu
            print("I recommend that you take 200 pounds of food per family member for this trip.")
            print("\n I price 20 cents per pound..")
            print(str.format("Total bill so far:     ${:.2f}", bill))

            # Updating variables
            answer = getNumber(high=1450,low=1,question="\nHow many pounds of food do you want? (1-1450)  ")
            cost = answer*.20
            bill += cost
            food = answer
            moneySpent[1] = cost
            
        elif choice == 3:
            # Resetting the money spent on this if the menu is acessed twice
            bill -= moneySpent[2]
            clothes = 0
            moneySpent[2] = 0.00

            # Printing Menu
            print("The mountains will be cold, and I reccomend 2 sets of clothes per person. I charge $10 per set.")
            print(str.format("Total bill so far:     ${:.2f}", bill))

            #Updating variables
            answer = getNumber(high=20,low=0,question="\nHow many sets of clothes do you want?  ")
            cost = answer*10
            bill += cost
            clothes = answer
            moneySpent[2] = cost
            
        elif choice == 4:
            # Resetting the money spent on this if the menu is acessed twice
            bill -= moneySpent[3]
            ammo = 0
            moneySpent[3] = 0.00

            # Printing the menu
            print("I sell ammunition in boxes of 20 bullets. Each box costs $2.00.")

            # Updating variables
            answer = getNumber(high=30,low=0,question="\nHow many boxes do you want?  ")
            cost = answer*2
            bill += cost
            ammo = answer
            moneySpent[3] = cost
            
        elif choice == 5:

            # Printing the welcome screen
            print("It is a good idea to have a few spare parts for your wagon on hand... A broken wagon can be a death sentence.")

            # Setting variables
            partsBill = 0.00
            inventory = ["Wagon Wheel","Wagon Axle","Wagon Tongue","Back to main shop"]
            partsCost = [10.00,20.00,50.00,partsBill]

            while True:
                partsCost[len(partsCost)-1] = partsBill
                print("Here is the list of things you can buy...")
                item = menuChoices(inventory)
                
                if item == 1:
                    answer = answer = getNumber(high=6,low=0,question="\nHow many wagon wheels do you want? (0-6)   ")
                    for i in range(answer):
                        parts.append("Wagon Wheel")
                    partsBill += partsCost[0]*answer
                elif item == 2:
                    answer = getNumber(high=6,low=0,question="\nHow many wagon axles do you want? (0-6)    ")
                    for i in range(answer):
                        parts.append("Wagon Axle")
                    partsBill += partsCost[1]*answer
                elif item == 3:
                    answer = getNumber(high=6,low=0,question="\nHow many wagon tongues do you want? (0-6)   ")
                    for i in range(answer):
                        parts.append("Wagon Tongue")
                    partsBill += partsCost[2]*answer
                else:
                    bill += partsBill
                    moneySpent[4] = partsBill
                    break
            
        elif choice == 6:
            # Printing the store checkout
            print(str.format("You have spent:     ${:.2f}", bill))
            correct = input("Is this correct?   ")

            # Making sure that the user approves of their purchases
            if ("y" in correct) or ("Y" in correct):
                if (money == moneySpent) or (money > moneySpent[0]):
                    money = money-moneySpent[0]
                    
                    return money,food,ammo,clothes,oxen,parts
                else:
                    print("This isn't valid... You've spent more money than you have!")
            else:
                print("Back to the store then!")
        else:
            print("Invalid input!")
    

def changeRations(currentRations):
    """ Determines rations. To use: changeRations(currentRations) """
    
    # Variables
    rations = ["Filling", "Meager", "Bare Bones"]
    currentRations = ""

    # Printing the current rations
    print(currentRations)

    # Creating a loop so if invalid input is entered, the menu keeps on appearing
    while True:
        userChoice = menuChoices(rations)
    
        # Creating if statements to return what the user desires
        if userChoice == 1:
            currentRations = "Filling"
            return currentRations
        elif userChoice == 2:
            currentRations = "Meager"
            return currentRations
        elif userChoice == 3:
            currentRations = "Bare Bones"
            return currentRations
        else:
            print("You can't do that!\n")

def changePace(currentPace):
    """ Determines the current pace. To use: changePace(currentPace) """
    
    # Variables
    pace = ["Slow","Normal","Fast"]

    while True:
        choice = menuChoices(pace)
        print(currentPace)

        # Creating if statements to return what the operator desires
        if choice == 1:
            currentPace = "Slow"
            return currentPace
        elif choice == 2:
            currentPace = "Normal"
            return currentPace
        elif choice == 3:
            currentPace = "Fast"
            return currentPace
        else:
            print("That is not an option!")


def rest(currentRations,hp):
    """ Determines how much health is restored by rest. To use: rest(currentRations,currentHealth) """
    
    # Variables
    healthMod = 0

    # Calling the getNumber variable to get a good number on how many days the user wants....
    numDays = getNumber(10,0,"How many days do you want to rest? (Only 0-10)  ")

    # Making sure that the user picks something
    if (currentRations == "Filling"):
        healthMod = 2
    elif (currentRations == "Meager"):
        healthMod = 1
    elif (currentRations == "Bare Bones"):
        healthMod = 5

    healthGain = 10*healthMod*numDays

    if (healthGain+hp > 100):
        hp = 100
    else:
        currentHealth += healthGain
        round(currentHealth)

    print("Your health is at:",hp)
    return hp,numDays

def checkSupplies(money,oxen,food,ammo,clothes,parts):
    supplies = [money,oxen,food,ammo,clothes,parts]
    names = ["Money","Oxen","Food","Ammo","Clothes","Parts"]
    for i in range(len(supplies)):
        print(str.format("{} = {}",names[i],supplies[i]))
    input("Press a key")

def travel(health,currentPace,weather):
    """ Determines miles traveled. To use: travel(health,currentPace,weather) """
    
    # Setting up variables
    mph = 0
    hours = 0
    milesTravel = 0

    while True:
        # Setting up the pace effects
        if (currentPace == "Slow"):
            mph = 1
        elif (currentPace == "Normal"):
            mph = 2
        elif (currentPace == "Fast"):
            mph = 4
        else:
            print("Invalid pace.")

        # Setting up the health effects
        if (health == "Poor"):
            hours = 4
        elif (health == "Fair"):
            hours = 6
        elif (health == "Good"):
            hours = 8
        else:
            print("Invalid health.")

        # Weather effects
        if (weather == "Hot"):
            milesTravel = mph*hours*1
            return milesTravel
        elif (weather == "Cold"):
            milesTravel = mph*hours*.75
            return milesTravel
        elif (weather == "Rain"):
            milesTravel = mph*hours*.5
            return milesTravel
        elif (weather == "Snow"):
            milesTravel = mph*hours*0
            return milesTravel
        else:
            print("Invalid weather.")

def trade(food,ammo,clothes,oxen,parts):
    """ Starts the trading system... To use: trade(food,ammo,clothes,oxen,parts) """
    
    print("You're attempting to trade...")
    currentDate += datetime.timedelta(days = 1)
    food -= (len(familyMembers)+1)*rationsMod
    input("Press key to continue  ")

    options = ["ammunition","food","clothes","oxen","wagon wheel","wagon tongue","wagon axle"]
    thingWanted = random.choice(options)

    if thingWanted == "ammunition":
        thingNum = random.randint(10,40)
        # Removing "ammunition" from the options... !! This will reset next time they trade !!
        options.remove("ammunition")
        # Choosing the thing given
        thingGiven = random.choice(options)

        # Choosing the amount of the thing given
        if thingGiven == "food":
            thingNum2 = random.randint(5,200)
        elif thingGiven == "clothes":
            thingNum2 = random.randint(1,5)
        elif thingGiven == "oxen":
            thingNum2 = random.randint(1,3)
        elif thingGiven == "wagon wheel" or "wagon tongue" or "wagon axle":
            thingNum2 = "1"
        else:
            print("Invalid trade...")

        # Printing what they want and what player gets
        print("A traveler wants",thingWanted,"(",str(thingNum),")","and will give",thingGiven,"(",str(thingNum2),")","for it.")

        # Determining if you have enough
        if (ammo < thingNum):
            input("You do not have enough ammunition to do this trade... \n Press enter to continue...")
        else: # IF you have enough this happens
            choice = input("Will you do this trade?")
            if ("y" in choice) or ("Y" in choice):
                thingNum2 = int(thingNum2)
                thingNum -= ammo
                
                if thingGiven == "food":
                    food += thingNum2
                elif thingGiven == "clothes":
                    clothes += thingNum2
                elif thingGiven == "oxen":
                    oxen += thingNum2
                elif thingGiven == "wagon wheel":
                    parts.append("Wagon Wheel")
                elif thingGiven == "wagon tongue":
                    parts.append("Wagon Tongue")
                elif thingGiven == "wagon axle":
                    parts.append("Wagon Axle")
                else:
                    print("Invalid trade...")
                    
                print("Trade made! Press any key.  ")
            else:
                input("Back to the menu then! Press any key.  ")
        
    elif thingWanted == "food":
        thingNum = random.randint(5,200)
        # Removing "food" from the options... !! This will reset next time they trade !!
        options.remove("food")
        # Choosing the thing given
        thingGiven = random.choice(options)

        # Choosing the amount of the thing given
        if thingGiven == "ammunition":
            thingNum2 = random.randint(10,40)
        elif thingGiven == "clothes":
            thingNum2 = random.randint(1,5)
        elif thingGiven == "oxen":
            thingNum2 = random.randint(1,3)
        elif thingGiven == "wagon wheel" or "wagon tongue" or "wagon axle":
            thingNum2 = "1"
        else:
            print("Invalid trade...")

        # Printing what they want and what player gets
        print("A traveler wants",thingWanted,"(",str(thingNum),")","and will give",thingGiven,"(",str(thingNum2),")","for it.")

        # Determining if you have enough
        if (food < thingNum):
            input("You do not have enough food to do this trade... \n Press enter to continue...")
        else: # IF you have enough this happens
            choice = input("Will you do this trade?")
            if ("y" in choice) or ("Y" in choice):
                thingNum2 = int(thingNum2)
                thingNum -= food
                
                if thingGiven == "ammunition":
                    ammo += thingNum2
                elif thingGiven == "clothes":
                    clothes += thingNum2
                elif thingGiven == "oxen":
                    oxen += thingNum2
                elif thingGiven == "wagon wheel":
                    parts.append("Wagon Wheel")
                elif thingGiven == "wagon tongue":
                    parts.append("Wagon Tongue")
                elif thingGiven == "wagon axle":
                    parts.append("Wagon Axle")
                else:
                    print("Invalid trade...")
                    
                input("Trade made! Press any key.  ")
            else:
                input("Back to the menu then! Press any key.  ")
         
    elif thingWanted == "clothes":
        thingNum = random.randint(1,5)
        # Removing "clothes" from the options... !! This will reset next time they trade !!
        options.remove("clothes")
        # Choosing the thing given
        thingGiven = random.choice(options)

        # Choosing the amount of the thing given
        if thingGiven == "ammunition":
            thingNum2 = random.randint(10,40)
        elif thingGiven == "food":
            thingNum2 = random.randint(5,200)
        elif thingGiven == "oxen":
            thingNum2 = random.randint(1,3)
        elif thingGiven == "wagon wheel" or "wagon tongue" or "wagon axle":
            thingNum2 = "1"
        else:
            print("Invalid trade...")

        # Printing what they want and what player gets
        print("A traveler wants",thingWanted,"(",str(thingNum),")","and will give",thingGiven,"(",str(thingNum2),")","for it.")

        # Determining if you have enough
        if (clothes < thingNum):
            input("You do not have enough clothes to do this trade... \n Press enter to continue...")
        else: # IF you have enough this happens
            choice = input("Will you do this trade?")
            if ("y" in choice) or ("Y" in choice):
                thingNum2 = int(thingNum2)
                thingNum -= clothes
                
                if thingGiven == "ammunition":
                    ammo += thingNum2
                elif thingGiven == "food":
                    food += thingNum2
                elif thingGiven == "oxen":
                    oxen += thingNum2
                elif thingGiven == "wagon wheel":
                    parts.append("Wagon Wheel")
                elif thingGiven == "wagon tongue":
                    parts.append("Wagon Tongue")
                elif thingGiven == "wagon axle":
                    parts.append("Wagon Axle")
                else:
                    print("Invalid trade...")
                    
                input("Trade made! Press any key.  ")
            else:
                input("Back to the menu then! Press any key.  ")
        
    elif thingWanted == "oxen":
        thingNum = random.randint(1,3)
        # Removing "oxen" from the options... !! This will reset next time they trade !!
        options.remove("oxen")
        # Choosing the thing given
        thingGiven = random.choice(options)

        # Choosing the amount of the thing given
        if thingGiven == "ammunition":
            thingNum2 = random.randint(10,40)
        elif thingGiven == "food":
            thingNum2 = random.randint(5,200)
        elif thingGiven == "clothes":
            thingNum2 = random.randint(1,5)
        elif thingGiven == "wagon wheel" or "wagon tongue" or "wagon axle":
            thingNum2 = "1"
        else:
            print("Invalid trade...")

        # Printing what they want and what player gets
        print("A traveler wants",thingWanted,"(",str(thingNum),")","and will give",thingGiven,"(",str(thingNum2),")","for it.")

        # Determining if you have enough
        if (oxen < thingNum):
            input("You do not have enough clothes to do this trade... \n Press enter to continue...")
        else: # IF you have enough this happens
            choice = input("Will you do this trade?")
            if ("y" in choice) or ("Y" in choice):
                thingNum2 = int(thingNum2)
                thingNum -= oxen
                
                if thingGiven == "ammunition":
                    ammo += thingNum2
                elif thingGiven == "food":
                    food += thingNum2
                elif thingGiven == "clothes":
                    clothes += thingNum2
                elif thingGiven == "wagon wheel":
                    parts.append("Wagon Wheel")
                elif thingGiven == "wagon tongue":
                    parts.append("Wagon Tongue")
                elif thingGiven == "wagon axle":
                    parts.append("Wagon Axle")
                else:
                    print("Invalid trade...")
                    
                input("Trade made! Press any key.  ")
            else:
                input("Back to the menu then! Press any key.  ")
            
    elif thingWanted ==  "wagon wheel":
        thingNum = random.randint(1,3)
        # Removing "wagon wheel" from the options... !! This will reset next time they trade !!
        options.remove("wagon wheel")
        # Choosing the thing given
        thingGiven = random.choice(options)

        # Choosing the amount of the thing given
        if thingGiven == "ammunition":
            thingNum2 = random.randint(10,40)
        elif thingGiven == "food":
            thingNum2 = random.randint(5,200)
        elif thingGiven == "clothes":
            thingNum2 = random.randint(1,5)
        elif thingGiven == "wagon tongue" or "wagon axle":
            thingNum2 = "1"
        else:
            print("Invalid trade...")

        # Printing what they want and what player gets
        print("A traveler wants",thingWanted,"(",str(thingNum),")","and will give",thingGiven,"(",str(thingNum2),")","for it.")

        # Determining if you have enough
        if ("Wagon Wheel" not in parts):
            input("You do not have enough wagon wheel(s) to do this trade... \n Press enter to continue...")
        else: # IF you have enough this happens
            choice = input("Will you do this trade?")
            if ("y" in choice) or ("Y" in choice):
                thingNum2 = int(thingNum2)
                parts.remove("Wagon Wheel")
                
                if thingGiven == "ammunition":
                    ammo += thingNum2
                elif thingGiven == "food":
                    food += thingNum2
                elif thingGiven == "clothes":
                    clothes += thingNum2
                elif thingGiven == "oxen":
                    oxen += thingNum2
                elif thingGiven == "wagon tongue":
                    parts.append("Wagon Tongue")
                elif thingGiven == "wagon axle":
                    parts.append("Wagon Axle")
                else:
                    print("Invalid trade...")
                    
                input("Trade made! Press any key.  ")
            else:
                input("Back to the menu then! Press any key.  ")
                    
    elif thingWanted == "wagon tongue":
        thingNum = random.randint(1,3)
        # Removing "wagon tongue" from the options... !! This will reset next time they trade !!
        options.remove("wagon tongue")
        # Choosing the thing given
        thingGiven = random.choice(options)

        # Choosing the amount of the thing given
        if thingGiven == "ammunition":
            thingNum2 = random.randint(10,40)
        elif thingGiven == "food":
            thingNum2 = random.randint(5,200)
        elif thingGiven == "clothes":
            thingNum2 = random.randint(1,5)
        elif thingGiven == "wagon wheel" or "wagon axle":
            thingNum2 = "1"
        else:
            print("Invalid trade...")

        # Printing what they want and what player gets
        print("A traveler wants",thingWanted,"(",str(thingNum),")","and will give",thingGiven,"(",str(thingNum2),")","for it.")

        # Determining if you have enough
        if ("Wagon Tongue" not in parts):
            input("You do not have enough wagon wheel(s) to do this trade... \n Press enter to continue...")
        else: # IF you have enough this happens
            choice = input("Will you do this trade?")
            if ("y" in choice) or ("Y" in choice):
                thingNum2 = int(thingNum2)
                parts.remove("Wagon Tongue")
                
                if thingGiven == "ammunition":
                    ammo += thingNum2
                elif thingGiven == "food":
                    food += thingNum2
                elif thingGiven == "clothes":
                    clothes += thingNum2
                elif thingGiven == "oxen":
                    oxen += thingNum2
                elif thingGiven == "wagon wheel":
                    parts.append("Wagon Wheel")
                elif thingGiven == "wagon axle":
                    parts.append("Wagon Axle")
                else:
                    print("Invalid trade...")
                    
                input("Trade made! Press any key.  ")
            else:
                input("Back to the menu then! Press any key.  ")
                
    elif thingWanted == "wagon axle":
        thingNum = random.randint(1,3)
        # Removing "wagon axle" from the options... !! This will reset next time they trade !!
        options.remove("wagon axle")
        # Choosing the thing given
        thingGiven = random.choice(options)

        # Choosing the amount of the thing given
        if thingGiven == "ammunition":
            thingNum2 = random.randint(10,40)
        elif thingGiven == "food":
            thingNum2 = random.randint(5,200)
        elif thingGiven == "clothes":
            thingNum2 = random.randint(1,5)
        elif thingGiven == "wagon wheel" or "wagon tongue":
            thingNum2 = "1"
        else:
            print("Invalid trade...")

        # Printing what they want and what player gets
        print("A traveler wants",thingWanted,"(",str(thingNum),")","and will give",thingGiven,"(",str(thingNum2),")","for it.")

        # Determining if you have enough
        if ("Wagon Axle" not in parts):
            input("You do not have enough wagon wheel(s) to do this trade... \n Press enter to continue...")
        else: # IF you have enough this happens
            choice = input("Will you do this trade?")
            if ("y" in choice) or ("Y" in choice):
                thingNum2 = int(thingNum2)
                parts.remove("Wagon Axle")
                
                if thingGiven == "ammunition":
                    ammo += thingNum2
                elif thingGiven == "food":
                    food += thingNum2
                elif thingGiven == "clothes":
                    clothes += thingNum2
                elif thingGiven == "oxen":
                    oxen += thingNum2
                elif thingGiven == "wagon wheel":
                    parts.append("Wagon Wheel")
                elif thingGiven == "wagon tongue":
                    parts.append("Wagon Tongue")
                else:
                    print("Invalid trade...")
                    
                input("Trade made! Press any key.  ")
            else:
                input("Back to the menu then! Press any key.  ")
        
    else:
        print("Invalid trade...")

def wagonFix(partBroke,parts):
    """ A function to fix your wagon. To use: wagonFix(partBroke,parts) """
    import random

    # Setting the wagon to broke
    wagon = "Broke"

    # Fixing the wagon is a 50/50 chance...
    while partBroke in parts:
        wagonChoice = input("Do you wish to repair your wagon?  ")
        if ("y" in wagonChoice) or ("Y" in wagonChoice):
            outcome = random.randint(1,2)
            parts.remove(partBroke)
            if outcome == 1:
                wagon = "Fixed"
                print("The fix was a success!!")
                break
            else:
                print("You failed to fix the wagon...")
        else:
            print("Try trading! You can't continue like this!")

def turn(food,ammo,clothes,oxen,parts,currentPace,weather,hp,health,familyMembers,currentRations,milesTravel,totalMiles,currentDate,money,wagon):
    """ Starts the turn system... defines the weather, health, problems that can happen, etc...
To use: turn(food,ammo,clothes,oxen,parts,currentPace,weather,hp,health,familyMembers,currentRations,milesTravel,totalMiles,currentDate,money,wagon) """

    import datetime
    import random
    
    # Selecting the weather
    weather = random.choice(["Hot","Cold","Rain","Snow"])

    # Setting HP and Rations Mod
    if hp >= 80:
        health = "Good"
    elif hp < 80 and hp >= 50:
        health = "Fair"
    else:
        health = "Poor"

    if currentRations == "Filling":
        rationsMod = 2
    elif currentRations == "Meager":
        rationsMod = 1
    else:
        rationsMod = .5

    # Problems
    problem = random.choice(["A member of your party got lost",
                             "A member of your party got a snake bite.",
                             "A member of your party got sick",
                             "An ox has died.",
                             "Your wagon axle broke.",
                             "Your wagon wheel broke.",
                             "Your wagon tongue broke.",
                             "No problems","No problems","No problems","No problems","No problems","No problems",
                             "No problems","No problems","No problems","No problems","No problems","No problems",
                             "No problems","No problems","No problems","No problems","No problems","No problems",
                             "No problems","No problems","No problems","No problems","No problems","No problems"])

    # Creating the ASCII Art for the main game
    while True:
        print(str.format("""
   .....                                        ..'..                              ..',,,'..        
..',;;;,,'...  ...                       ..'''',,;;;;,..                       ..',;;;;;;;;,,,'..   
,;;,;;;;;,;;;,,,;,,...               ..',;;;;;,,;;;;;;;;,'..     ..''....',,'',,;;;;;;;;;;,;;;;;,'..
;;;;;;;;;;;;;;;;;;;;;,,....'..   ..',;;;;;;;;;;;;;;;;;;;;;;,'..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,',,;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
''''''''''''''',,,''''.........'''''',,,''''''''''''',,;;;;;,,,,,,,,,,,,;;;;;;;;;;;;,,,''...'',,,;;;
                                                      ........        ...............            ...
 +-----------------------------+                                                                    
 |Date:{:_>24}|                 
 |Weather:{:_>21}|           ..'''''''''''..                         ..''''''.        
 |Health:{:_>22}|          ,:ccccllllllllc::::,...  ......  ..,::::::clclllcc,.      
 |Miles Travled:{:_>15}|         .cc'.;cccclccccccccclc'.;cllllc;.'ccccccccccccclcl;.      
 |Miles To Go:{:_>17}|          .;c, .,:clcclclcclcclc'.clcccclc.'cccccccccccclll:.       
 |Food:{:_>24}|           .cc.  .';cccclcclcclc'.clcccclc.'cccccccccccccc:.        
 |Rations:{:_>21}|           ,:;.   'ccccccclcclc'.clcccclc.'cccccccccccccc'         
 +-----------------------------+           .;c;.   ,ccclccccllc'.clcccllc.'cccccclccllcc,          
          .,,. .'::.  ....                   .:c.   .clcccccclcc'.cccccclc.'cccccccccccc'           
           .,:::cl,..',';c;:;;;;:;;;'.        ',.   .:cccccccccc..:cccccc:.'ccccccccccc:.           
         .';clcccl,';;::ccccccccccccc:.       ....  ......,,,,'.  .............',,,,..','.          
          ...';:;,,;cccllcclcclccccccc........'.''.',...',.,;',,. .,','',,,  .,'';,','.''.          
                .;:clcclcccclllccccc:,.      ...',... .,'. ', .';. ..,',,.. .;. .,. .,,.            
                 .'clcccc::;'.,:lclc.         ..''    ';...;;...;'   ''''   ,;..';,..';.            
                  .cc,:c;..  .,cc,:c.                 .,'. ', .',.          .;. .,. .,,.            
                .':c,..;l'   .';:;:c.                  .',',;','.            .,,';,',.              
'..''.''''.'''.',:c:,'';:,''''',::::,'''''...'''''''''''',;;;;,''''''''''..'''';;;;;,'''.''''''''''.
;;;;;;;;;;;;;;,;;:::;;;::;,,+------------------------------------------------+;;,;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;,;::::;;;:;;;;|Problem:{: ^40}|;;;;;;;;;;;;;;;;;;;;;,
;;;;;;;;;;;;;;;;;:::;;;::;;;+------------------------------------------------+;;;;,;;;;;;;;;;;;;;;;;
""",currentDate.strftime("%A %b, %d, %Y"),weather,health,milesTravel,totalMiles,food,currentRations,problem))

        # Determining what happens with each problem
        if problem == "A member of your party got lost":
            lost = random.randint(1,7)
            famLost = random.choice(familyMembers)
            print(str.format("{} got lost for {} days...",famLost,lost))
            currentDate += datetime.timedelta(days=lost)
            food -= (len(familyMembers))*rationsMod*lost
        elif problem == "A member of your party got a snake bite.":
            hp -= 50
        elif problem == "A member of your party got sick":
            hp -= 20
        elif problem == "An ox has died.":
            oxen -= 1
            food += 50
            
        elif problem == "Your wagon axle broke.":
            wagonFix("Wagon Axle",parts)
                        
        elif problem == "Your wagon wheel broke.":
            wagonFix("Wagon Wheel",parts)
                        
        elif problem == "Your wagon tongue broke.":
            wagonFix("Wagon Tongue",parts)
            

        # Printing menu choices
        options = ["Continue On",
               "Check Supplies",
               "Change Pace",
               "Change Rations",
               "Stop and Rest",
               "Attempt to trade",
               "Hunt for food",
               "Shop",
               "Fix Wagon"]
        
        choice = menuChoices(options) # I have the get good number built into my menu

        if choice == 1: # Determining what to do if the choice is number one -- This is the "Continue On" option
            if (oxen > 0) and (wagon == "Fixed"):
                # Calling in the travel function to add to miles traveled, but only if number of oxen is greater than zero
                milesTravel = travel(health,currentPace,weather)
                if food > 0:
                    food -= (len(familyMembers)+1)*rationsMod
                else:
                    # Subtracting health from the party if you're out of rations
                    hp -= 10*len(familyMembers)
                currentDate += datetime.timedelta(days=1)
                totalMiles -= milesTravel
                break
            else:
                input("You can't continue today, try trading. \n Press any key to continue.  ") # Forcing them to trade!
                food -= (len(familyMembers)+1)*rationsMod
                currentDate += datetime.timedelta(days = 1)
                
        elif choice == 2: # Determining what to do if the choice is number two -- This is the "Check supplies" option
           checkSupplies(money,oxen,food,ammo,clothes,parts) # Calling the checkSupplies function; built above
           
        elif choice == 3: # Determining what to do if the choice is number three -- This is the "Change Pace" option
            pace = changePace(currentPace) # Calling the changePace function to do all the work
            break

        elif choice == 4: # Determining what to do if the choice is number four -- This is the "Change Rations" option
            currentRations = changeRations(currentRations) # Once again calling a previously built function to do all the work
            break
        
        elif choice == 5: # Determining what to do if the choice is number five -- This is the "Stop and rest" option
            hp, daysRested = rest(currentRations,hp) # Calling a function
            # Determining the amount of food/health lost
            if food > 0:
                food -= ((len(familyMembers)+1)*rationsMod)*daysRested
            else:
                hp -= 10*len(familyMembers)
            currentDate += datetime.timedelta(days=daysRested)
            break
        
        elif choice == 6: # Determining what to do if the choice is number six -- This is the "Attempt to trade" option
            trade(food,ammo,clothes,oxen,parts)
            currentDate += datetime.timedelta(days = 1)
            break
        
        elif choice == 7: # Determining what to do if the choice is number seven -- This is the "Hunt for food" option
            if ammo >= 1:
                print("You're hunting for food.")
                num = random.randint(1,2) # Picking a number for the success of the hunt
                if num == 1:
                    print("The hunt was successful")
                    lbs = random.randint(20,100)
                    print("You collected",str(lbs),"pounds of food.")
                    currentDate += datetime.timedelta(days = 1)
                    food -= (len(familyMembers)+1)*rationsMod
                    break
                else:
                    print("The hunt was not a success. You loose a day.")
                    currentDate += datetime.timedelta(days = 1)
                    food -= (len(familyMembers)+1)*rationsMod
            else:
                print("You do not have enough ammo to hunt")
            input("Press a key  ")
            
        elif choice == 8: # Determining what to do if the choice is number eight -- This is the "Shop" option
            if money > 0:
                shop(money,food,ammo,clothes,oxen,parts)
            else:
                print("You don't have any money! Try trading if you're stuck.")
            input("Press any key to continue....   ")
            
        elif choice == 9:# Determining what to do if the choice is number nine -- This is the "Fix Wagon" option
            if (wagon == "Broke"):
                if problem == "Your wagon axle broke.":
                    wagonFix("Wagon Axle",parts)
                                
                elif problem == "Your wagon wheel broke.":
                    wagonFix("Wagon Wheel",parts)
                                
                elif problem == "Your wagon tongue broke.":
                    wagonFix("Wagon Tongue",parts)
            else:
                print("You have a working wagon! ")
            input("Press a key to continue...")
            
        else:
            print("Please enter a number...")

    if hp <= 0: # Determining if a famiy memeber has died
        die = random.choice(familyMembers) # Choosing who died
        print("A member of your family,",die,"has died")

        # Getting if the player wants to go cannibal
        famFood = input("Would you like to eat your family member?  ")
        
        if ("y" in famFood) or ("Y" in famFood):
            familyMembers.remove(die)
            food += 100
            print("\nCongratulations! You're all cannibals, but at least you got 100lbs of food.")
        else:
            familyMembers.remove(die)
            print(die+"'s body was instead eaten by the wolves...")
            
        hp = 100
        input("\n Press enter to continue:  ")

    if food < 0:
        food = 0

    return food,ammo,clothes,oxen,parts,currentPace,weather,hp,health,familyMembers,currentRations,milesTravel,totalMiles,currentDate,money,wagon
        
def play():
    """ Starts the game. To use: play() """
    
    # Importing things needed
    import datetime
    import random
    
    # Starting the play stuff
    #############################################

    START_DATE = datetime.datetime(1848,3,1)
    currentDate = START_DATE

    # Variables
    money = 0
    prof = ""
    listOfProfs = []
    familyMembers = []
    wagonLeader = ""
    ammo = 0
    food = 0
    clothes = 0
    oxen = 5
    parts = []
    bill = 0
    totalMiles = 2000
    milesTravel = 0
    currentRations = "Filling"
    hp = 100
    weather = "Cold"
    wagon = "Fixed"

    # Calling functions and updating variables
    health = "Good"
    weather = "Cold"
    currentPace = "Normal"

    prof,money = charCreate()
    familyMembers,wagonLeader = familySetup()
    print("\n Before leaving for independence you should buy equipment and supplies.")
    print(str.format("\n You have {} in cash to make this trip.",money))
    print("Remember you can buy supplies along the way, so you don't have to spend it all now.")
    input("\n\n Press any key to continue")
    money,food,ammo,clothes,oxen,parts = shop(money,food,ammo,clothes,oxen,parts)
    
    #############################################

    # Setting win conditions
    while (totalMiles > 0) and (len(familyMembers) > 0):
        food,ammo,clothes,oxen,parts,currentPace,weather,hp,health,familyMembers,currentRations,milesTravel,totalMiles,currentDate,money,wagon = turn(food,ammo,clothes,oxen,parts,currentPace,weather,hp,health,familyMembers,currentRations,milesTravel,totalMiles,currentDate,money,wagon)
    if totalMiles <= 0:
        print("Congrats you made it!")
    else:
        print("You lost... You and your family have all died.")


mainMenu()
