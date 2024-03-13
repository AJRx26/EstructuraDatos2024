def obtener_matriculas(cadenas):
    matriculas = []
    for cadena in cadenas:
        partes = cadena.split('(')
        #"rstrip" eliminar caracteres específicos
        matricula = partes[1].rstrip(')')
        matriculas.append(matricula)
    return matriculas

n = int(input())
cadenas = []
for _ in range(n):
    cadena=input()
    cadenas.append(cadena)

matriculas = obtener_matriculas(cadenas)
for matricula in matriculas:
    print(matricula)
