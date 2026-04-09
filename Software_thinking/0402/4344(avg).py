c = int(input())
for i in range (c):
    s = []
    sum = 0
    a = 0
    avg = 0
    s.extend(map(int,input().split()))
    for j in range(1, s[0]+1):
        sum += s[j]
    avg = sum/s[0]
    for k in range(1, s[0]+1):
        if s[k] > avg:
            a += 1
    r = round(a/s[0]*100, 3)
    print(f"{r:.3f}%")
