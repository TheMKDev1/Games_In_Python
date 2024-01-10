from os import system
import time
from colorit import *

def slowPrint(inputtedString, alliteration):
    time.sleep(0.5)

    if alliteration == True:
        for i in range(len(inputtedString)):

            time.sleep(0.025)  
            if inputtedString[i] == "P":
                print(color(inputtedString[i], Colors.green), end= "", flush= True)
            else:
                print(inputtedString[i], end= "", flush= True)
    else:
        for i in range(len(inputtedString)):

            time.sleep(0.025)   
            print(inputtedString[i], end= "", flush= True)

def Start():

    while True:
        system('cls')

        slowPrint("\n\nType 1 for " + color("Alliteration", Colors.green) + ", 2 for " + color("Irony", Colors.red) + ", 3 for " + color("Imagery", Colors.purple) + ", 4 for " + color("Onomatopoeia", Colors.yellow) + ", 5 for " + color("Personification", Colors.orange) + ", and 6 for an " + color("extra", Colors.blue) + "!  ", False)
        desiredLocation = input("")

        if desiredLocation == "1":

            slowPrint(color("\n\nAlliteration\n", Colors.green), False)

            slowPrint("\nWhen the same letter or sound is used at the beginning of words that are next to each other, often used in tongue twisters\n", False)
            slowPrint("\nFor example:\n\n\n", False)

            slowPrint("Peter Piper Picked a Peck of Pickled Peppers\n", True)
            slowPrint("a Peck of Pickled Peppers Peter Piper Picked.\n", True)
            slowPrint("If Peter Piper Picked a Peck of Pickled Peppers,\n", True)
            slowPrint("Where’s the Peck of Pickled Peppers Peter Piper Picked?", True)

            slowPrint(color("\n\nPress enter to continue", Colors.purple), False)
            input("")
            del(desiredLocation)
            
        elif desiredLocation == "2":

            slowPrint(color("\n\nIrony\n", Colors.red), False)

            slowPrint("\nWhen you express something, in way that normally would mean the opposite, often used in comedy\n", False)
            slowPrint("\nFor example:\n\n\n", False)

            slowPrint(color("Mcdonald's", Colors.red) + " once warned about eating too much " + color("Mcdonald's", Colors.red) + "\n", False)
            slowPrint("The Irony here is that Mcdonald's would normally want you to eat more Mcdonalds, not less\n", False)

            slowPrint("\nA few other examples:\n\n\n", False)
            slowPrint("A " + color("Fire Station", Colors.red) + color(" Burned", Colors.red) + " down\n", False)
            slowPrint("A " + color("Marriage Counselor", Colors.red) +" files for "+ color("Divorce\n", Colors.red), False)

            slowPrint("\nAnd my favorite:\n", False)
            slowPrint("A " + color("Therapist", Colors.red) + " becomes " + color("Deppressed", Colors.red), False)

            slowPrint(color("\n\nPress enter to continue", Colors.purple), False)
            input("")
            del(desiredLocation)

        elif desiredLocation == "3":

            slowPrint(color("\n\nImagery\n", Colors.purple), False)

            slowPrint("\nWhen you describe something so vividly and visually that it puts an image in your head, often used in poetry\n", False)
            slowPrint("\nFor example:\n\n\n", False)

            slowPrint("And the " + color("Silken", Colors.purple) +", " + color("Sad", Colors.purple) + ", uncertain " + color("Rustling", Colors.purple) + " of each " + color("Purple Curtain", Colors.purple) + " thrilled me\n", False) 
            slowPrint("filled me with " + color("Fantastic Terrors", Colors.purple) + " never felt before. -The Raven\n", False)

            slowPrint("\nA few other examples:\n\n\n", False)

            slowPrint("The " + color("Big ", Colors.purple) + color("purple ", Colors.purple) + color("Box\n", Colors.purple), False)
            slowPrint("The " + color("Magnificent ", Colors.purple) + color("Fragrant ", Colors.purple) + color("Lavenders\n", Colors.purple), False)
            slowPrint("The " + color("Smooth ", Colors.purple) + color("Leather ", Colors.purple) + color("Jacket\n", Colors.purple), False)
            
            slowPrint(color("\n\nPress enter to continue", Colors.purple), False)
            input("")
            del(desiredLocation)

        elif desiredLocation == "4":

            slowPrint(color("\n\nOnomatopoeia\n", Colors.yellow), False)

            slowPrint("\nWhen you use a word to describe a sound, often used in entertainment\n", False)
            slowPrint("\nA few examples:\n\n\n", False)

            slowPrint("The word " + color("Tinkle", Colors.yellow) + " in the first few lines of Edgar Allan Poe's The Bells\n", False)
            slowPrint("The Words " + color("Wham!, Bam!, Ka-pow!, and Zok! ", Colors.yellow) + "in the hit 1960 Batman TV series, source: youtube.com/watch?v=k9GqATedqPQ\n", False)
            
            slowPrint(color("\n\nPress enter to continue", Colors.purple), False)
            input("")
            del(desiredLocation)

        elif desiredLocation == "5":

            slowPrint(color("\n\nPersonification\n", Colors.orange), False)

            slowPrint("\nWhen you describe something non-human as having human characteristics, often used in stories and fables\n", False)
            slowPrint("\nFor Example:\n\n\n", False)

            slowPrint("The Tortoise is described to " + color("Talk and Think", Colors.orange) + " like a human in The Hare And The Tortoise by aesop\n", False)

            slowPrint("\nA few other examples:\n\n\n", False)

            slowPrint("The " + color("Intelligent ", Colors.orange) + color("Talking ", Colors.orange) + color("Dog\n", Colors.orange), False)
            slowPrint("The " + color("Conscious ", Colors.orange) + color("Feeling ", Colors.orange) + color("Pumpkin\n", Colors.orange), False)
            
            slowPrint(color("\n\nPress enter to continue", Colors.purple), False)
            input("")
            del(desiredLocation)

        elif desiredLocation == "6":

            slowPrint(color("\n\nPuns\n", Colors.blue), False)

            slowPrint("\nA joke that uses the fact that words have multiple meanings or that they sound similar in order to be funny\n", False)
            slowPrint("\nA few examples:\n\n\n", False)

            slowPrint(color("Santa Claus's Helpers", Colors.blue) + " are known as " + color("subordinate Clauses\n", Colors.blue), False)
            slowPrint("My " + color("Math Teacher", Colors.blue) + " called me "+ color("Average", Colors.blue) + ". He's so " + color("Mean", Colors.blue)+ "!\n", False)
            slowPrint(color("Atheism", Colors.blue) + " is a " + color("Non-Prophet Organization\n", Colors.blue), False)
            slowPrint("after breaking every bone in the " + color("left side", Colors.blue) + " of my body, i went to the doctor and he said it's ok you're " + color("all right", Colors.blue) + " now\n", False)
            
            slowPrint(color("\n\nPress enter to continue", Colors.purple), False)
            input("")
            del(desiredLocation)

        else:
            slowPrint(color("\n\nSorry that wasn't an option, press enter to try again", Colors.purple), False)
            input("")
            del(desiredLocation)
            continue

        while True:
            system('cls')

            slowPrint(color("\nIf you want to try something else type 1, if you want to leave type 2  ", Colors.purple), False)
            againInput = input("")

            if againInput == "1":
                del(againInput)
                break

            if againInput == "2":
                quit()

            else:
                slowPrint(color("\n\nSorry that wasn't an option, press enter to try again  ", Colors.purple), False)
                input("")
                del(againInput)

Start()
#banana_power