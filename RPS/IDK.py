import random 
def forfunc():
    for l in range(0,21,7):
        print(tictactoeBoard[l],end="")
        print(tictactoeBoard[l+1],end="")
        print(tictactoeBoard[l+2],end="")
        print(tictactoeBoard[l+3],end="")
        print(tictactoeBoard[l+4],end="")
        print(tictactoeBoard[l+5],end="")
        print(tictactoeBoard[l+6])
coordinatesPossible=["1 1","1 2","1 3","2 1","2 2","2 3","3 1","3 2","3 3"]
def tictactoe():
    print("You are...")
    list=["X.", "O."]
    choice=random.choice(list)
    print(choice)
    print("Computer is...")
    if choice=="X.":
        compchoice="O."
    else:
        compchoice="X."
    print(compchoice)
    global tictactoeBoard
    tictactoeBoard=["|","__","|","__","|","__","|","|","__","|","__","|","__","|","|","__","|","__","|","__","|"]
    for j in range(3):
        for i in range(7):
            print(tictactoeBoard[i],end="")
        print()
    while True:
        if tictactoeBoard[1]==tictactoeBoard[10]==tictactoeBoard[20]==choice or tictactoeBoard[6]==tictactoeBoard[10]==tictactoeBoard[15]==choice or tictactoeBoard[1]==tictactoeBoard[8]==tictactoeBoard[15]==choice or tictactoeBoard[3]==tictactoeBoard[10]==tictactoeBoard[17]==choice or tictactoeBoard[5]==tictactoeBoard[12]==tictactoeBoard[19]==choice or tictactoeBoard[1]==tictactoeBoard[3]==tictactoeBoard[5]==choice or tictactoeBoard[8]==tictactoeBoard[10]==tictactoeBoard[12]==choice or tictactoeBoard[15]==tictactoeBoard[17]==tictactoeBoard[19]==choice:
            print("You win! :)")
            userPlayAgain=input("Do you want to play again? (y/n)")
            if userPlayAgain.lower()==y:
                tictactoe()
            else:
                break
        elif tictactoeBoard[1]==tictactoeBoard[10]==tictactoeBoard[20]==compchoice or tictactoeBoard[6]==tictactoeBoard[10]==tictactoeBoard[15]==compchoice or tictactoeBoard[1]==tictactoeBoard[8]==tictactoeBoard[15]==compchoice or tictactoeBoard[3]==tictactoeBoard[10]==tictactoeBoard[17]==compchoice or tictactoeBoard[5]==tictactoeBoard[12]==tictactoeBoard[19]==compchoice or tictactoeBoard[1]==tictactoeBoard[3]==tictactoeBoard[5]==compchoice or tictactoeBoard[8]==tictactoeBoard[10]==tictactoeBoard[12]==compchoice or tictactoeBoard[15]==tictactoeBoard[17]==tictactoeBoard[19]==compchoice:
            print("You lost. :()")
            userPlayAgain=input("Do you want to play again? (y/n)")
            if userPlayAgain.lower()==y:
                tictactoe()
            else:
                break
        else:
            def func():
                try:
                    global user
                    user=input("Please enter a pair of coordinates in the form 'x y'.")
                    global x
                    global y
                    x,y=user.split()
                    x=int(x)
                    y=int(y)
                except ValueError:
                    print("That is not a perceptible coordinate. Please try again.")
                    func()
                if x>3 or y>3:
                    print("I'm sorry, but that coordinate cannot fit on a tic-tac-toe board. Please try again.")
                    func()
            func()
            if x==1 and y==1:
                tictactoeBoard[15]=choice
                forfunc()
            if x==1 and y==2:
                tictactoeBoard[8]=choice
                forfunc()
            if x==1 and y==3:
                tictactoeBoard[1]=choice
                forfunc()
            if x==2 and y==1:
                tictactoeBoard[17]=choice
                forfunc()
            if x==2 and y==2:
                tictactoeBoard[10]=choice
                forfunc()
            if x==2 and y==3:
                tictactoeBoard[3]=choice
                forfunc()
            if x==3 and y==1:
                tictactoeBoard[19]=choice
                forfunc()
            if x==3 and y==2:
                tictactoeBoard[12]=choice
                forfunc()
            if x==3 and y==3:
                tictactoeBoard[5]=choice
                forfunc()
            print()
        if tictactoeBoard[1]==tictactoeBoard[10]==tictactoeBoard[20]==choice or tictactoeBoard[6]==tictactoeBoard[10]==tictactoeBoard[15]==choice or tictactoeBoard[1]==tictactoeBoard[8]==tictactoeBoard[15]==choice or tictactoeBoard[3]==tictactoeBoard[10]==tictactoeBoard[17]==choice or tictactoeBoard[5]==tictactoeBoard[12]==tictactoeBoard[19]==choice or tictactoeBoard[1]==tictactoeBoard[3]==tictactoeBoard[5]==choice or tictactoeBoard[8]==tictactoeBoard[10]==tictactoeBoard[12]==choice or tictactoeBoard[15]==tictactoeBoard[17]==tictactoeBoard[19]==choice:
            print("You win! :)")
            userPlayAgain=input("Do you want to play again? (y/n)")
            if userPlayAgain.lower()==y:
                tictactoe()
            else:
                break
        elif tictactoeBoard[1]==tictactoeBoard[10]==tictactoeBoard[20]==compchoice or tictactoeBoard[6]==tictactoeBoard[10]==tictactoeBoard[15]==compchoice or tictactoeBoard[1]==tictactoeBoard[8]==tictactoeBoard[15]==compchoice or tictactoeBoard[3]==tictactoeBoard[10]==tictactoeBoard[17]==compchoice or tictactoeBoard[5]==tictactoeBoard[12]==tictactoeBoard[19]==compchoice or tictactoeBoard[1]==tictactoeBoard[3]==tictactoeBoard[5]==compchoice or tictactoeBoard[8]==tictactoeBoard[10]==tictactoeBoard[12]==compchoice or tictactoeBoard[15]==tictactoeBoard[17]==tictactoeBoard[19]==compchoice:
            print("You lost. :(")
            userPlayAgain=input("Do you want to play again? (y/n)")
            if userPlayAgain.lower()==y:
                tictactoe()
            else:
                break
        else:
            print("Computer's turn:")
            coordinatesPossible.pop(coordinatesPossible.index(user))
            computer=random.choice(coordinatesPossible)
            a,b=computer.split()
            a=int(a)
            b=int(b)
            if a==1 and b==1:
                tictactoeBoard[15]=compchoice
                forfunc()
            if a==1 and b==2:
                tictactoeBoard[17]=compchoice
                forfunc()
            if a==1 and b==3:
                tictactoeBoard[19]=compchoice
                forfunc()
            if a==2 and b==1:
                tictactoeBoard[8]=compchoice
                forfunc()
            if a==2 and b==2:
                tictactoeBoard[10]=compchoice
                forfunc()
            if a==2 and b==3:
                tictactoeBoard[12]=compchoice
                forfunc()
            if a==3 and b==1:
                tictactoeBoard[1]=compchoice
                forfunc()
            if a==3 and b==2:
                tictactoeBoard[3]=compchoice
                forfunc()
            if a==3 and b==3:
                tictactoeBoard[5]=compchoice
                forfunc()
tictactoe()
