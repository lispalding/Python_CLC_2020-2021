# PROGRAM NAME: Oregon_Trail.py
# PROGRAM PURPOSE: To play Oregon Trail
# MADE BY: Lisette Spalding, Danson Coats, Hanna Kraemer
# DATE LAST MODIFIED: 11-03-2020
# PYTHON VER. USED: 3.8

def logoScreen():
    # !! MAKE PRETTIER !!
    title = '''
   ___                     __ _                            _____                     _       _    
  / _ \     _ _    ___    / _` |   ___    _ _       o O O |_   _|    _ _   __ _     (_)     | |   
 | (_) |   | '_|  / -_)   \__, |  / _ \  | ' \     o        | |     | '_| / _` |    | |     | |   
  \___/   _|_|_   \___|   |___/   \___/  |_||_|   TS__[O]  _|_|_   _|_|_  \__,_|   _|_|_   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| {======|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'./o--000'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' '''
    
    logo = """
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc.oXMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx. .lXMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXc,;lllKMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc::xXlc0WMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk:c:xMXlcKMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0:o0coWM0:oNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo:KNllNMMk:kMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXcoWNllNMMXclNMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO:kMNllNMWXc'kWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWocKMNl:kdooo,cXMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXclWMNc 'd0NWd:0MMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:kMMNc lWMMMk:OMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNlcXMMNl,0MMMM0:dWMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:oWMMWx:OMMMMXclNMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:kMMMMK:dMMMMWd:0MMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMKcoWMMMM0;lNMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMNlcXMMMKo.,0MMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMWocXMM0clo;xWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMWocXMK:lNNocXMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMWdcKKclXMMx:OMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMMk:lcoXMMMKcoNMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMMO;,oXMMMMWocXMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMMO:xNMMMMMWocKMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMMO:kMMMMMMMO:kMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMMO:kMMMMMMMXcoWMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMM0:xWMMMMMMNclWMMMMMMMM
MMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:OMMMMMXcoWMMMMWNO;lNMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx:0MMMMMNclWMMNkdoo;:KMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXclNMMMMMNclWNkclONM0:oNMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx:OMMMMMMNc:xlckNMMMWx:kWMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXclNMMMMMMNc,okNMMMMMMNlcXMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd:OMMMMMMMNclWMMMMMMMMMx:OMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMK:oWMMMMMMMNxkWMMMMMMMMMXllXMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNl'ldddddddddddddxkkkkkkkkc.lXMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx;cxk0KXXXXXXXX0OxxxxxxxxxxdclONMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO;oNMMMMMMMMMMMMMMMMMMMMMMMMMNOll0W
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkocxXMMMMMMMMMMMMMMMMMMWNX0OOOkxxl'lX
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkdoldONMMMMMMWNXKKKKKK0OkxdddddxxxxxkO0XW
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNx;,:ldO0K0Oxdoodddoddddd;,lxkOXWWMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxoddddddddxk:;OXNWMMMMWlcXMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMk:kMMMMMMMWlcNMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWNXXk;oXXNMMMNO;'ldddoxXMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKxodddddddddlodclKM0cldk0KK0c:KMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWOcoOXNWWNWWMMMMMO;dWx:0MMMMMMx;OMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNlcXMMMMMMMMMMMMMNo;OO;dWWWX0kc.lWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNllNMMMMMMMMMMMMMMXclKc'codoodd;lNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWN0OOOOOOOOOOkxockWMMMMMMMMMWWMMMMx:kO;,kNWMMNllNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0OkxddddoodxxdxxddxxdxOXWMMMMNKOxdoldXMMMO:xWx:0MMMMNllNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMNKkdddddddxk0XNNWWMMMMMMMMMMMMMMMMNkooodxk0o:0MMMXcoWx:0MMMMNllNMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMNOdoodk0KNWMMMMMMMMMMMMMMMMMMMMMMMMMKl:kNWMMMMx:KMMMXcoWx:0WMWWXo;OMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMW0dllkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKclKMMMMMMMx:0MMMNl:Kx',cdddd:,kMMMMMMMMMM
MMMMMMMMMMMMMMMMMMNkolxKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0clXMMMMMMMMx:k0kxd:;OXl'dXXNWx:0MMMMMMMMMM
MMMMMMMMMMMMMMMWXxllONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWX0dcdXMMMMMMMMMOclc;lkOKWMk:OMMMMx:OMMMMMMMMMM
MMMMMMMMMMMWXOdold0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOdoox0WMMMMMMMMMMWWWXllXMMMMx:OMMMM0:dWMMMMMMMMM
MMMMMMWX0kdooox0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNWMMMMMMMMMMMMMMMMMM0:dWMMWocXMMMMNlcXMMMMMMMMM
NXKOxdooddOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWo:0MMWocKMMMMWocXMMMMMMMMM
OddddOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO:xMMMk:xXXXKO:cXMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNXk,oWMM0:':ldddd0WMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNKOxxxxxxxxxxddddddo'cNMMWo;0WWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXkdooddkkOOOOOOOOO0KXNMWlcXMMMx:0MMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXkolloxKNMMMMMMMMMMMMMMMMMMWlcXMMWK:cXMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xolok0XMMMMMMMMMMMMMMMMMMMMMMWo;ddoodlxNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkooodOXWMMMMMMMMMMMMMMMMMMMMMMMMMMXkkk0XNWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxlldONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOxood0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kxoooxKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWWNXKOxxxxkkxxddddoxk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MNOxxxxxddddoddddxkkxxkkkOKXNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MN0kkkkkO0KKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM"""
    companyName = '''Brand'''
    trademark = "TM"

    print("\t\t\t",title)
    print(logo)
    print("\t\t\t",companyName,trademark)

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

