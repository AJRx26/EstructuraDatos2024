def contar_puntos(cadena):
    puntos = 0
    punto_anterior = False
    for caracter in cadena:
        if caracter == '.':
            if not punto_anterior:
                puntos += 1
            punto_anterior = True
        else:
            punto_anterior = False
    return puntos

cadena = input()
resultado = contar_puntos(cadena)
print(resultado)
