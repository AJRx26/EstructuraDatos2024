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
    conjunto1 = set(lista_enlazada_a_lista(lista1))
    conjunto2 = set(lista_enlazada_a_lista(lista2))
    valores_comunes = conjunto1 & conjunto2

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
    n = int(input())
    m = int(input())
    valores1 = list(map(int, input().split(", ")))
    valores2 = list(map(int, input().split(", ")))

    lista1 = None
    for valor in valores1[::-1]:
        nodo = Nodo(valor)
        nodo.siguiente = lista1
        lista1 = nodo

    lista2 = None
    for valor in valores2[::-1]:
        nodo = Nodo(valor)
        nodo.siguiente = lista2
        lista2 = nodo

    interseccion = interseccion_listas(lista1, lista2)
    imprimir_lista(interseccion)
