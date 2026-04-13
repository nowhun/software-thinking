a, b = map(int, input().split())
dic = {}

for i in range(b):
    c = input()
    if c in dic:
        dic.pop(c)
        dic[c] = 0
    else:
        dic[c] = 0
result = []

for i in dic:
    result.append(i)

for i in range(a):
    print(result[i])