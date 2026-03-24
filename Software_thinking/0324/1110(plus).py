a = str(input())
s = 0
if len(a) < 2:
    a = a + '0'
c = a
while 1:
    a1 = int(a[0])
    a2 = int(a[1])
    b = str(a1 + a2)
    if len(b) < 2:
        a = a[1] + b
    else:
        a = a[1] + b[1]
    s += 1
    if a==c:
        break
print(s)