from os import system
from colorit import *


p1ShipColor = Colors.blue
p2ShipColor = (255, 0, 0)
emptyColor = Colors.white
brokenShipColor = Colors.purple
missedMissileColor = Colors.yellow
hitMissileColor = Colors.green
mineColor = (100, 100, 100)
brokenMineColor = (255, 111, 0)


global totalP1MissileCount
global totalP2MissileCount

global totalSmallShipCount
global totalLargeShipCount

global totalMineCount


global currentTurn

mineMissilePenalty = 1
hitShipBoost = 1

acceptablePositions = ("A1 A2 A3 A4 A5 A6 B1 B2 B3 B4 B5 B6 C1 C2 C3 C4 C5 C6 D1 D2 D3 D4 D5 D6 E1 E2 E3 E4 E5 E6 F1 F2 F3 F4 F5 F6").split()


def GetIndexFromPosition(pos):
    for i in range(len(acceptablePositions)):
        if acceptablePositions[i] == pos:
            return i
       
def PrivacyScreen(currentPlayerTurn):
    system('cls')
    
    if currentPlayerTurn == "P1":
        input("It's " + color("Player one's ", Colors.blue) + "turn, press enter to continue ")
    if currentPlayerTurn == "P2":
        input("It's " + color("Player two's ", Colors.red) + "turn, press enter to continue ")

def IsDeadCheck(playerToCheck):

    if playerToCheck == "P1":
        
        livingShipCount = 0

        for i in range(len(p1HomeBoard)):

            if p1HomeBoard[i][1] == p1ShipColor:
                livingShipCount += 1
        
        if livingShipCount > 0:
            del(livingShipCount)
            return False
        else:
            del(livingShipCount)
            return True


    elif playerToCheck == "P2":
        
        livingShipCount = 0

        for i in range(len(p2HomeBoard)):

            if p2HomeBoard[i][1] == p2ShipColor:
                livingShipCount += 1
        
        if livingShipCount > 0:
            del(livingShipCount)
            return False
        else:
            del(livingShipCount)
            return True


