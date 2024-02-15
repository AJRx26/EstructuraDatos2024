x = int(input())
lista = []

if x == 0:
    print('sin datos')
    exit
    
for _ in range(x):
    lista.append(input())

for elemento in lista:
    print(elemento)