li = []
for i in range(1, 10001):
    sum = 0
    dig = [int(d) for d in str(i)]
    for k in range(len(dig)):
            sum += dig[k]
    sum += i
    li.append(sum)

for i in range(1, 10001):
      if i not in li:
            print(i)