def DisplayP1HomeBoard():

    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.green))
    print(color("┃", Colors.green) + color("   ⌂ ", Colors.blue) + color(" | ", Colors.green) + color("  1  ", Colors.orange) + color(" | ", Colors.green) + color("  2  ", Colors.orange) + color(" | ", Colors.green) + color("  3  ", Colors.orange) + color(" | ", Colors.green) + color("  4  ", Colors.orange) + color(" | ", Colors.green) + color("  5  ", Colors.orange) + color(" | ", Colors.green) + color("  6  ", Colors.orange) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  A ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[0][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[1][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[2][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[3][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[4][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[5][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  B ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[6][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[7][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[8][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[9][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[10][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[11][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  C ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[12][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[13][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[14][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[15][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[16][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[17][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  D ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[18][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[19][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[20][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[21][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[22][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[23][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  E ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[24][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[25][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[26][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[27][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[28][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[29][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  F ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[30][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[31][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[32][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[33][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[34][1]) + color(" | ", Colors.green) + color("  ◼  ", p1HomeBoard[35][1]) + color(" ┃", Colors.green))
    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.green))

    print("\n") 

def DisplayP1AttackBoard():

    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.yellow))
    print(color("┃", Colors.yellow) + color("   ⚔ ", Colors.blue) + color(" | ", Colors.yellow) + color("  1  ", Colors.orange) + color(" | ", Colors.yellow) + color("  2  ", Colors.orange) + color(" | ", Colors.yellow) + color("  3  ", Colors.orange) + color(" | ", Colors.yellow) + color("  4  ", Colors.orange) + color(" | ", Colors.yellow) + color("  5  ", Colors.orange) + color(" | ", Colors.yellow) + color("  6  ", Colors.orange) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  A ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[0][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[1][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[2][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[3][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[4][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[5][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  B ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[6][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[7][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[8][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[9][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[10][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[11][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  C ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[12][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[13][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[14][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[15][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[16][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[17][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  D ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[18][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[19][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[20][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[21][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[22][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[23][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  E ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[24][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[25][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[26][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[27][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[28][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[29][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  F ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[30][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[31][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[32][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[33][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[34][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p1AttackBoard[35][1]) + color(" ┃", Colors.yellow))
    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.yellow))


def DisplayP2HomeBoard():

    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.green))
    print(color("┃", Colors.green) + color("   ⌂ ", Colors.red) + color(" | ", Colors.green) + color("  1  ", Colors.orange) + color(" | ", Colors.green) + color("  2  ", Colors.orange) + color(" | ", Colors.green) + color("  3  ", Colors.orange) + color(" | ", Colors.green) + color("  4  ", Colors.orange) + color(" | ", Colors.green) + color("  5  ", Colors.orange) + color(" | ", Colors.green) + color("  6  ", Colors.orange) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  A ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[0][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[1][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[2][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[3][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[4][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[5][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  B ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[6][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[7][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[8][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[9][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[10][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[11][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  C ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[12][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[13][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[14][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[15][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[16][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[17][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  D ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[18][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[19][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[20][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[21][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[22][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[23][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  E ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[24][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[25][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[26][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[27][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[28][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[29][1]) + color(" ┃", Colors.green))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.green))

    print(color("┃ ", Colors.green)+ color("  F ", Colors.orange) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[30][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[31][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[32][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[33][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[34][1]) + color(" | ", Colors.green) + color("  ◼  ", p2HomeBoard[35][1]) + color(" ┃", Colors.green))
    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.green))

    print("\n") 

def DisplayP2AttackBoard():

    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.yellow))
    print(color("┃", Colors.yellow) + color("   ⚔ ", Colors.red) + color(" | ", Colors.yellow) + color("  1  ", Colors.orange) + color(" | ", Colors.yellow) + color("  2  ", Colors.orange) + color(" | ", Colors.yellow) + color("  3  ", Colors.orange) + color(" | ", Colors.yellow) + color("  4  ", Colors.orange) + color(" | ", Colors.yellow) + color("  5  ", Colors.orange) + color(" | ", Colors.yellow) + color("  6  ", Colors.orange) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  A ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[0][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[1][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[2][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[3][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[4][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[5][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  B ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[6][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[7][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[8][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[9][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[10][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[11][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  C ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[12][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[13][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[14][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[15][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[16][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[17][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  D ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[18][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[19][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[20][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[21][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[22][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[23][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  E ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[24][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[25][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[26][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[27][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[28][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[29][1]) + color(" ┃", Colors.yellow))
    print(color("┃⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯┃", Colors.yellow))

    print(color("┃ ", Colors.yellow)+ color("  F ", Colors.orange) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[30][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[31][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[32][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[33][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[34][1]) + color(" | ", Colors.yellow) + color("  ◼  ", p2AttackBoard[35][1]) + color(" ┃", Colors.yellow))
    print(color("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━", Colors.yellow))


def PlaceP1SmallShips():
    for i in range(totalSmallShipCount):
        while True:

            try:

                system('cls')
                DisplayP1HomeBoard()

                inputedLoc = input(color("\nType where you would like the head of your 2 units long small ship to go and which direction the tail should be: ", Colors.blue)).split()

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p1ShipColor
                                            break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [30, 31, 32, 33, 34, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:
                                                                                    
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p1ShipColor
                                            break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 6, 12, 18, 24, 30]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:

                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p1ShipColor
                                            break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [5, 11, 17, 23, 29, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                            p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p1ShipColor
                                            break
                            
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)

                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)
                else: 
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedLoc)

def PlaceP2SmallShips():
    for i in range(totalSmallShipCount):
        while True:

            try:

                system('cls')
                DisplayP2HomeBoard()

                inputedLoc = input(color("\nType where you would like the head of your 2 units long small ship to go and which direction the tail should be: ", Colors.red)).split()

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p2ShipColor
                                            break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [30, 31, 32, 33, 34, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p2ShipColor
                                            break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 6, 12, 18, 24, 30]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p2ShipColor
                                            break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [5, 11, 17, 23, 29, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                            p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p2ShipColor
                                            break
                            
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)

                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)
                else: 
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedLoc)

def PlaceP1LargeShips():

    for i in range(totalLargeShipCount):
        while True:

            try:

                system('cls')
                DisplayP1HomeBoard()

                inputedLoc = input(color("\nType where you would like the head of your 3 units long large ship to go and which direction the tail should be: ", Colors.blue)).split()

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] = p1ShipColor
                                                break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor: 

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p1ShipColor                                            
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] = p1ShipColor
                                                break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 6, 7, 12, 13, 18, 19, 24, 25, 30, 31]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:                         

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:   

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] = p1ShipColor
                                                break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [4, 5, 10, 11, 16, 17, 22, 23, 28, 29, 34, 35]:

                                    if p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            if p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] == emptyColor:

                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p1ShipColor
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p1ShipColor                                            
                                                p1HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] = p1ShipColor
                                                break
                            
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)

                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)
                else: 
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedLoc)

def PlaceP2LargeShips():

    for i in range(totalLargeShipCount):
        while True:

            try:

                system('cls')
                DisplayP2HomeBoard()

                inputedLoc = input(color("\nType where you would like the head of your 3 units long large ship to go and which direction the tail should be: ", Colors.red)).split()

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedLoc)

            else:

                if len(inputedLoc) > 1:

                    if inputedLoc[0] in acceptablePositions:

                        match inputedLoc[1].lower():

                            case "up":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:  

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] == emptyColor:

                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 6][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 12][1] = p2ShipColor
                                                break

                            case "down":

                                if GetIndexFromPosition(inputedLoc[0]) not in [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] == emptyColor:

                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 6][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 12][1] = p2ShipColor
                                                break

                            case "left":

                                if GetIndexFromPosition(inputedLoc[0]) not in [0, 1, 6, 7, 12, 13, 18, 19, 24, 25, 30, 31]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] == emptyColor:
                                            
                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 1][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) - 2][1] = p2ShipColor
                                                break

                            case "right":

                                if GetIndexFromPosition(inputedLoc[0]) not in [4, 5, 10, 11, 16, 17, 22, 23, 28, 29, 34, 35]:

                                    if p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] == emptyColor:                     

                                        if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] == emptyColor:

                                            if p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] == emptyColor:

                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0])][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 1][1] = p2ShipColor
                                                p2HomeBoard[GetIndexFromPosition(inputedLoc[0]) + 2][1] = p2ShipColor
                                                break
                            
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)

                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedLoc)
                else: 
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedLoc)

def PlaceP1Mines():
    for i in range(totalMineCount):

        while True:

            try:
                
                system('cls')
                DisplayP1HomeBoard()

                inputedMineLoc = input(color("\nType where you would like to place your mine: ", Colors.blue)).split()

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedMineLoc)

            else:

                if len(inputedMineLoc) > 0:

                    if inputedMineLoc[0] in acceptablePositions:

                        if p1HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] == emptyColor:

                            p1HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] = mineColor
                            break

                        else:
                            input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                            del(inputedMineLoc)
            
                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedMineLoc)

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedMineLoc)

    system('cls')
    DisplayP1HomeBoard()

    input(color("This is your home board", Colors.blue) + ", press enter to continue ")

def PlaceP2Mines():
    for i in range(totalMineCount):

        while True:

            try:
                
                system('cls')
                DisplayP2HomeBoard()

                inputedMineLoc = input(color("\nType where you would like to place your mine: ", Colors.red)).split()

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedMineLoc)

            else:

                if len(inputedMineLoc) > 0:

                    if inputedMineLoc[0] in acceptablePositions:

                        if p2HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] == emptyColor:
                            
                            p2HomeBoard[GetIndexFromPosition(inputedMineLoc[0])][1] = mineColor
                            break

                        else:
                            input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                            del(inputedMineLoc)
            
                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedMineLoc)

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedMineLoc)

    system('cls')
    DisplayP2HomeBoard()

    input(color("This is your home board", Colors.red) + ", press enter to continue ")


def P1AttackTurn():
    global totalP1MissileCount
    global currentTurn
    global P1Gamble
    global P2Gamble

    PrivacyScreen("P1")

    currentP1MissileCount = totalP1MissileCount

    if currentTurn > 2:

        while True:

            try:
                system('cls')

                DisplayP1AttackBoard()

                p1Belief = input(color(f"\nPlayer 2 says there is a ship at {P2Gamble}, if you think he is bluffing type 1, if you think he isn't type 2: ", Colors.blue))

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(p1Belief)

            else:
                if p1Belief == "1":

                    if p2HomeBoard[GetIndexFromPosition(P2Gamble)][1] == p2ShipColor:

                        input(color(f"\nYou were wrong, there is a ship at {P2Gamble}, so you lose a missile this round", Colors.blue) + ", press enter to continue ")
                        currentP1MissileCount -= 1
                        break

                    else:

                        input(color(f"\nYou were right, there isn't a ship at {P2Gamble}, so you get an extra missile this round", Colors.blue) + ", press enter to continue ")
                        currentP1MissileCount += 1
                        break

                elif p1Belief == "2":

                    if p2HomeBoard[GetIndexFromPosition(P2Gamble)][1] == p2ShipColor:

                        input(color(f"\nYou were right, there is a ship at {P2Gamble}, so you get an extra missile this round", Colors.blue) + ", press enter to continue ")
                        currentP1MissileCount += 1
                        break

                    else:

                        input(color(f"\nYou were wrong, there isn't a ship at {P2Gamble}, so you lose a missile this round", Colors.blue) + ", press enter to continue ")
                        currentP1MissileCount -= 1
                        break         

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(p1Belief)

    for i in range(currentP1MissileCount):  

        while True:
            try:
                
                system('cls')
                DisplayP1AttackBoard()
                DisplayP1HomeBoard()

                if (currentP1MissileCount - i) > 1: 
                    inputedAttackLoc = input(color(f"You have {currentP1MissileCount - i} missiles, where you would like to launch your missile: ", Colors.blue))

                else:
                    inputedAttackLoc = input(color(f"You have {currentP1MissileCount - i} missile left, where you would like to launch your last missile: ", Colors.blue)) 

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedAttackLoc)

            else:
                if len(inputedAttackLoc) > 0:

                    if inputedAttackLoc in acceptablePositions:

                        if p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == p2ShipColor:

                            p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenShipColor
                            p1AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = hitMissileColor

                            system('cls')
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()


                            if IsDeadCheck("P2") == True:

                                input(color("\nYou destroyed all enemy ships!", Colors.blue) + ", press enter to continue ")
                                del(inputedAttackLoc)

                                return True
                            
                            else:
                                totalP1MissileCount += hitShipBoost

                                input(color(f"\nYou hit a ship!, and you now have {totalP1MissileCount} total missiles to use next round", Colors.blue) + ", press enter to continue ")
                                del(inputedAttackLoc)

                                break

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenShipColor:

                            system('cls')
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            input(color("\nYou already hit that ship!", Colors.blue) + ", press enter to continue ")
                            del(inputedAttackLoc)

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenMineColor:

                            system('cls')
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            input(color("\nYou already hit that mine!", Colors.blue) + ", press enter to continue ")
                            del(inputedAttackLoc)

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == missedMissileColor:

                            system('cls')
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            input(color("\nYou already launched a missle here!", Colors.blue) + ", press enter to continue ")
                            del(inputedAttackLoc)

                        elif p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == mineColor:

                            if (totalP1MissileCount - mineMissilePenalty) > 0:
                                totalP1MissileCount -= mineMissilePenalty

                            p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor
                            p1AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor

                            system('cls')
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            input(color(f"\nYou hit a mine!, and you now have {totalP1MissileCount} total missiles to use next round", Colors.blue) + ", press enter to continue ")
                            del(inputedAttackLoc)
                        
                            break

                        else:

                            p2HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor
                            p1AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor

                            system('cls')
                            DisplayP1AttackBoard()
                            DisplayP1HomeBoard()

                            input(color("\nYou Missed!", Colors.blue) + ", press enter to continue ")
                            del(inputedAttackLoc)

                            break

                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedAttackLoc)

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedAttackLoc)
    
    return False

def P2AttackTurn():
    global totalP2MissileCount
    global P1Gamble
    global P2Gamble

    PrivacyScreen("P2")

    currentP2MissileCount = totalP2MissileCount

    if currentTurn > 2:

        while True:

            try:       
                system('cls')

                DisplayP2AttackBoard()

                p2Belief = input(color(f"\nPlayer 1 says there is a ship at {P1Gamble}, if you think he is bluffing type 1, if you think he isn't type 2: ", Colors.red))

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(p2Belief)

            else:
                if p2Belief == "1":

                    if p1HomeBoard[GetIndexFromPosition(P1Gamble)][1] == p1ShipColor:

                        input(color(f"\nYou were wrong, there is a ship at {P1Gamble}, so you lose a missile this round", Colors.red) + ", press enter to continue ")
                        currentP2MissileCount -= 1
                        break

                    else:

                        input(color(f"\nYou were right, there isn't a ship at {P1Gamble}, so you get an extra missile this round", Colors.red) + ", press enter to continue ")
                        currentP2MissileCount += 1
                        break

                elif p2Belief == "2":

                    if p1HomeBoard[GetIndexFromPosition(P1Gamble)][1] == p1ShipColor:

                        input(color(f"\nYou were right, there is a ship at {P1Gamble}, so you get an extra missile this round", Colors.red) + ", press enter to continue ")
                        currentP2MissileCount += 1
                        break

                    else:

                        input(color(f"\nYou were wrong, there isn't a ship at {P1Gamble}, so you lose a missile this round", Colors.red) + ", press enter to continue ")
                        currentP2MissileCount -= 1       
                        break         

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(p2Belief)

    for i in range(currentP2MissileCount):  

        while True:
            try:
                
                system('cls')
                DisplayP2AttackBoard()
                DisplayP2HomeBoard()

                if (currentP2MissileCount - i) > 1: 
                    inputedAttackLoc = input(color(f"You have {currentP2MissileCount - i} missiles, where you would like to launch your missile: ", Colors.red))

                else:
                    inputedAttackLoc = input(color(f"You have {currentP2MissileCount - i} missile left, where you would like to launch your last missile: ", Colors.red))

            except:
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(inputedAttackLoc)

            else:
                if len(inputedAttackLoc) > 0:

                    if inputedAttackLoc in acceptablePositions:

                        if p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == p1ShipColor:

                            p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenShipColor
                            p2AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = hitMissileColor

                            system('cls')
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            if IsDeadCheck("P1") == True:

                                input(color("\nYou destroyed all enemy ships!", Colors.red) + ", press enter to continue ")
                                del(inputedAttackLoc)

                                return True
                            
                            else:
                                totalP2MissileCount += hitShipBoost

                                input(color(f"\nYou hit a ship!, and you now have {totalP2MissileCount} total missiles to use next round", Colors.red) + ", press enter to continue ")
                                del(inputedAttackLoc)

                                break

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenShipColor:

                            system('cls')
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            input(color("\nYou already hit that ship!", Colors.red) + ", press enter to continue ")
                            del(inputedAttackLoc)

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == brokenMineColor:

                            system('cls')
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            input(color("\nYou already hit that mine!", Colors.red) + ", press enter to continue ")
                            del(inputedAttackLoc)

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == missedMissileColor:

                            system('cls')
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            input(color("\nYou already launched a missle here!", Colors.red) + ", press enter to continue ")
                            del(inputedAttackLoc)

                        elif p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] == mineColor:

                            if (totalP2MissileCount - mineMissilePenalty) > 0:
                                totalP2MissileCount -= mineMissilePenalty
                            
                            p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor
                            p2AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = brokenMineColor

                            system('cls')
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            input(color(f"\nYou hit a mine!, and you now have {totalP2MissileCount} total missiles to use next round", Colors.red) + ", press enter to continue ")
                            del(inputedAttackLoc)

                            break

                        else:

                            p1HomeBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor
                            p2AttackBoard[GetIndexFromPosition(inputedAttackLoc)][1] = missedMissileColor

                            system('cls')
                            DisplayP2AttackBoard()
                            DisplayP2HomeBoard()

                            input(color("\nYou Missed!", Colors.red) + ", press enter to continue ")
                            del(inputedAttackLoc)

                            break

                    else:
                        input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                        del(inputedAttackLoc)

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(inputedAttackLoc)
    
    return False


def P1GambleTurn():
    global P1Gamble
    global P2Gamble
    
    while True:

        try:
            system('cls')

            DisplayP1HomeBoard()

            P1Gamble = input(color("\nType the position you want to gamble: ", Colors.blue))

        except:
            input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
            del(P1Gamble)

        else:

            if len(P1Gamble) > 0:

                if P1Gamble in acceptablePositions:
                    break

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(P1Gamble)

            else: 
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(P1Gamble)

def P2GambleTurn():
    global P1Gamble
    global P2Gamble
    
    while True:

        try:
            system('cls')
    
            DisplayP2HomeBoard()

            P2Gamble = input(color("\nType the position you want to gamble: ", Colors.red))

        except:
            input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
            del(P2Gamble)

        else:

            if len(P2Gamble) > 0:

                if P2Gamble in acceptablePositions:
                    break

                else:
                    input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                    del(P2Gamble)

            else: 
                input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")
                del(P2Gamble)               


while True:

    totalSmallShipCount = 2
    totalLargeShipCount = 2

    totalP1MissileCount = 3
    totalP2MissileCount = 3

    totalMineCount = 4


    currentTurn = 0


    p1HomeBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    p1AttackBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    p2HomeBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    p2AttackBoard = [["A1", emptyColor], ["A2", emptyColor], ["A3", emptyColor], ["A4", emptyColor], ["A5", emptyColor], ["A6", emptyColor],
            ["B1", emptyColor], ["B2", emptyColor], ["B3", emptyColor], ["B4", emptyColor], ["B5", emptyColor], ["B6", emptyColor],
            ["C1", emptyColor], ["C2", emptyColor], ["C3", emptyColor], ["C4", emptyColor], ["C5", emptyColor], ["C6", emptyColor],
            ["D1", emptyColor], ["D2", emptyColor], ["D3", emptyColor], ["D4", emptyColor], ["D5", emptyColor], ["D6", emptyColor],
            ["E1", emptyColor], ["E2", emptyColor], ["E3", emptyColor], ["E4", emptyColor], ["E5", emptyColor], ["E6", emptyColor],
            ["F1", emptyColor], ["F2", emptyColor], ["F3", emptyColor], ["F4", emptyColor], ["F5", emptyColor], ["F6", emptyColor],]

    PlaceP1SmallShips()

    PlaceP1LargeShips()

    PlaceP1Mines()

    PlaceP2SmallShips()

    PlaceP2LargeShips()

    PlaceP2Mines()

    while True:

        currentTurn += 1

        if P1AttackTurn() == True:
            
            system('cls')
            DisplayP1AttackBoard()
            DisplayP1HomeBoard()

            input(color("Player One Wins!", Colors.blue) + ", press enter to continue")

            break

        if currentTurn > 2:
            P1GambleTurn()

        if P2AttackTurn() == True:

            system('cls')
            DisplayP2AttackBoard()
            DisplayP2HomeBoard()

            input(color("Player Two Wins!", Colors.red) + ", press enter to continue")

            break
        if currentTurn > 1:
            P2GambleTurn()

    while True:
        try:        
            system('cls')
            askToPlayAgain = input(color("\nDo you want to play again?  ", Colors.purple))

        except:
            
            input(color("\nThat's invalid", Colors.purple) + ", press enter to continue ")

            del(askToPlayAgain)

        else:

            if (askToPlayAgain.lower() == "yes") or (askToPlayAgain.lower() == "no"):
                break

    if askToPlayAgain.lower() == "yes":
        del(askToPlayAgain)

    elif askToPlayAgain.lower() == "no":
        break

    elif askToPlayAgain.lower() == "maybe":
        input(color("Stop it, get some help", Colors.purple))
        del(askToPlayAgain)
        
#banana_power