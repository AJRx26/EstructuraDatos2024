def regresar_valor_mitad(lista):
    if not lista:  # Verificar si la lista está vacía
        return None
    
    mitad = len(lista) // 2  # División entera para obtener un índice entero
    
    if isinstance(lista[mitad], int):  # Verificar si el elemento a la mitad es un número
        if len(lista) % 2 == 0:
            return lista[mitad - 1] + lista[mitad]  # Sumar los dos números a la mitad si el número de elementos es par
        else:
            return lista[mitad]
    else:
        return None  # Devolver None si algún elemento no es un número

# Pruebas, deben pasar todas
print(regresar_valor_mitad([1, 2, 3]) == 2)
print(regresar_valor_mitad([5]) == 5)
print(regresar_valor_mitad([]) == None)
print(regresar_valor_mitad([1, 2]) == 3)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 6]) == 7)
print(regresar_valor_mitad([1, 'hola', 3]) == None)
print(regresar_valor_mitad([1, 2, 3, 4, 5, 'hola']) == None)