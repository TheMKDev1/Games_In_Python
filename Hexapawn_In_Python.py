from os import system
from colorit import *

global board
global boardOutlineColor

p1PossibleMoves = [74, 41, 85, 52, 96, 63]
p1PossibleCaptures = [75, 42, 84, 86, 51, 53, 95, 62]

p2PossibleMoves = [14, 47, 25, 58, 36, 69]
p2PossibleCaptures = [15, 48, 24, 26, 57, 59, 35, 68]

p1PawnColor = Colors.blue
p2PawnColor = Colors.red
emptyColor = Colors.white
pawnColors = [emptyColor, p1PawnColor, p2PawnColor]
boardOutlineColor = Colors.yellow

board = [pawnColors[2], pawnColors[2], pawnColors[2], pawnColors[0], pawnColors[0], pawnColors[0], pawnColors[1], pawnColors[1], pawnColors[1]]

def DisplayBoard():
    system('cls')
    print("\n")

    print(color("  " + " ◼  ", board[0]) + color("|", boardOutlineColor) + color("  ◼  ", board[1]) + color("|", boardOutlineColor) + color("  ◼ ", board[2]))
    print(color(" ―――――――――――――――――", boardOutlineColor))

    print(color("  " + " ◼  ", board[3]) + color("|", boardOutlineColor) + color("  ◼  ", board[4]) + color("|", boardOutlineColor) + color("  ◼ ", board[5]))

    print(color(" ―――――――――――――――――", boardOutlineColor))
    print(color("  " + " ◼  ", board[6]) + color("|", boardOutlineColor) + color("  ◼  ", board[7]) + color("|", boardOutlineColor) + color("  ◼ ", board[8]))

    print("\n")

    print(color("  " + "  1  ", pawnColors[0]) + color("|", boardOutlineColor) + color("  2  ", pawnColors[0]) + color("|", boardOutlineColor) + color("  3  ", pawnColors[0]))
    print(color(" ――――――――――――――――――", boardOutlineColor))

    print(color("  " + "  4  ", pawnColors[0]) + color("|", boardOutlineColor) + color("  5  ", pawnColors[0]) + color("|", boardOutlineColor) + color("  6  ", pawnColors[0]))

    print(color(" ――――――――――――――――――", boardOutlineColor))
    print(color("  " + "  7  ", pawnColors[0]) + color("|", boardOutlineColor) + color("  8  ", pawnColors[0]) + color("|", boardOutlineColor) + color("  9  ", pawnColors[0]))
    print("\n")

def Player1Turn():
    while True:
        p1Input = input(color("\nBlue's turn: ", p1PawnColor))

        try:
            p1Input = int(p1Input)

        except:
            DisplayBoard()

            input(color("\nYour answer ", Colors.purple) + color(str(p1Input), p1PawnColor) + color(" is not valid, press enter to continue", Colors.purple))
            del(p1Input)            

        else:
            p1Input = int(p1Input)

            twoDigitList = [int(x) for x in str(p1Input)]

            if p1Input in p1PossibleMoves:
                if board[twoDigitList[0] - 1] == pawnColors[1]:
                    if board[twoDigitList[1] -1] == pawnColors[0]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[1]

                        del(p1Input) 
                        del(twoDigitList)
                        break

            elif p1Input in p1PossibleCaptures:
                if board[twoDigitList[0] - 1] == pawnColors[1]:
                    if board[twoDigitList[1] - 1] == pawnColors[2]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[1]

                        del(p1Input) 
                        del(twoDigitList)
                        break
            
            DisplayBoard()

            input(color("\nYour answer ", Colors.purple) + color(str(p1Input), p1PawnColor) + color(" is not valid, press enter to continue", Colors.purple))
            del(p1Input) 
            del(twoDigitList)    

            DisplayBoard()            

