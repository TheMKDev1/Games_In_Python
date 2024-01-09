from colorit import *
from operator import itemgetter
from os import system

global board
global boardInputColor

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

boardInputColor = [Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow]

#possible win conditions
winList = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

XInput = 0
OInput = 0

global boardColor
boardColor = Colors.orange

def DisplayBoard():

    print("\n")

    print(color("  " + str(board[0]), boardInputColor[0]) + color("|", boardColor) + color(str(board[1]), boardInputColor[1]) + color("|", boardColor) + color(str(board[2]), boardInputColor[2]))
    print(color(" ―――――――", boardColor))

    print(color("  " + str(board[3]), boardInputColor[3]) + color("|", boardColor) + color(str(board[4]), boardInputColor[4]) + color("|", boardColor) + color(str(board[5]), boardInputColor[5]))

    print(color(" ―――――――", boardColor))
    print(color("  " + str(board[6]), boardInputColor[6]) + color("|", boardColor) + color(str(board[7]), boardInputColor[7]) + color("|", boardColor) + color(str(board[8]), boardInputColor[8]))

    print("\n")

def XPlays():

    print("\n")
    XInput = input(color("Where Would You Like To Place Your X:  ", Colors.blue))

    try:
        XInput = int(XInput)

    except:
        system('cls')

        DisplayBoard()

        print(color("Your Answer ", Colors.purple) + color(str(XInput), Colors.blue) + color(" Is Not Valid", Colors.purple))

        del(XInput)
        XPlays()

    else:
        XInput = int(XInput)

        if (XInput < 1) or (XInput > 9) or (board[XInput - 1] == "O") or (board[XInput - 1] == "X"):
            system('cls')

            DisplayBoard()

            print(color("Your Answer ", Colors.purple) + color(str(XInput), Colors.blue) + color(" Is Not Valid", Colors.purple))

            XPlays()

        else:
            board[XInput - 1] = "X"

            boardInputColor[XInput - 1] = Colors.blue

        print("\n")

def OPlays():

    print("\n")
    OInput = input(color("Where Would You Like To Place Your O:  ", Colors.red))

    try:
        OInput = int(OInput)

    except:
        system('cls')

        DisplayBoard()

        print(color("Your Answer ", Colors.purple) + color(str(OInput), Colors.red) + color(" Is Not Valid", Colors.purple))

        del(OInput)
        OPlays()

    else:
        OInput = int(OInput)

        if (OInput < 1) or (OInput > 9) or (board[OInput - 1] == "O") or (board[OInput - 1] == "X"):
            system('cls')

            DisplayBoard()

            print(color("Your Answer ", Colors.purple) + color(str(OInput), Colors.red) + color(" Is Not Valid", Colors.purple))

            OPlays()

        else:
            board[OInput - 1] = "O"

            boardInputColor[OInput - 1] = Colors.red

        print("\n")

def CheckXForWin():
    for i in range(8):
        if itemgetter(*winList[i])(board) == ("X","X","X"):
            return True

def CheckOForWin():
    for i in range(8):
        if itemgetter(*winList[i])(board) == ("O","O","O"):
            return True

def PlayGame():

    for i in range(5):

        system('cls')

        DisplayBoard()

        XPlays()
        if CheckXForWin() == True:
            break

        if i == 4:
            break

        system('cls')

        DisplayBoard()

        OPlays()
        if CheckOForWin() == True:
            break   

def ShowResults():
    global boardColor

    if CheckXForWin() == True:
        boardColor = Colors.blue
        DisplayBoard()
        print(color("X Wins!", Colors.blue))

    elif CheckOForWin() == True:
        boardColor = Colors.red
        DisplayBoard()
        print(color("O Wins!", Colors.red))

    else:
        boardColor = Colors.green
        DisplayBoard()
        print(color("Its a Tie!", Colors.green))

def AskToPlayAgain():
    
    print("\n")
    again = input(color("Do You Want To Play Again?  ", Colors.yellow))

    if again.lower() == "yes":
            global board
            global boardInputColor
            global boardColor

            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            boardInputColor = [Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow, Colors.yellow]
            boardColor = Colors.orange

            GameLoop()

    elif again.lower() == "no":
        pass

    else:
        system('cls')

        print(color("Your Answer ", Colors.purple) + color(str(again), Colors.yellow) + color(" Is Not Valid", Colors.purple))

        AskToPlayAgain()

def GameLoop():

    system('cls')

    PlayGame() 
    
    system('cls')

    ShowResults()

    AskToPlayAgain()

GameLoop()    

#Banana_Power