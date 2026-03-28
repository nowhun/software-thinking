a = int(input())

for i in range(a, 1, -1):
    for k in range(a-i):
        print(" ",end='')
    for j in range(i*2-1):
        print("*", end='')
    print() 
for i in range(1, a+1 ,+1):
    for k in range(a-i):
        print(" ",end='')
    for j in range(i*2-1):
        print("*", end='')
    print() 