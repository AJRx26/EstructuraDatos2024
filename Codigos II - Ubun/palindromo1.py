def palindromo(cadena):
    return cadena == cadena[::-1]

if __name__ == "__main__":
    cadena = input()
    if palindromo(cadena):
        print("True")
    else:
        print("False")
