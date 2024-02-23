# Regresa el valor que está a la mitad de la lista de números
# Si el número de elementos es par, regresar la suma
# del dos números a la mitad
# Si algún elemento no es un número, se regresa None
def regregar_valor_mitad(lista):
    if not lista:
        return None
    
    mitad = len(lista) // 2
    if isinstance(lista[mitad], int):  
        if len(lista) % 2 == 0:
            return lista[mitad - 1] + lista[mitad] 
        else:
            return lista[mitad]
    else:
        return None  

# Pruebas, deben pasar todas
print(regregar_valor_mitad([1, 2, 3]) == 2)
print(regregar_valor_mitad([5]) == 5)
print(regregar_valor_mitad([]) == None)
print(regregar_valor_mitad([1, 2]) == 3)
print(regregar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regregar_valor_mitad([1, 'hola', 3]) == None)
print(regregar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)
