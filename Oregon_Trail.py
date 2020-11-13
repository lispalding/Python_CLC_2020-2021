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
    # Creating a choice menu base that we can call to
    index = 1
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

    mainDisplay()

    options = ["Play Game","Learn About Oregon Trail","Quit"]   # Defining what will go into the menu 
    menuChoices(options) # Calling to menuChoices

def learn():
    page =  ("Take a journey by covered wagon across 2000 miles of plains, rivers, and mountains. \
On the plains you will slosh your oxen through mud and water filled ruts or will you plod through dust six inches deep", \
             "How will you cross the rivers, how will you spend yoru money? How will you use supplies? \
It's all up to you to make the choice..."\
             , "You will face many challenges from theives to disease, and many other challenges.\
If you fail, try and try again til you succeed.")
    for i in page:
        print(i)
        input("Press enter to go on...")
    
def charCreate():
    options = ["Banker", "Carpenter", "Farmer", "Display Differences"] # Listing the menu options
    userChoice = menuChoices(options)

    while True:
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
            print('''\t\tA banker is rich and has $1600.
            A Carpenter is middle class and has $800.
            A Farmer is poor and has $400.''')
        else:
            print("Sorry, that is not an option.")

def getName():
    while True:
        name = input("What are the names of your family members (Including yourself)?  ") # Getting family memeber names
        if name == name.isnumeric: # Making sure that the name is numeric
             print("Not valid!!")
        elif len(name) > 1:
            return name
            break 
        else:
            print("Not valid!!")

def familySetup(): # Setting up the family
    familyMembers = []
    wagonLeader = getName()
    familyMem = getNumber(high=7,low=5)
    print("You need at 5-7 family memebers... How many do you have?")
    for i in range(familyMem):
        name = getName()
        familyMembers.append(name)
    return familyMembers, wagonLeader
    

def getNumber(high,low): # Defining the high and low values with high=7 and low=5
    while True:
        number = input()
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

def shop(money):
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
    print("\n\n Press any key to continue")

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
        
        choice = getNumber(len(items),1)

        if choice == 1:
            # Resetting the money spent on this if the menu is acessed twice
            bill -= moneySpent[0]
            ox = 0
            moneySpent[0] = 0.00

            # Printing the menu
            print('''There are two oxek in a yoke; I reccomend at least three yokes. I charge 40$ a yoke.''')
            print(str.format("Total bill so far:     ${:.2f}", bill))
            print("\nHow many yokes do you want?")

            # Updating variables
            answer = getNumber(high=5,low=1)
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
            print("How many pounds of food do you want?")

            # Updating variables
            answer = getNumber(high=1450,low=1)
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
            print("How many sets of clothes do you want?")

            #Updating variables
            answer = getNumber(high=20,low=0)
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
            print("How many boxes do you want?")

            # Updating variables
            answer = getNumber(high=30,low=0)
            cost = answer*2
            bill += cost
            ammo = answer
            moneySpent[3] = cost
            
        elif choice == 5:
            pass
        elif choice == 6:
            # Printing the store checkout
            print(str.format("You have spent:     ${:.2f}", bill))
            correct = input("Is this correct?")

            # Making sure that the user approves of their purchases
            if ("y" in correct) or ("Y" in correct):
                if (money == moneySpent) or (money > moneySpent[0]):
                    money = money-moneySpent[0,1,2,3,4]
                    
                    break
                else:
                    print("This isn't valid... You've spent more money than you have!")
            else:
                print("Back to the store then!")
            
        else:
            pass

def play():
    money = 0
    prof = ""
    listOfProfs = []
    familyMembers = []
    wagonLeader = ""
    prof,money = charCreate()
    familyMembers,wagonLeader = familySetup()
    shop(money)

money = 100
shop(money)
