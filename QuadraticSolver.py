import math
from os import system

def SolveQuadratic():
    a = float(input("\ntype the value of a: "))

    b = float(input("\nPlease type the value of b: "))

    c = float(input("\nPlease type the value of c: "))

    if ((b*b) - (4*a*c)) < 0:

        term1 = (b * -1)/ (2*a)

        term2 = math.sqrt(((b*b) - (4*a*c)) * -1 ) / (2*a)

        if (term1 % 1) == 0:
            term1 = math.floor(term1)

        if (term2 % 1) == 0:
            term2 = math.floor(term2)

        print("\npositiveOutput: " + str(term1) + " + " + str(term2) + "i")

        print("\nnegativeOutput: " + str(term1) + " - " + str(term2) + "i")
    else:

        positiveOutput = ((b * -1) + math.sqrt( (b*b) - (4*a*c) )) / (2*a)

        negativeOutput = ((b * -1) - math.sqrt( (b*b) - (4*a*c) )) / (2*a)


        if (positiveOutput % 1) == 0:
            positiveOutput = math.floor(positiveOutput)

        if (negativeOutput % 1) == 0:
            negativeOutput = math.floor(negativeOutput)

        print("\npositiveOutput: " + str(positiveOutput))

        print("\nnegativeOutput: " + str(negativeOutput))


    if input("\nDo you want to reset the program? ") == "yes":

        system('cls')
        
        SolveQuadratic()

SolveQuadratic()
