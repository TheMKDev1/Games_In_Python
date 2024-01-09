import random
#loop
while True:
    # for getting a random bot choice
    def get_bot_choice():
        return random.choice(("rock", "paper", "scissors"))
    bot_choice = get_bot_choice()

    #getting player input
    while True:
        player_choice = input("rock, paper, or scissors?  \n")

        if player_choice.lower() == "rock" or player_choice.lower() == "paper" or player_choice.lower() == "scissors":
            break
        else:
            print("That isn't an answer!")
            pass


    #logic if player choice is rock
    if player_choice == "rock":
        if bot_choice == "scissors":
            print(f"you win, the bot chose {bot_choice}\n")
        elif bot_choice == "paper":
            print(f"you lose, the bot chose {bot_choice}\n")
        else:
            print("its a tie!\n")
    #logic if player choice is paper
    elif player_choice == "paper":
        if bot_choice == "rock":
            print(f"you win, the bot chose {bot_choice}\n")
        elif bot_choice == "scissors":
            print(f"you lose, the bot chose {bot_choice}\n")
        else:
            print("its a tie\n")
    #logic if player choice is scissors
    elif player_choice == "scissors":

        if bot_choice == "paper":
            print(f"you win, the bot chose {bot_choice}\n")
        elif bot_choice == "rock":
            print(f"you lose, the bot chose {bot_choice}\n")
        else:
            print("its a tie\n")
    
    #if the player wants to play again

    want_again= input("do you want to try again?  \n")
    if want_again.lower() == "yes" or want_again.lower == "ye" or want_again.lower == "y":
        pass
    else:
        print("\nbye!")
        break

