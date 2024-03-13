class Nodo:
    def __init__(self, numero):
        self.numero=numero
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_nodo_at_start(self, numero):
        new_nodo = Nodo(numero)
        if (self.head is None):
            self.head = Nodo(numero)  
            return
        
        new_nodo.next = self.head
        self.head = new_nodo
        
    def insert_nodo_at_end(self, numero):
        new_nodo = None(numero)
        if self.head==None:
            self.head = new_nodo
            return
        current=self.head 
        while(current is not None):
            current = current.next