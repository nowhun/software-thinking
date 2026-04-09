a = int(input())
b = []
for i in range(a):
    c = int(input())
    if c != 0:
        b.append(c)
        c = 0
    elif c == 0:
        b.pop()
        c = 0
print(sum(b))   