def  shop(money,food,ammo,clothes,oxen):
    """ Runs the shop. To use: shop(money,food,ammo,clothes,oxen) """
    
    # Defining the things needed in the stores
    ammo = 0
    food = 0
    clothes = 0
    oxen = 0
    parts = []
    bill = 0
    items = ["Oxen","Food","Clothes","Ammunition","Wagon Parts","Check Out"]
    moneySpent = [0.00,0.00,0.00,0.00,0.00,bill]

    print("\n Before leaving for independence you should buy equipment and supplies.")
    print(str.format("\n You have {} in cash to make this trip.",money))
    print("Remember you can buy supplies along the way, so you don't have to spend it all now.")
    input("\n\n Press any key to continue")

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
            ox = 0
            moneySpent[0] = 0.00

            # Printing the menu
            print('''There are two oxek in a yoke; I reccomend at least three yokes. I charge 40$ a yoke.''')
            print(str.format("Total bill so far:     ${:.2f}", bill))

            # Updating variables
            answer = getNumber(high=5,low=1,question="\nHow many yokes do you want?")
            cost = answer*40
            bill += cost
            ox = answer*2
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
            answer = getNumber(high=1450,low=1,question="\nHow many pounds of food do you want?")
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
            answer = getNumber(high=20,low=0,question="\nHow many sets of clothes do you want?")
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
            answer = getNumber(high=30,low=0,question="\nHow many boxes do you want?")
            cost = answer*2
            bill += cost
            ammo = answer
            moneySpent[3] = cost
            
        elif choice == 5:
            # Setting Inventory to nothing
            parts = []

            # Printing the welcome screen
            print("It is a good idea to have a few spare parts for your wagon on hand... A broken wagon can be a death sentence.")

            # Setting variables
            partsBill = 0.00
            inventory = ["Wagon Wheel","Wagon Axle","Wagon Tongue","Back to main shop"]
            partsCost = [10.00,20.00,50.00,partsBill]

            while True:
                partsCost[len(partsCost)-1] = partsBill
                print("Here is the list of things you can buy...")
                
                for i in range(len(parts)):
                    print(str.format("{}.     {:20}     ${:.2f}",parts[i],partsCost[i]))
                    print(str.format("Total bill so far:     ${:.2f}",bill))
                    print(str.format("Total funds available: ${:.2f}",money))
                    item = int(input("What item would you like to buy"))


                    if item == 1:
                        answer = answer = getNumber(high=6,low=0,question="\nHow many wagon wheels do you want?")
                        for i in range(answer):
                            parts.append("Wagon Wheel")
                        partsBill += partsCost[0]*answer
                    elif item == 2:
                        answer = getNumber(high=6,low=0,question="\nHow many wagon wheels do you want?")
                        for i in range(answer):
                            parts.append("Wagon Axle")
                        partsBill += partsCost[1]*answer
                    elif item == 3:
                        answer = getNumber(high=6,low=0,question="\nHow many wagon wheels do you want?")
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
            correct = input("Is this correct?")

            # Making sure that the user approves of their purchases
            if ("y" in correct) or ("Y" in correct):
                if (money == moneySpent) or (money > moneySpent[0]):
                    money = money-moneySpent[0,1,2,3,4]
                    
                    return ox, food, clothes, inventory
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
    
    # Printing Rations Menu
    menuChoices(rations)

    # Printing the current rations
    print(currentRations)

    # Creating a loop so if invalid input is entered, the menu keeps on appearing
    while True:
        for i in range(len(rations)):
            userChoice = getNumber(high=3,low=1,question="What rations would you like?  ")

            # Creating if statements to return what the user desires
            if userChoice == 1:
                currentRations = "Filling"
                return currentRations
            elif userChoice == 2:
                currentRations = "Meager"
                return currentRations
            elif userchoice == 3:
                currentRations = "Bare Bones"
                return currentRations
            else:
                print("You can't do that!\n")

def changePace(currentPace):
    """ Determines the current pace. To use: changePace(currentPace) """
    
    # Variables
    pace = ["Slow","Normal","Fast"]
    currentPace = ""

    menuChoices(pace)
    print(currentPace)
    
    for i in range(len(pace)):
        choice = getNumber(1,3,"What pace would you like?  ")

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


def rest(currentRations,currentHealth):
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

    if (healthGain+currentHealth > 100):
        currentHealth = 100
    else:
        currentHealth += healthGain
        round(currentHealth)

    print("Your health is at:",currentHealth)

