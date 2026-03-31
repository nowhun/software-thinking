a = int(input())

for i in range(a):
    if (a%2 == 0):
        print("* "*(a//2))
        print(" *"*(a//2))
    else:
        print("* "*((a//2)+1))
        print(" *"*(a//2))

