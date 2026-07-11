import sys
import os

archivo_api = "jcn_automatico_completo.equ"

if not os.path.exists(archivo_api):
    print(f"[-] No se encuentra el mapa de la API: {archivo_api}")
    sys.exit(1)

print("=== JAVACRAFT LEXICON DICTIONARY ===")
print("Escribí palabras clave (ej: 'network', 'crash') para buscar macros.")
print("Introduce 'salir' para terminar.\n")

# Cargamos el megabyte de texto en la RAM (para Python 1 MB es un vuelto)
with open(archivo_api, "r", encoding="utf-8") as f:
    diccionario = [linea.strip() for linea in f if "::" in linea]

while True:
    busqueda = input("Buscar macro >>> ").strip().lower()
    if busqueda == "salir" or not busqueda:
        break
        
    # Filtrado difuso: la línea debe contener todas las palabras clave separadas por espacio
    palabras = busqueda.split()
    resultados = [l for l in diccionario if all(p in l.lower() for p in palabras)]
    
    print("-" * 55)
    if resultados:
        # Mostramos los primeros 15 resultados para no inundar la pantalla del celular
        for r in resultados[:15]:
            macro, real = r.split("::", 1)
            print(f"\033[92m{macro.strip()}\033[0m -> {real.strip()}")
        if len(resultados) > 15:
            print(f"... y otros {len(resultados) - 15} resultados más.")
    else:
        print("[-] No se encontraron coincidencias para esa estructura.")
    print("-" * 55)
