def Crear_matriz(x, y):
    matriz = []
    for i in range(x):
        l = []
        for j in range(y):
            v = int(input())
            l.append(v)
        matriz.append(l)
    return m

def Sumar_matriz(matriz,x,y):
    sum = 0
    for i in range(x):
        for j in range(y):
            if i == j:
                sum += matriz[i][j]
    return sum


x = int(input())
y = int(input())
matriz = Crear_matriz(x,y)
print(Sumar_matriz(matriz,x,y))

