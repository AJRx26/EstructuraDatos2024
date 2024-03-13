def obtener_matriculas(cadenas):
    matriculas = []
    for cadena in cadenas:
        # Buscamos la posición del primer paréntesis
        indice_inicio = cadena.find("(")
        # Buscamos la posición del último paréntesis
        indice_fin = cadena.find(")")
        # Extraemos la matrícula entre los paréntesis
        matricula = cadena[indice_inicio + 1:indice_fin]
        matriculas.append(matricula)
    return matriculas

# Ejemplo de uso
n = int(input())
cadenas = []
for _ in range(n):
    cadena = input()
    cadenas.append(cadena)

matriculas_obtenidas = obtener_matriculas(cadenas)
for matricula in matriculas_obtenidas:
    print(matricula)
