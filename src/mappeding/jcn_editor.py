import os
import sys

def limpiar_pantalla():
    # Comando rápido de sistema para mantener la interfaz limpia
    os.system('cls' if os.name == 'nt' else 'clear')

print("=== JAVACRAFT LINE-EDITOR v1.0.0 ===")
print("1. Crear nuevo archivo .equ")
print("2. Retomar un archivo existente")
opcion = input("Seleccione una opción (1-2): ").strip()

nombre_archivo = "jcn-1.12.2.equ"
lineas = []

if opcion == "2":
    nombre_archivo = input("Nombre del archivo a abrir (defecto: jcn-1.12.2.equ): ").strip() or "jcn-1.12.2.equ"
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            lineas = [linea.rstrip('\n') for linea in f.readlines()]
        print(f"[+] Archivo cargado con {len(lineas)} líneas.")
    else:
        print("[-] El archivo no existe. Se creará uno nuevo.")

# Elegir desde qué línea arrancar/editar
if lineas:
    try:
        entrada_linea = input(f"Escriba el número de línea para empezar (1-{len(lineas) + 1}, Enter para el final): ").strip()
        puntero_linea = int(entrada_linea) - 1 if entrada_linea else len(lineas)
    except ValueError:
        puntero_linea = len(lineas)
else:
    puntero_linea = 0

print("\n[+] Entrando al modo ráfaga. Escribí en minúsculas. Doble Enter o 'salir' para terminar.")
input("Presioná Enter para empezar...")

# Inicializamos el estado del registro de control antes de entrar al bucle
vago_check = False

# --- BUCLE PRINCIPAL (Lector línea por línea con actualización estática) ---
while True:
    limpiar_pantalla()
    
    # 3. Pantalla que te dice en qué línea estás y muestra el contexto
    print("=====================================================================")
    print(f" EDITOR JAVACRAFT NATIVO | MODO: MANU-MAPPING | ARCHIVO: {nombre_archivo}")
    print("=====================================================================")
    
    # Mostrar las 3 líneas anteriores para tener contexto visual de qué venías escribiendo
    inicio_vista = max(0, puntero_linea - 3)
    for idx in range(inicio_vista, puntero_linea):
        print(f"  {idx + 1}: {lineas[idx]}")
        
    print(f"--> {puntero_linea + 1}: [Escribiendo acá...]")
    print("=====================================================================")

    # 4. Entrada de texto
    entrada = input(">>> ").strip()
    
    # Control de salida explícito
    if entrada.lower() == 'salir':
        break
        
    # Control de doble Enter seguro
    #if entrada == "":
    #    if vago_check:
    #        break  # Segundo Enter consecutivo vacío -> Salir
    #    vago_check = True
        
        # Un enter vacío simple te permite avanzar de línea o dejar un espacio
        if puntero_linea >= len(lineas):
            lineas.append("")
        puntero_linea += 1
        continue
    else:
        vago_check = False  # Si escribió algo, se resetea el registro de control

    # Procesamiento del Mapping: Si usás '::', pasamos a mayúsculas sólo el token izquierdo
    if "::" in entrada:
        izq, der = entrada.split("::", 1)
        linea_procesada = f"{izq.strip().upper()} :: {der.strip()}"
    else:
        # Si es un comentario o directiva simple
        if entrada.startswith("#"):
            linea_procesada = entrada
        else:
            linea_procesada = entrada.upper()

    # Inserción o reemplazo en la lista de líneas
    if puntero_linea < len(lineas):
        lineas[puntero_linea] = linea_procesada
    else:
        lineas.append(linea_procesada)
        
    # 5. Contador de líneas (Avanza el puntero posicional)
    puntero_linea += 1

    # Guardado directo (Seguridad ante cortes de energía o bloqueos)
    with open(nombre_archivo, "w", encoding="utf-8") as f_out:
        f_out.write("\n".join(lineas) + "\n")

limpiar_pantalla()
print(f"[+] Proceso terminado. Archivo '{nombre_archivo}' guardado de forma segura con {len(lineas)} líneas.")
