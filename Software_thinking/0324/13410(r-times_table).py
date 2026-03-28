a, b = map(int, input().split())
x = []
for i in range(b):
    x.append(str((a*(i+1)))[::-1])

x = map(int, x)
print(max(x))