def checkSupplies(money,oxen,food,ammo,clothes,parts):
    supplies = [money,oxen,food,ammo,clothes,parts]
    menuChoices(supplies)
    

def travel(health,pace,weather):
    """ Determines miles traveled. To use: travel(health,pace,weather) """
    
    # Setting up variables
    mph = 0
    hours = 0
    milesTravel = 0

    while True:
        # Setting up the pace effects
        if (pace == "Slow"):
            mph = 1
        elif (pace == "Normal"):
            mph = 2
        elif (pace == "Fast"):
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

def turn(oxen,food,pace,weather,health,familyMembers,rations,milesTravel,totalMiles,hp,currentDate):
    """ Starts the turn system... defines the weather, health, problems that can happen, etc...
To use: turn(oxen,food,pace,weather,health,familyMembers,rations,milesTravel,totalMiles,hp,currentDate) """

    # Selecting the weather
    weather = random.choice(["Hot","Cold","Rain","Snow"])

    # Setting HP and Rations Mod
    if health >= 80:
        health = "Good"
    elif health < 80 and hp >= 50:
        health = "Fair"
    else:
        health = "Poor"

    if rations == "Filling":
        rationsMod = 2
    elif rations == "Meager":
        rationsMod = 1
    else:
        rationsMod = .5

    # Problems
    problem = random.choice(["A member of your party got lost",
                             "A member of your party got a snake bite.",
                             "A member of your party got sick",
                             "An ox has died.",
                             "No problems","No problems","No problems","No problems","No problems","No problems",
                             "No problems","No problems","No problems","No problems","No problems","No problems",
                             "No problems","No problems","No problems","No problems","No problems","No problems",
                             "No problems","No problems","No problems","No problems","No problems","No problems"])
    if problem == "A member of your party got lost":
        lost = random.randint(1,7)
        famLost = random.choice(familyMembers)
        print(str.format("{} got lost for {} days...",famLost,lost))
        currentDate += datetime.timedelta(days=lost)
        food -= (len(familyMembers))*rationsMod*lost
    elif problem == "A member of your party got a snake bite.":
        health -= 50
    elif problem == "A member of your party got sick":
        hp -= 20
    elif problem == "An ox has died.":
        ox -= 1
        food += 50

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

    while True:
        options = ["Continue On",
               "Check Supplies",
               "Change Pace",
               "Change Rations",
               "Stop and Rest",
               "Attempt to trade",
               "Hunt for food"]
        
        menuChoices(options)
        
        getNumber(1,6,"\n \tWhat would you like to do?  ")

        if choice == 1:
            if oxen > 0:
                milesTravel = travel(pace,weather,currentHealth)
                if food > 0:
                    food -= (len(familyMembers)+1)*rationsMod
                else:
                    hp -= 10*len(familyMembers)
                currentDate += datetime.datedelta(days=1)
                totalMiles -= milesTravel
                break
            else:
                print("You don't have enough Oxen to continue today, try trading.")
                food -= (len(familyMembers)+1)*rationsMod
                currentDate += datetime.timedelta(days = 1)
        elif choice == 2:
           checkSupplies(money,oxen,food,ammo,clothes,parts)
        elif choice == 3:
            pace = changePace(currentPace)
            break
        elif choice == 4:             
            currentRations = changeRations(currentRations)
            break
        elif choice == 5:
            hp, daysRested = rest(currentRations,currentHealth)
            if food > 0:
                food -= ((len(familyMembers)+1)*rationsMod)*daysRested
            else:
                hp -= 10*len(familyMembers)
            currentDate += datetime.datedelta(days=daysRested)
            break
        elif choice == 6:
            print("You're attempting to trade...")
            currentDate += datetime.timedelta(days = 1)
            food -= (len(familyMembers)+1)*rationsMod
            break
        elif choice == 7:
            print("You're hunting for food.")
            num = random.randint(1,2)
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

    if hp <= 0:
        print("A member of your family has died")
        die = random.choice(familyMembers)
        familyMembers.remove(die)
        hp = 100
        input("Press enter to continue:  ")

    if food < 0:
        food = 0

    return oxen,food,pace,weather,health,familyMembers,rations,milesTravel,totalMiles,hp,currentDate
        
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
    oxen = 0
    parts = []
    bill = 0
    hp = 100
    totalMiles = 2000
    milesTravel = 0

    # Calling functions and updating variables
    health = "Good"
    weather = "Cold"
    pace = "Normal"

    prof,money = charCreate()
    familyMembers,wagonLeader = familySetup()
    shop(money,food,ammo,clothes,oxen)
    turn(oxen,food,pace,weather,health,familyMembers,rations,milesTravel,totalMiles,health,currentDate)
    
    #############################################

    # Setting win conditions
    while (totalMiles > 0) and (len(familyMembers) > 0):
        turn(oxen,food,pace,weather,health,familyMembers,rations,milesTravel,totalMiles,hp,currentDate)
    if toalMiles <= 0:
        print("Congrats you made it!")
    else:
        print("You lost... You and your family have all died.")


mainMenu()
