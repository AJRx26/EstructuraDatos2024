class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
def crear_lista(numero):
    lista = []
    for i in range(numero):
        num = int(input())
        lista.append(num)
    return lista

def interseccion_listas(lista1, lista2):
    valores_set = set(lista1) & set(lista2)

    resultado = None
    for valor in sorted(valores_set, reverse=True):
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
    lista1 = crear_lista(n)    
    lista2 = crear_lista(m)

    interseccion = interseccion_listas(lista1, lista2)
    imprimir_lista(interseccion)

