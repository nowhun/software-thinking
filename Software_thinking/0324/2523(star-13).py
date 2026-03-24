a = int(input())

for i in range (1, a+1, 1):
    for j in range(i):
        print("*", end='')
    print(end='\n')
for i in range (a-1, 0, -1):
    for j in range(i):
        print("*", end='')
    print(end='\n')