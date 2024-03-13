import os
import sys

def contar_archivos(ruta):
    if not os.path.isdir(ruta):
        raise ValueError("La ruta proporcionada no es un directorio válido.")
    
    archivos = os.listdir(ruta)
    return len(archivos)

def main():
    # Validar que se reciba un parámetro
    if len(sys.argv) != 2:
        print("Uso: python programa.py <directorio>")
        sys.exit(1)
    
    directorio = sys.argv[1]
    
    try:
        total_archivos = contar_archivos(directorio)
        print(f"El número total de archivos en el directorio '{directorio}' es: {total_archivos}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()