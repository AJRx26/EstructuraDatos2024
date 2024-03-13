import os
import sys

def contar_archivos(ruta):
    if os.path.isdir(ruta):
        print(len(os.listdir(ruta)))
        return
    
if len(sys.argv) != 2:
    print("Uso: import_os_contar_ar.py<directorio>")
    sys.exit(1)
    
ruta = sys.argv[1]
contar_archivos(ruta) 
    
