word = input()
sum = 0
b = 0
for i in range(len(word)):
    if ord(word[i]) > 96:
        sum += ord(word[i])-96
    else:
        sum += ord(word[i])-38
for i in range(2, sum-1):
    if sum % i == 0:
        b = 1
if b == 0:
    print("It is a prime word.")
else:
    print("It is not a prime word.")