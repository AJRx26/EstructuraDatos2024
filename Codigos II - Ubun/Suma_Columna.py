def Crear_columna(x, y):
    col = []
    for i in range(x):
        l = []
        for j in range(y):
            num = int(input())
            l.append(num)
        col.append(l)
    return col

def Sumar_lista(col,x,y):
    lista2 = []
    lista = []
    sum = 0
    for i in range(y):
        for j in range(x):
            sum += col[j][i]
            lista = sum
        lista2.append(lista)
        sum = 0
    return lista2

def ImprimirLista(lista2):
    print(",".join(map(str, lista2))) 

x = int(input())
y = int(input())
col = Crear_columna(x, y)
lista = Sumar_lista(col, x, y)
ImprimirLista(lista)


