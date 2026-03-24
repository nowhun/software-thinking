a = int(input())
i = 0
if a%5 == 0:
    print(a//5)
else:
    while a > 0:
        a -= 3
        i += 1
        if a%5 == 0:
            i+=(a//5)
            print(i)
            break
        elif (a==1) or (a==2):
            print(-1)
            break

