class Nodo():
    def __init__(self,valor):
        self.valor = valor
        self.siguiente = None 
        
class Lista():
    def __init__(self):
        self.cabeza = None
        
    def append(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        
        aux = self.cabeza
        while aux.siguiente != None:
            aux = aux.siguiente
        aux.siguiente = nuevo_nodo

    def get(self, pos):
        
        if pos < 0:
            return None
        aux = self.cabeza
        indice = 0
        while aux is not None:
            if indice == pos:
                return aux.valor
            aux = aux.siguiente
            indice += 1
        return None
    
if __name__=='__main__':
    p=int(input())
    n=int(input())
    l=Lista()
    for _ in range(n):
        l.append(int(input()))
    
    print(l.get(p))