c = int(input())
for _ in range(c):
    a = input()
    stack = []
    for i in a:
        if i == '(':
            stack.append('(')
        elif i == ')':
            if len(stack) == 0:
                stack.append(')')
                break
            else:
                stack.pop()
    if len(stack) != 0:
        print('NO')
    else:
        print('YES')