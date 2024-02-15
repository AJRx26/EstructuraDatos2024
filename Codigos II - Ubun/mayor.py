def sum(lista,x):
    mayor = lista[0]
    for numero in range(x):
        if mayor < lista[numero]:
            mayor = lista[numero]
    
    return mayor

lista = []
x = int(input())
for i in range(x):
    elemento = int(input())
    lista.append(elemento)

mayor = sum(lista,x)
print(mayor)