n, m = 0, 0

for j in range(4):
    o, i = map(int, input().split())
    n -= o
    n += i
    if n > m:
        m = n

print(m)