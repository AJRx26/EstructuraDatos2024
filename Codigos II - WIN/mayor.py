def encontrar_mayor(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    else:
        mayor = lista[0]
        for elemento in lista:
            if elemento > mayor:
                mayor = elemento
        return mayor

# Ejemplo de uso
def main():
    try:
        x = int(input("Ingrese el tamaño de la lista de enteros: "))
        lista = []
        for i in range(x):
            elemento = int(input(f"Ingrese el elemento {i + 1}: "))
            lista.append(elemento)
        
        resultado = encontrar_mayor(lista)
        print("El elemento mayor es:", resultado)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
