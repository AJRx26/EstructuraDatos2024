def xor(booleano1, booleano2):
    if booleano1 == booleano2:
        return False
    return True

booleano1 = bool(int(input()))
booleano2 = bool(int(input()))

resultado=xor(booleano1, booleano2)
print(resultado)