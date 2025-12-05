n=input()
n=list(n)
for i in range(len(n)):
    n[i]=int(n[i])

numsToPlace=input().split()
for i in range(len(numsToPlace)):
    numsToPlace[i]=int(numsToPlace[i])
row1=[]
row2=[]
row3=[]
row4=[]
discard=[]
row1.append(n[0])
row2.append(n[1])
row3.append(n[2])
row4.append(n[3])
for j in range(len(numsToPlace)):
    ones=(((numsToPlace[j])%100)-((numsToPlace[j])%10))//10
    tens=ones
    ones=numsToPlace[j]%10
    if row1[len(row1)-1]%10==tens:
        row1.append(numsToPlace[j])
    elif row1[len(row1)-1]%10==ones:
        row1.append(10*ones+tens)
    elif row2[len(row2)-1]%10==tens:
        row2.append(numsToPlace[j])
    elif row2[len(row2)-1]%10==ones:
        row2.append(10*ones+tens)
    elif row3[len(row3)-1]%10==tens:
        row3.append(numsToPlace[j])
    elif row3[len(row3)-1]%10==ones:
        row3.append(10*ones+tens)
    elif row4[len(row4)-1]%10==ones:
        row4.append(10*ones+tens)
    elif row4[len(row4)-1]%10==tens:
        row4.append(numsToPlace[j])
    else:
        discard.append(numsToPlace[j])
something=0
for k in range(len(discard)):
    something=(((discard[k])%100)-((discard[k])%10))//10+discard[k]%10+something
print(something)