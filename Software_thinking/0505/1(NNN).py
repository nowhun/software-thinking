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
B = make(N)
C = make(N)

AB = []
for i in range(N):
    hap = []
    for j in range(N):
        x = 0
        for k in range(N):
            x += A[i][k] * B[k][j]
        hap.append(x)
    AB.append(hap)

ABC = []
for i in range(N):
    hap =[]
    for j in range(N):
        hap.append(AB[i][j] + C[i][j])
    ABC.append(hap)

show(ABC)