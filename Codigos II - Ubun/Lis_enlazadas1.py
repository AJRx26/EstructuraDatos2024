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
    aux1 = lista1
    aux2 = lista2
    resultado = None

    while aux1 is not None and aux2 is not None:
        if aux1.valor == aux2.valor:
            nuevo_nodo = Nodo(aux1.valor)
            if not resultado or resultado.valor != nuevo_nodo.valor:
                nuevo_nodo.siguiente = resultado
                resultado = nuevo_nodo
            aux1 = aux1.siguiente
            aux2 = aux2.siguiente
        elif aux1.valor < aux2.valor:
            aux1 = aux1.siguiente
        else:
            aux2 = aux2.siguiente

    return resultado

def ordenar_lista(lista):
    lista_valores = lista_enlazada_a_lista(lista)
    lista_valores.sort()
    resultado = None
    for valor in lista_valores[::-1]:
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

    lista1 = ordenar_lista(lista1)
    lista2 = ordenar_lista(lista2)

    interseccion = interseccion_listas(lista1, lista2)
    imprimir_lista(interseccion)
