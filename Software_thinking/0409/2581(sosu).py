def sosu(a, b):
    sum = 0
    mini = b
    
    for i in range(a, b+1):
        sos = 1
        if i == 1:
            continue
        for j in range(2, i):
            if i%j == 0:
                sos = 0
        if sos == 1:
            sum += i
            if mini >= i:
                mini = i
    if sum == 0:
        print("-1")
    else:
        print(sum)
        print(mini)

c = int(input())
d = int(input())
sosu(c,d)