print("Enter the number of boxes:")
numOfBoxes=int(input())
print("Enter pennies in each box:")
print()
board=input().split()
currentPlayer=1
p1=0
p2=0
p1Moves=[]
p2Moves=[]
def playerMove3():
    global p1
    global p2
    global currentPlayer
    #print("p1")
    #print(p1)
    if len(p1Moves)==0 and len(p2Moves)==0:
        print("Invalid move!")
        currentPlayer=3-currentPlayer
    elif currentPlayer==1:
        strUndoAction=p2Moves[len(p2Moves)-1]
        #print("strUndoAction")
        #print(strUndoAction)
        x,y=strUndoAction.split()
        x=int(x)
        y=int(y)
        p2=p2-y
        if x==1:
            board.insert(0, y)
        if x==2:
            board.insert(len(board), y)
        p2Moves.pop()
        #print("after edits board")
        #print(board)
    elif currentPlayer==2:
        strUndoAction=p1Moves[len(p1Moves)-1]
        #print("strUndoAction")
        #print(strUndoAction)
        x,y=strUndoAction.split()
        x=int(x)
        y=int(y)
        p1=p1-y
        if x==1:
            board.insert(0, y)
        if x==2:
            board.insert(len(board), y)
        p1Moves.pop()
        #print("after edits board")
        #print(board)
def updatePlayerMove():
	if currentPlayer==1:
		if playerMove==1:
			p1Moves.append(f"{playerMove} {board[0]}")
		if playerMove==2:
			p1Moves.append(f"{playerMove} {board[(len(board)-1)]}")
	if currentPlayer==2:
		if playerMove==1:
			p2Moves.append(f"{playerMove} {board[0]}")
		if playerMove==2:
			p2Moves.append(f"{playerMove} {board[(len(board)-1)]}")
for j in range(len(board)):
    board[j]=int(board[j])
while True:
    print("Boxes:")
    for i in range(len(board)):
        print(board[i],end=" ")
    print()
    print(f"Player 1 score: {p1}")
    print(f"Player 2 score: {p2}")
    print(f"Enter player {currentPlayer} move (1 for leftmost,2 for rightmost,3 for undo):")
    playerMove=int(input())
    if playerMove==1:
        if currentPlayer==1:
            p1=p1+board[0]
        if currentPlayer==2:
            p2=p2+board[0]
        updatePlayerMove()
        board.pop(0)
    elif playerMove==2:
        if currentPlayer==1:
            p1=p1+board[len(board)-1]
        if currentPlayer==2:
            p2=p2+board[len(board)-1]
        updatePlayerMove()
        board.pop()
    elif playerMove==3:
        playerMove3()
        #print("after undo p1moves")
        #print(p1Moves)
        #print("after undo p2moves")
        #print(p2Moves)
    elif playerMove!=1 and playerMove!=2 and playerMove!=3:
        print("Invalid move!")
        currentPlayer=3-currentPlayer
    if len(board)==0:
        print("Player 1 score:" ,p1)
        print("Player 2 score:" ,p2)
        break
    else:
        if playerMove!=1 and playerMove!=2 and playerMove!=3 or len(p1Moves)==0 and len(p2Moves)==0:
            currentPlayer=3-currentPlayer
            print()
        else:
            currentPlayer=3-currentPlayer
            print()
        #print("into player move")
        #print(p1Moves)
        #print(p2Moves)
        #print(board)

if p1>p2:
    print("Player 1 won!")
    #print(p1Moves)
    #print(p2Moves)
elif p2>p1:
    print("Player 2 won!")
    #print(p1Moves)
    #print(p2Moves)
else:
    print("It's a tie!")
    #print(p1Moves)
    #print(p2Moves)
