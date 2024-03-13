class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    
    def __repr__(self):
        return '%s/%s' % (self.numerador, self.denominador)
    
    #función eq
    def __eq__(self, other):
        if isinstance(other, Fraccion):
            return self.numerador * other.denominador == other.numerador * self.denominador
        else:
            return False

if __name__ == "__main__":
    numerador1 = int(input())
    denominador1 = int(input())
    numerador2 = int(input())
    denominador2 = int(input())

    fraccion1 = Fraccion(numerador1, denominador1)
    fraccion2 = Fraccion(numerador2, denominador2)

    print(fraccion1 == fraccion2)
