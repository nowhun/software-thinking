import random

N = int(input())

def make(n):
    mat = []
    for i in range(n):
        m = []
        for j in range(n):
            m.append(random.randint(1, n*n*10))
        mat.append(m)
    return mat

def show(m):
    for i in m:
        for j in i:
            print(f"{j:5}", end='')
        print()

A = make(N)
Trans = []
for i in range(N):
    x = []
    for j in range(N):
        x.append(A[j][i])
    Trans.append(x)
show(Trans)