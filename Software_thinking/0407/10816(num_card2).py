a = int(input())
dic = {}
card = list(map(int, input().split()))
b = int(input())
num = list(map(int, input().split()))

for i in num:
    dic[i] = 0

c =[]
for j in card:
    if j in dic:
        dic[j] += 1

for k in num:
    c.append(dic[k])
    
print(*c, sep=' ')