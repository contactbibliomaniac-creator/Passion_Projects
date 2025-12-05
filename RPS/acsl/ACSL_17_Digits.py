n,p,d=input().split()
p,d=int(p),int(d)
p=len(n)-p
n=input()
n=list(n)
for i in range(len(n)):
    n[i]=int(n[i])
digit=n[p]
if digit==0 or digit==1 or digit==2 or digit==3 or digit==4:
    digit=(digit+d)%10
else:
    digit=abs(digit-d)
    number=1
    while digit//number!=0:
        number=number*10
    number=number//10
    digit=digit// number
n[p]=digit
for i in range(1,len(n)-p):
    n[p+i]=0
for i in range(len(n)):
    print(n[i],end="")