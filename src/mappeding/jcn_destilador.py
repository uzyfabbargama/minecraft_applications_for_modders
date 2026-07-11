import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Archivos de entrada y salida establecidos
archivo_nativo = "mcp_nativo_1.12.2.equ"
archivo_legible = "jcn-1.12.2.equ"

# 1. Cargar el archivo base (el gigante con nombres feos)
lineas_nativas = []
if os.path.exists(archivo_nativo):
    with open(archivo_nativo, "r", encoding="utf-8") as f:
        # Filtramos comentarios o líneas vacías para ir directo al grano
        lineas_nativas = [l.strip() for l in f if "::" in l]
else:
    print(f"[-] No se encontró el archivo origen: {archivo_nativo}")
    exit(1)

# 2. Cargar o crear el archivo de salida para saber por dónde íbamos
lineas_guardadas = []
if os.path.exists(archivo_legible):
    with open(archivo_legible, "r", encoding="utf-8") as f:
        lineas_guardadas = [l.strip() for l in f if l.strip()]

# El contador de líneas procesadas se deduce del tamaño del archivo de salida
puntero_idx = len(lineas_guardadas)

print(f"[+] Archivo origen cargado con {len(lineas_nativas)} definiciones.")
print(f"[+] Ya tenés {puntero_idx} líneas traducidas en tu archivo legible.")
input("Presioná Enter para empezar a destilar...")

vago_check = False

# 3. Bucle principal de mapeo manual
while puntero_idx < len(lineas_nativas):
    limpiar_pantalla()
    
    linea_actual = lineas_nativas[puntero_idx]
    token_izq, codigo_java = linea_actual.split("::", 1)
    token_izq = token_izq.strip()
    codigo_java = codigo_java.strip()
    
    print("=====================================================================")
    print(f" DESTILADOR JAVACRAFT NATIVO | CONTADOR: {puntero_idx + 1}/{len(lineas_nativas)}")
    print("=====================================================================")
    print(f" ORIGINAL FEO : {token_izq}")
    print(f" CODIGO REAL  : {codigo_java}")
    print("=====================================================================")
    print(" Escribí tu versión legible en minúsculas (ej: estilo_visual(usr))")
    print(" 'salir' para terminar | Doble Enter para saltar línea")
    print("=====================================================================")
    
    entrada = input(">>> ").strip()
    
    # Salida explícita
    if entrada.lower() == 'salir':
        break
        
    # Doble enter para saltear tokens que no te interesen mapear ahora
    if entrada == "":
        if vago_check:
            puntero_idx += 1 # Avanza al siguiente sin guardar si tocás enter dos veces
            vago_check = False
            continue
        vago_check = True
        print("\n[!] Presioná Enter otra vez para SALTEAR esta línea...")
        input()
        puntero_idx += 1
        vago_check = False
        continue
    
    vago_check = False
    
    # 4. Procesamiento mágico: convertimos tu entrada a MAYÚSCULAS
    # Si pusiste argumentos en minúsculas tipo 'vida(usr)', podemos dejar 'VIDA(usr)' o todo 'VIDA(USR)'
    # Vamos a pasar a mayúsculas todo el token de la macro para estandarizar
    # Entrada de ejemplo: "estilo_visual(usr, args)"
    if "(" in entrada:
        cabeza, argumentos = entrada.split("(", 1)
        # cabeza = "estilo_visual", argumentos = "usr, args)"
        nueva_macro = f"{cabeza.strip().upper()}({argumentos.strip()}"
    else:
        # Si no tiene parámetros, va a mayúsculas directo
        nueva_macro = entrada.upper()
    nueva_linea_equ = f"{nueva_macro} :: {codigo_java}"
    
    # 5. Guardado en caliente (línea por línea al final del archivo)
    with open(archivo_legible, "a", encoding="utf-8") as f_out:
        f_out.write(nueva_linea_equ + "\n")
        
    puntero_idx += 1

limpiar_pantalla()
print(f"[+] Sesión finalizada. Tu archivo '{archivo_legible}' quedó firme en el disco.")
