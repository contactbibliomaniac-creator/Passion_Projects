list1=[]
map1={}
def J1():
    b=int(input())
    p=b*5-400
    print(p)
    if b>100:
        print(-1)
    elif b<100:
        print(1)
    elif b==100:
        print(0)
def J2():
    number_people=int(input())
    for i in range(number_people):
        person=str(input())
        money=int(input())
        list1.append(money)
        map1[money] = person
    max_money=max(list1)
    max_money_person = map1[max_money]
    print(max_money_person)
l,c,p=map(int, input().split())
coordinates=[]
for i in range(c):
    z=input()
    coordinates.append(z)
for i in range(len(coordinates)):
    a=coordinates[i]
    x,y=a.split()
    print(abs(p-x)+abs(y))