# AUTOGENERADO - no tocar
# =====================================================================
# MOTOR INTEGRADO JAVACRAFT - FILOSOFÍA DE BAJO NIVEL (REGISTROS)
# =====================================================================
import sys

# manos (Registros de trabajo)
h1 = 0 # hand 1
h2 = 0 # hand 2
caracter = 0
puntero_fuente = 0

# Tablas del Entorno de Equivalencias (.equ)
lista_claves = []      # Hashes xorid de las macros (ej: SEND_MSG)
lista_anclas = []      # Punteros (inicio, fin) del fragmento Java
lista_parametros_equ = []  # NUEVO: Guarda las listas de variables molde de cada macro

# Datos del sistema (Validación de los 3 argumentos de consola)
if len(sys.argv) < 4:
    print("Uso: python3 javacraft.py <origen> <destino> <equivalencias>")
    sys.exit(1)

arg1 = sys.argv[1] # Archivo fuente (.jc)
arg2 = sys.argv[2] # Archivo de salida (.java)
arg3 = sys.argv[3] # Tabla de equivalencias (.equ)

try:
    with open(arg1, "r") as f_a:
        codigo_fuente = f_a.read()
    print("Archivo fuente detectado...")
    
    with open(arg3, "r") as f_b: # Cargamos las equivalencias desde el tercer argumento
        jc_equ = f_b.read()
    print("Tabla de equivalencias detectada...")
except Exception as e:
    print(f"Archivos no encontrados: {e}")
    sys.exit(1)

# Buffer global para acumular el código Java generado
codigo_java_final = ""


#======
# MACROS
#======
        
            
            
    
                
            
            
                

        
        
            
                
                
                
                
                
                
                            

# --- PIPELINE DE EJECUCIÓN LINEAL ---

# Paso 1: Cargamos de forma lineal toda la ROM de configuraciones del .equ
while True:
    if caracter >= len(jc_equ):
        retorno = False # Llegamos al final de la ROM del .equ
    else:
        h1 ^= h1
        h2 ^= h2
        h1 = ord(jc_equ[caracter]) # pongo un byte en mi mano
        if h1 != 35 and h1 != 10 and h1 != 13: # No es '#' (comentario) ni salto de línea
            # --- Lector del Token Javacraft (Xorid Hash) ---
            while h1 != ord(" ") and h1 != ord("("):
                h2 ^= h1
                h2 <<= 1
                caracter += 1
                if caracter >= len(jc_equ): break
                h1 = ord(jc_equ[caracter])
            # NUEVO: Justo cuando h1 es '(' o avanzamos, extraemos los parámetros del molde
            # Buscamos los límites del paréntesis de definición en el .equ
            idx_p = caracter
            while idx_p < len(jc_equ) and ord(jc_equ[idx_p]) != ord("("):
                idx_p += 1
            idx_p += 1
            inicio_p = idx_p
            while idx_p < len(jc_equ) and ord(jc_equ[idx_p]) != ord(")"):
                idx_p += 1
            fin_p = idx_p
            # Sacamos las variables limpias (ej: ["world", "x", "y", "z", "id"])
            params_molde = [p.strip() for p in jc_equ[inicio_p:fin_p].split(",") if p.strip()]
            lista_parametros_equ.append(params_molde)
            lista_claves.append(h2) # Movemos el hash a lista_claves
            # --- Avanzamos hasta encontrar el divisor '::' ---
            h2 ^= h2 # lavo mi otra mano
            while caracter < len(jc_equ):
                h1 = ord(jc_equ[caracter])
                if h1 == ord(":"):
                    h2 ^= h1
                    h2 <<= 1
                    if h2 == 0x9c: # Constante mágica que detecta "::"
                        caracter += 1 # Salteamos el segundo ':'
                        break
                caracter += 1
            # Salteamos posibles espacios después del '::'
            if caracter < len(jc_equ):
                h1 = ord(jc_equ[caracter])
                while h1 == ord(" "):
                    caracter += 1
                    h1 = ord(jc_equ[caracter])
            # --- EL TRUCO DEL ANCLA (Punteros puros de texto) ---
            inicio_reemplazo = caracter
            while caracter < len(jc_equ) and ord(jc_equ[caracter]) != 10 and ord(jc_equ[caracter]) != 13:
                caracter += 1
            fin_reemplazo = caracter
            # Guardamos el mapa físico del trozo de código Java
            lista_anclas.append((inicio_reemplazo, fin_reemplazo))
            # Consumimos el salto de línea sobrante
            if caracter < len(jc_equ):
                caracter += 1
        else:
            # Si es un comentario o línea vacía, saltamos directamente al siguiente \n
            while caracter < len(jc_equ) and ord(jc_equ[caracter]) != 10:
                caracter += 1
            caracter += 1 # Saltamos el \n
        retorno = True
    continuar = retorno
    if not continuar:
        break

