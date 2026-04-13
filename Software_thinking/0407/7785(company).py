dic = {}
c = int(input())
for i in range(c):
    a, b = input().split()
    dic[a] = b
p = []
for i in dic:
    if dic[i] == "enter":
        p.append(i)
p.sort(reverse=True)
print(*p, sep=' ')