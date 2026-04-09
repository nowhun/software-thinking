a = int(input())
b = []
for i in range(a):
    b.append(int(input()))
b.sort()
for j in range(len(b)):
    print(b[j])