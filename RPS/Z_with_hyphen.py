def a():
    print("z", end=" ")
def hyphen():
    print("-", end=" ")
for h in range(9):
    a()
for i in range(2,9):
    print()
    for j in range (i-1,i):
        for k in range(i-1):
            hyphen()
        a()
        for l in range(9-i):
            hyphen()
print()
for h in range(9):
    a()


print()
print()


for h in range(9):
    a()
for i in range(2,9):
    print()
    for j in range (i-1,i):
        for l in range(9-i):
            hyphen()
        a()
        for k in range(i-1):
            hyphen()
print()
for h in range(9):
    a()