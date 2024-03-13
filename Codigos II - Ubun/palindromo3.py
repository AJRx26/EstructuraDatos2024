def es_palindromo(cadena):
#Linea de codigo para quitar los espacios y letras mayusculas
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

if __name__ == "__main__":
    cadena = input()
    if es_palindromo(cadena):
        print("True")
    else:
        print("False")
