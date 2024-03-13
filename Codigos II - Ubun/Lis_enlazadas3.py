class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

def lista_enlazada_a_lista(lista):
    resultado = []
    aux = lista
    while aux:
        resultado.append(aux.valor)
        aux = aux.siguiente
    return resultado

def interseccion_listas(lista1, lista2):
    valores_comunes = list(set(lista_enlazada_a_lista(lista1)) & set(lista_enlazada_a_lista(lista2)))

    resultado = None
    for valor in sorted(valores_comunes, reverse=True):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = resultado
        resultado = nuevo_nodo

    return resultado

def imprimir_lista(lista):
    if lista is None:
        print("[]")
        return
    resultado = []
    aux = lista
    while aux:
        resultado.append(aux.valor)
        aux = aux.siguiente
    print(resultado)

if __name__ == "__main__":
    x = int(input())
    valores1 = []
    for _ in range(x):
        valor = int(input())
        valores1.append(valor)

    y = int(input())
    valores2 = []
    for _ in range(y):
        valor = int(input())
        valores2.append(valor)

    lista1 = None
    for valor in reversed(valores1):
        nodo = Nodo(valor)
        nodo.siguiente = lista1
        lista1 = nodo

    lista2 = None
    for valor in reversed(valores2):
        nodo = Nodo(valor)
        nodo.siguiente = lista2
        lista2 = nodo

    interseccion = interseccion_listas(lista1, lista2)
    imprimir_lista(interseccion)
