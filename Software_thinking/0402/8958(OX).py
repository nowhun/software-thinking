c = int(input())
for i in range(c):
    a = input()
    s = 0
    b = 0
    for j in a:
        if j == 'O':
            b += 1
            s += b
        else:
            b = 0
    print(s)