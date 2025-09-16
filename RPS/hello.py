import random


def rps():
  UserInputA = input("Rock?")
  UserInputB = input("Paper?")
  UserInputC = input("Scissor?")
  
  if UserInputA != "y":
   input(UserInputB)
  if UserInputA == "y" and compOutput == "Scissor":
   print("You win :) ")
  if UserInputA == "y" and compOutput == "Paper":
   print("You lost :( ")
  if UserInputA == "y" and compOutput == "Rock":
   print("It's a tie!")
  if UserInputB != "y":
   input(UserInputC)
  if UserInputB == "y" and compOutput =="Scissor":
    print("You lost :( ")
  if UserInputB == "y" and compOutput == "Rock":
    print("You win :) ")
  if UserInputB == "y" and compOutput == "Paper":
    print("It's a tie!")
  if UserInputC != "y":
   print("An error has occurred. Please try again.")
  if UserInputC == "y" and compOutput == "Scissor":
    print("It's a tie!")
  if UserInputC == "y" and compOutput == "Rock":
   print("You lost :( ")
  if UserInputC == "y" and compOutput == "Paper":
   print("You win :) ")

PlayAgain = input("Play again? y/n")
if (PlayAgain == "y"):
 rps() 

rpsList=["Rock","Paper","Scissor"]
compOutput=random.choice(rpsList)
print("Rock, Paper, Scissor, Shoot!")
rps()