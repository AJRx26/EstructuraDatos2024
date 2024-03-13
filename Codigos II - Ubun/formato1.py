def formato(cadena):
    nombre, edad, grado = cadena.split('.')
    xml = f"<nombre>{nombre}</nombre><edad>{edad}</edad><grado>{grado}</grado>"
    return xml
    
cadena = input()
xml = formato(cadena) 
print(xml)



