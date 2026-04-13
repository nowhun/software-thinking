c = int(input())
dic = {}
for i in range(c):
    book = input()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 0

max_value = max(dic.values())

result = []
for i in dic:
    if dic[i] == max_value:
        result.append(i)
result.sort()
print(result[0])