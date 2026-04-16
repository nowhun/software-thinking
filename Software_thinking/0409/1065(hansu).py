def hansu(a):
    count = 0
    for i in range(1 , a+1):
        if i < 100:
            count += 1
        if i > 99:
            dig = [int(d) for d in str(i)]
            gap = dig[1] - dig[0]
            d = True
            for j in range(len(dig)-1):
                if (dig[j+1] - dig[j]) != gap:
                    d = False
                    break
            if d:
                count += 1
    return(count)
n = int(input())
print(hansu(n))