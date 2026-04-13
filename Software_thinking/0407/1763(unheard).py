a, b = map(int, input().split())
dic = {}
for i in range(a):
    p = input()
    dic[p] = 0
    dic[p] += 1
for i in range(b):
    p = input()
    if p in dic:
       dic[p] += 1
result = []
for i in dic:
    if dic[i] == 2:
        result.append(i)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])