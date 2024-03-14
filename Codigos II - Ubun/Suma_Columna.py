def CrearColumna(f,c):
    m = []
    for i in range(f):
        l = []
        for j in range(c):
            num = int(input())
            l.append(num)
        m.append(l)
    return m

def ListaSumar(m,f,c):
    listasumas = []
    lista = []
    sum = 0
    for i in range(c):
        for j in range(f):
            sum += m[j][i]
            lista = sum
        listasumas.append(lista)
        sum = 0
    return listasumas

def ImprimirLista(listasumas):
    print(",".join(map(str, listasumas))) 

f = int(input())
c = int(input())
m = CrearColumna(f,c)
lista = ListaSumar(m,f,c)
ImprimirLista(lista)


