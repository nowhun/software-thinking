a, x = map(int, input().split())
num = list(map(int, input().split()))

for j in range(a):
    if num[j]<x:
        print(num[j],end='')