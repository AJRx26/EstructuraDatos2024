def mult(lista,num):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

lista = []
num = int(input())
for i in range(num):
    elemento = int(input())
    lista.append(elemento)
    
resultado = mult(lista, num)
print(resultado)
