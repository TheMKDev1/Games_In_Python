from colorit import *
from os import system
import random

global acceptableLetters
acceptableLetters = (' a b c d e f g h i j k l m n o p q r s t u v w x y z ').split()

global guess
guess = ""

global word
word = ""

global wordLength
wordLength = 0

global splitWord
splitWord = ""

global guessedLetters
guessedLetters = []

global misses
misses = 0

global hangmanColor
hangmanColor = Colors.orange

global backgroundColor
backgroundColor = Colors.yellow

global guessedLettersColor
guessedLettersColor = Colors.purple


def Display():


    print("\n")

    print(color("________", backgroundColor))
    print(color("||     |", backgroundColor))
    print(color("||     ", backgroundColor), end = ""); print(color("O", hangmanColor)) if misses >= 1 else print("")
    print(color("||    ", backgroundColor), end = "")
    
    if misses >= 2:
        print(color("/", hangmanColor), end = "")

    if misses >=3:
        print(color("|", hangmanColor), end = "")

    if misses >= 4:
        print(color("\ ", hangmanColor), end = "")

    print("")

    print(color("||     ", backgroundColor), end = ""); print(color("|", hangmanColor)) if misses >= 5 else print("")
    print(color("||    ", backgroundColor), end = "")

    if misses >= 6:
        print(color("/", hangmanColor), end = "")
    
    if misses >= 7:
        print(color(" \ ", hangmanColor), end = "")
    
    print("")

    print(color("||__",backgroundColor))

    print("\n")


def GuessInput():
    global guess
    global splitWord
    global guessedLetters
    global acceptableLetters
    global misses

    for i in range(len(word)):

        if guess == splitWord[i] and guess != guessedLetters[i]:

            guessedLetters.pop(i)
            guessedLetters.insert(i, guess)

        print(color(" " + guessedLetters[i] + " ", guessedLettersColor), end= "")
     
    
    print("") #fix for weird bug that shows the guessed letters at the end of the game


    if misses >= 7 or guessedLetters == splitWord:
        pass
    else:

        print("\n")
        guess = input(color("Guess a letter:  ", Colors.blue))

        if guess.isalpha() == True and len(guess) == 1 and guess in acceptableLetters and guess in splitWord:
            pass

        elif guess.isalpha() == True and len(guess) == 1 and guess in acceptableLetters and guess not in splitWord:
            misses += 1

        else:
            system('cls')

            print('\n')

            Display()

            print(color("Your Answer ", Colors.purple) + color(str(guess), Colors.yellow) + color(" Is Not Valid", Colors.purple))

            GuessInput()

def GameLoop():

    global guessedLetters
    global splitWord

    system('cls')
    
    if guessedLetters == splitWord or misses >= 7:
        pass
    else:

        Display()

        GuessInput()

        GameLoop() 
        


def AskForWords():
    global word
    global splitWord

    word = " ".join(input(color("\nWrite your word here: \n\n", Colors.purple)).lower().split())

    splitWord = [*word]

    for i in range(len(word)):

        if splitWord[i] == " ":
            guessedLetters.append(" ")

        else:
            guessedLetters.append(" __ ")

#game start
def Start():

    global guess
    global word
    global wordLength
    global splitWord
    global guessedLetters
    global misses
    global hangmanColor
    global backgroundColor
    global guessedLettersColor


    system('cls')
    AskForWords()

    GameLoop()

    Display()

    if misses >= 7:
        print(color(f'\nThe word was "{word}"', Colors.red))
    else:
        print(color(f'\nYou correctly guessed "{word}"', Colors.green))

    input(color("\n\nPress enter to continue", Colors.purple))


    while True:

        system('cls')

        ask = input(color("\n\nDo You Want To Play Again? ", Colors.blue)).lower()

        if ask == "yes":

            guess = ""
            word = ""
            wordLength = 0
            splitWord = ""
            guessedLetters = []
            misses = 0
            hangmanColor = Colors.orange
            backgroundColor = Colors.yellow
            guessedLettersColor = Colors.purple

            Start()
        elif ask == "no":
            break
        else:
            pass

Start()