class Usuario():
    def __init__(self, usuario, clase, grupo):
        self.usuario = usuario
        self.clase = clase
        self.grupo = grupo
        
        if clase == 1 and grupo == 1:
            self.tipo='root'
        else:
            self.tipo = 'normal'
        
        
    def __repr__(self):
        return '%s (%s)' % (self.usuario, self.tipo)
    
if __name__ == '__main__':
    entrada = input()
    partes = entrada.split(':')
    usuario=partes[0]
    clase=int(partes[1])
    grupo = int(partes[2])
    print(Usuario(usuario, clase, grupo))
