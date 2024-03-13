def formato(plantilla):
    dato = int(plantilla.split('.'))
    for i in dato:
        print()
        
age=input()
name=input()
plantilla = 'Hola {nombre}, tu edad es {edad}, adiós {nombre}'
print(plantilla.format(edad=age, nombre=name))