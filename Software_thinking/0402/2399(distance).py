c = 0
a = int(input())
b = list(map(int, input().split()))
b.sort(reverse=True)
for i in range(a):
    for j in range(i, a):
        c += b[i] - b[j]

print(c*2)