# Paso 2: Procesamos el archivo de código fuente completo usando el lector plano
while puntero_fuente < len(codigo_fuente):
    # 1. Limpiamos espacios y saltos de línea iniciales mandándolos directo a la salida
    while puntero_fuente < len(codigo_fuente) and (ord(codigo_fuente[puntero_fuente]) in [10, 13, 32]):
        codigo_java_final += codigo_fuente[puntero_fuente]
        puntero_fuente += 1
    if puntero_fuente >= len(codigo_fuente):
        retorno = False
    else:
        # Obtenemos el byte actual
        h1 = ord(codigo_fuente[puntero_fuente])
        # --- FILTRO ANTIPÁJAROS ---
        # Las macros de Javacraft SIEMPRE empiezan con mayúscula (A-Z, ord 65 a 90)
        # Si no es una mayúscula, es Java puro. Lo copiamos y avanzamos de inmediato.
        if h1 < 65 or h1 > 90:
            codigo_java_final += codigo_fuente[puntero_fuente]
            puntero_fuente += 1
        else:
            # Si es una mayúscula, guardamos el inicio por si la macro resulta no existir
            puntero_ancla_java = puntero_fuente
            h2 ^= h2
            dedos = 0
            # Leemos el token potencial
            while puntero_fuente < len(codigo_fuente) and h1 != ord(" ") and h1 != ord("("):
                h2 ^= h1
                h2 <<= 1
                puntero_fuente += 1
                if puntero_fuente >= len(codigo_fuente): break
                h1 = ord(codigo_fuente[puntero_fuente])
            # Buscamos el Hash
            while dedos < len(lista_claves) and h2 != lista_claves[dedos]:
                dedos += 1
            # ¿Es una macro real mapeada en el .equ?
            if dedos < len(lista_claves) and h2 == lista_claves[dedos]:
                # Extraemos argumentos del usuario
                while puntero_fuente < len(codigo_fuente) and ord(codigo_fuente[puntero_fuente]) != ord("("):
                    puntero_fuente += 1
                puntero_fuente += 1 # saltamos el '('
                inicio_args = puntero_fuente
                while puntero_fuente < len(codigo_fuente) and ord(codigo_fuente[puntero_fuente]) != ord(")"):
                    puntero_fuente += 1
                fin_args = puntero_fuente
                puntero_fuente += 1 # saltamos el ')'
                args_usuario = [a.strip() for a in codigo_fuente[inicio_args:fin_args].split(",")]
                params_plantilla = lista_parametros_equ[dedos]
                inicio_java, fin_java = lista_anclas[dedos]
                plantilla_java = jc_equ[inicio_java:fin_java]
                codigo_generado = plantilla_java
                for p_idx, param in enumerate(params_plantilla):
                    if param in args_usuario:
                        u_idx = args_usuario.index(param)
                        codigo_generado = codigo_generado.replace(param, args_usuario[u_idx])
                    else:
                        if p_idx < len(args_usuario):
                            codigo_generado = codigo_generado.replace(param, args_usuario[p_idx])
                codigo_java_final += codigo_generado + "\n"
            else:
                # Si empezaba con mayúscula pero NO era una macro (ej: la clase "Microcontroller")
                # hacemos rollback al inicio de la palabra, copiamos el primer carácter y avanzamos 1
                puntero_fuente = puntero_ancla_java
                codigo_java_final += codigo_fuente[puntero_fuente]
                puntero_fuente += 1

# Paso 3: Guardamos el resultado consolidado en el archivo <destino>
nombre_salida = arg2
try:
    with open(nombre_salida, "w") as f_out:
        f_out.write(codigo_java_final)
    print(f"\n[+] ¡TRANSPILACIÓN EXITOSA!")
    print(f"Código Java guardado en: '{nombre_salida}'")
except Exception as e:
    print(f"Error al escribir el archivo de salida: {e}")
