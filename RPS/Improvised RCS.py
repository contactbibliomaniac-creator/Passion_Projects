import random

def rps():# Scissor beats Paper, Paper beats Rock, Rock beats Scissor.

    choices=["ROCK", "PAPER", "SCISSOR"]
    win = {"SCISSOR" : "PAPER" , "PAPER" : "ROCK" , "ROCK" : "SCISSOR"}

    userInput = input("Rock, Paper, or Scissor?")
    filteredInput = userInput.upper()
    compInput = random.choice(choices)
    print(filteredInput)
    print(compInput)

    if filteredInput in choices:
        inornot = True
    else:
        inornot = False


    if filteredInput not in choices:
        print("Your input is invalid. Please try again")
        rps()

    if filteredInput == compInput:
        print("Computer and you both chose", filteredInput ,".")
    elif compInput == win[filteredInput]:
        print("You won!:) ")
    else:
        print("Computer won :( ")
    userPlayAgain = input("Play again? y/n")
    if userPlayAgain == "y":
        rps()
rps()
