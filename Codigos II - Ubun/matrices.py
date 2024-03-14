def CreateMatrix(r, c):
    m = []
    for i in range(r):
        l = []
        for j in range(c):
            v = int(input())
            l.append(v)
        m.append(l)
    return m

def SumMatrix(m,r,c):
    sum = 0
    for i in range(r):
        for j in range(c):
            if i == j:
                sum += m[i][j]
    return sum


r = int(input())
c = int(input())
m = CreateMatrix(r,c)
print(SumMatrix(m,r,c))

