class RutaUnix:
    def __init__(self, entrada):
        self.entrada = entrada
        self.directorio = self.obtener_directorio()
        self.archivo = self.obtener_archivo()
        self.extension = self.obtener_extension()

    def obtener_directorio(self):
        if '/' not in self.entrada:
            return './'
        else:
            diagonal = self.entrada.rfind('/')
            return self.entrada[:diagonal + 1]

    def obtener_archivo(self):
        diagonal = self.entrada.rfind('/')
        return self.entrada[diagonal + 1:]

    def obtener_extension(self):
        punto = self.entrada.rfind('.')
        if punto == -1:
            return ''
        else:
            return self.entrada[punto + 1:]

    def __repr__(self):
        return "directorio:%s:archivo:%s:extension:%s" % (self.directorio, self.archivo, self.extension)

if __name__ == '__main__':
    entrada = input("")
    ruta_objeto = RutaUnix(entrada)
    print(ruta_objeto)
