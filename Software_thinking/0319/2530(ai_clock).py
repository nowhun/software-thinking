h, m, s = map(int, input().split())
t = int(input())

s += t

while s>=60:
    m += 1
    s -= 60

while m>=60:
    h += 1
    m -= 60

while h>23:
    h -= 24

print(h, m, s)