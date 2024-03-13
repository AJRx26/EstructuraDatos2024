def eliminar(lista, y):
    lista2=[num for num in lista if num != y]
    return lista2

if __name__ == '__main__':
    y=int(input())
    x=int(input())    
    lista=[int(input()) for _ in range(x)]
    
    res=eliminar(lista, y)
    print(res)