n=int(input())
sky=input().split()
ground=input().split()
for i in range(n):
    sky[i]=int(sky[i])
    ground[i]=int(ground[i])
door=0
score=0
current=0
for i in range(n):
    if ground[i]==1:
        current=i
    if ground[i]==4:
        door=i
target=0


while True:
    print("Score:",score)
    for i in range(n):
        print(sky[i],end="")
    print()
    for i in range(n):
        print(ground[i],end="")
    print()
    move=int(input("Enter move:"))
    if move == 1:
        target = current - 1
    if move==2:
        target = current+1
    if move == 3:
        target = current-2
        if sky[current-1]==2:
            score+=100
            sky[current-1]=0
    if move == 4:
        target = current+2
        if sky[current+1]==2:
            score+=100
            sky[current+1]=0
    if ground[target]==2:
        score+=100
    ground[current]=0
    ground[target]=1
    current=target
    print()
    if not (1 <= move <= 4):
        print("Invalid move!")
    elif target >= n or target < 0:
        print("Invalid move!")
    if door==current:
        for i in range(n):
            print(sky[i],end="")
        print()
        for i in range(n):
            print(ground[i],end="")
        print()
        break
print("Congratulations! You have successfully completed this game!")
print("Your score is:",score)