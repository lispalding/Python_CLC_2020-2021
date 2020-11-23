# PROGRAM NAME: 11_12_2020__Tic_Tac_Toe.py
# PROGRAM PURPOSE: To play a game of Tic Tac Toe
# MADE BY: Lisette Spalding
# DATE LAST MODIFIED: 11-18-2020
# PYTHON VER. USED: 3.8

# Global Constants
X = " X "
O = " O "
EMPTY = "   "
TIE = "Tie"
NUM_SQUARES = 9

# Function Definitions
def displayInstructions():
    """Display game instructions. To use ( displayInstructions() )"""
    print('''
Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
This will be a showdown between your human brain and my silicon processor.

You will make your move known my entering a number, 0-8. The number will correspond to the board position as illustrated:

               \t\t 0 | 1 | 2
               \t\t ---------
               \t\t 3 | 4 | 5
               \t\t ---------
               \t\t 6 | 7 | 8
               
Prepare yourself, human. The ultimate battle is about to begin. \n''')

def nextTurn(currentTurn):
    """ This function switches the turns in the game. To use: ( turn = nextTurn(currentTurn) ) """
    if currentTurn == X:
        return O
    else:
        return X

def pieces(): 
    """ Determine if the player or computer goes first. To use: ( computer,human = pieces() ) """

    # Asking if the user wantsthe first move
    goFirst = askYesNo("Do you require the first move? (y/n):  ")

    # Defining the varibles on if the user/computer gets X or O
    if (goFirst == "y") or (goFirst == "yes"):
        human = X
        computer = O
        print("\nThen take the first move. You will need it.\n")
    else:
        computer = X
        human = O
        print("\nYour bravery will be your undoing... I will go first.\n")
    return computer, human

def askYesNo(question): 
    """Ask a yes or no question and get back a yes or no answer. To use: ( answer = askYesNo(question) ) """
    response = None
    while response not in ("y","n","yes","no"):
        response = input(question).lower()
    return response

def newBoard():
    """ Create a new game board full of empty spaces. To use: ( board = newBoard() ) """
    board = []

    for square in range(NUM_SQUARES):
        board.append(EMPTY)    
    return board

def displayBoard(board):
    """ Display game board on screen. To use ( displayBoard(board) ) """
    print(str.format("\t\t{}|{}|{}",board[0],board[1],board[2]))
    print("\t\t-----------")
    print(str.format("\t\t{}|{}|{}",board[3],board[4],board[5]))
    print("\t\t-----------")
    print(str.format("\t\t{}|{}|{}",board[6],board[7],board[8]))

def humanMove():
    move = None
    while move == None:
        move = askNumber("What place on the board do you desire? (0-8):  ",0,8)
    return move

def askNumber(question,low,high):
    """ Ask for a number within a range. To use: ( answer = askNumber(question, low, high) ) """
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

# Main Game
def main():
    # Pulling in functions and defining variables
    displayInstructions()
    turn = X
    computer,human = pieces()
    board = newBoard()
    while True:
        displayBoard(board)
        move = humanMove()
        board[move] = turn
        turn = nextTurn(turn)
main()
