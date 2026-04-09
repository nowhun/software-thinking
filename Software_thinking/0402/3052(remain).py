a = []
c = []

for i in range(10):
    b = int(input())
    a.append(b%42)

for j in range(0, 42):
    c.append(a.count(j))

print(42 - c.count(0))