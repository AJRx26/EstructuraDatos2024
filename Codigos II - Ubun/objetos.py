class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumar1(self):
        self.numerador += 1

    # función que se invoca al hacer print del objeto
    def __repr__(self):
        return '%s/%s' % (self.numerador, self.denominador)

    # suma la fracción actual y otra y regresa la suma
    def sumar_fracciones(self, otra_fraccion):
        comun_denominador = self.denominador * otra_fraccion.denominador
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        return Fraccion(nuevo_numerador, comun_denominador)

f1 = Fraccion(1, 2)
print(f1)
f1.sumar1()
print(f1)
f2 = Fraccion(1, 4)
print(f2)
nueva = f1.sumar_fracciones(f2)
print(nueva)
