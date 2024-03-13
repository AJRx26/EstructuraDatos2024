class Ruta():
    def __init__(self, entrada):
        self.entrada = entrada
        self.directorio = self.obtener_directorio()
        self.archivo = self.obtener_archivo()
        self.extension = self.obtener_extension()

    def obtener_directorio(self):
        if '/' not in self.entrada:
            return './'
        else:
            directorio1= self.entrada.find('/')
            directorio2= self.entrada.rfind('/')
            return self.entrada[directorio1:directorio2 + 1]

    def obtener_archivo(self):
        archivo1 = self.entrada.rfind('/')
        archivo2 = self.entrada.rfind('.')
        return self.entrada[archivo1 + 1: archivo2]

    def obtener_extension(self):
        archivo2 = self.entrada.rfind('.')
        return self.entrada[archivo2 + 1:]

    def __repr__(self):
        return "directorio:%s:archivo:%s:extension:%s" % (self.directorio, self.archivo, self.extension)

if __name__ == '__main__':
    entrada = input("")
    print(Ruta(entrada))