def Player2Turn():
    while True:
        p2Input = input(color("\nRed's turn: ", p2PawnColor))

        try:
            p2Input = int(p2Input)

        except:
            DisplayBoard()

            input(color("\nYour answer ", Colors.purple) + color(str(p2Input), p2PawnColor) + color(" is not valid, press enter to continue", Colors.purple))
            del(p2Input)            

        else:
            p2Input = int(p2Input)

            twoDigitList = [int(x) for x in str(p2Input)]

            if p2Input in p2PossibleMoves:
                if board[twoDigitList[0] - 1] == pawnColors[2]:
                    if board[twoDigitList[1] -1] == pawnColors[0]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[2]

                        del(p2Input) 
                        del(twoDigitList)
                        break

            elif p2Input in p2PossibleCaptures:
                if board[twoDigitList[0] - 1] == pawnColors[2]:
                    if board[twoDigitList[1] - 1] == pawnColors[1]:
                        board[twoDigitList[0] - 1] = pawnColors[0]
                        board[twoDigitList[1] - 1] = pawnColors[2]

                        del(p2Input) 
                        del(twoDigitList)
                        break
            
            DisplayBoard()

            input(color("\nYour answer ", Colors.purple) + color(str(p2Input), p2PawnColor) + color(" is not valid, press enter to continue", Colors.purple))
            del(p2Input) 
            del(twoDigitList)    

            DisplayBoard()        

def CheckIfMoveIsPossible(move, player):
    splitMove = [int(x) for x in str(move)]

    if player == 1:
        if move in p1PossibleMoves:
            if board[splitMove[0] - 1] == pawnColors[1]:
                if board[splitMove[1] -1] == pawnColors[0]:
                    return True
        elif move in p1PossibleCaptures:
            if board[splitMove[0] - 1] == pawnColors[1]:
                if board[splitMove[1] -1] == pawnColors[2]:
                    return True
            
    elif player == 2:
        if move in p2PossibleMoves:
            if board[splitMove[0] - 1] == pawnColors[2]:
                if board[splitMove[1] -1] == pawnColors[0]: 
                    return True  
        elif move in p2PossibleCaptures:
            if board[splitMove[0] - 1] == pawnColors[2]:
                if board[splitMove[1] -1] == pawnColors[1]: 
                    return True  
                
    return False

def CheckForP1Win():
    stuckCounter = 0

    if (board[0] == pawnColors[1]) or (board[1] == pawnColors[1]) or (board[2] == pawnColors[1]):
        return True
    else:
        for i in range(len(p2PossibleMoves)):
            if CheckIfMoveIsPossible(p2PossibleMoves[i], 2) == False:
                stuckCounter += 1  
            
        for i in range(len(p2PossibleCaptures)):
            if CheckIfMoveIsPossible(p2PossibleCaptures[i], 2) == False:
                stuckCounter += 1

    if stuckCounter == 14:
        return True           
    
    return False
         
def CheckForP2Win():    
    stuckCounter = 0

    if (board[6] == pawnColors[2]) or (board[7] == pawnColors[2]) or (board[8] == pawnColors[2]):
        return True
    else:
        for i in range(len(p1PossibleMoves)):
            if CheckIfMoveIsPossible(p1PossibleMoves[i], 1) == False:
                stuckCounter += 1
                
            
        for i in range(len(p1PossibleCaptures)):
            if CheckIfMoveIsPossible(p2PossibleCaptures[i], 1) == False:
                stuckCounter += 1

    if stuckCounter == 14:
        return True           
    
    return False

def StartGameLoop():
    global p1Win
    global p2Win

    p1Win = False
    p2Win = False

    while True:
        DisplayBoard()

        Player1Turn()
        if CheckForP1Win() == True:
            p1Win = True
            GameEnd()
            break
            
        DisplayBoard()

        Player2Turn()
        if CheckForP2Win() == True:
            p2Win = True
            GameEnd()
            break

def GameEnd():
    global board
    global boardOutlineColor
    global p1Win
    global p2Win

    if p1Win == True:
        boardOutlineColor = Colors.blue
    elif p2Win == True:
        boardOutlineColor = Colors.red

    DisplayBoard()
    if p1Win == True:
        print(color("Blue Wins!", p1PawnColor))
    elif p2Win == True:
        print(color("Red Wins!", p2PawnColor))

    if input(color("\nif you want to play again type 1: ", Colors.purple)) == "1":
        board = [pawnColors[2], pawnColors[2], pawnColors[2], pawnColors[0], pawnColors[0], pawnColors[0], pawnColors[1], pawnColors[1], pawnColors[1]]
        
        del(p1Win)
        del(p2Win)
        boardOutlineColor = Colors.yellow
        StartGameLoop()

StartGameLoop()
#Banana_Power