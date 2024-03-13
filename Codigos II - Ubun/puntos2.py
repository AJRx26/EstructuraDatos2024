def contar_puntos(cadena):
    cadena_limpia = ""
    for i in range(len(cadena)):
        if cadena[i] == ".":
            # Si el siguiente caracter no es un punto, lo agregamos a la cadena limpia
            if i == len(cadena) - 1 or cadena[i + 1] != ".":
                cadena_limpia += "."
    return cadena_limpia.count(".")

cadena = input()
resultado = contar_puntos(cadena)
print(resultado)