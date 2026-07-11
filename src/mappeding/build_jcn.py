# =====================================================================
# GENERADOR JAVACRAFT NATIVO (jcn-1.12.2.equ) - COMPILACIÓN EN LINLINEA
# =====================================================================
import re

# 1. Cargamos el diccionario nativo (Mapea el nombre humano al código ofuscado)
# Ejemplo: "GETHEALTH" -> "usr.al(args)" o similar
mapa_nativo_metodos = {}
mapa_nativo_campos = {}

print("[+] Cargando base de datos nativa...")
with open("mcp_nativo_1.12.2.equ", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if not linea or linea.startswith("#") or "::" not in linea:
            continue
        
        clave, valor = linea.split("::", 1)
        clave = clave.strip()
        valor = valor.strip()
        
        # Separar si es macro de método (MC_) o de campo (FIELD_)
        if clave.startswith("MC_"):
            nombre_humano = clave.replace("MC_", "")
            mapa_nativo_metodos[nombre_humano] = valor
        elif clave.startswith("FIELD_"):
            nombre_humano = clave.replace("FIELD_", "")
            mapa_nativo_campos[nombre_humano] = valor

# 2. Procesamos tu archivo base jcforge-1.12.2.equ para remapear su sintaxis
jcn_lineas = []
jcn_lineas.append("# =====================================================================")
jcn_lineas.append("# JAVACRAFT NATIVO (JCN) - MINECRAFT 1.12.2 VANILLA (SIN FORGE)")
jcn_lineas.append("# Sintaxis unificada directa al binario")
jcn_lineas.append("# =====================================================================\n")

print("[+] Unificando sintaxis desde jcforge-1.12.2.equ...")
with open("jcforge-1.12.2.equ", "r", encoding="utf-8") as f_forge:
    for linea in f_forge:
        linea_limpia = linea.strip()
        if not linea_limpia or linea_limpia.startswith("#"):
            jcn_lineas.append(linea_limpia) # Preservamos comentarios y espacios
            continue
            
        clave_forge, valor_forge = linea_limpia.split("::", 1)
        clave_forge = clave_forge.strip()
        valor_forge = valor_forge.strip()
        
        # Extraemos el nombre de la macro de Forge (ej: GET_HEALTH(usr))
        macro_nombre = clave_forge.split("(")[0].strip()
        macro_args = clave_forge.split("(")[1].replace(")", "").strip() if "(" in clave_forge else ""
        
        # --- LÓGICA DE DETECCIÓN Y REEMPLAZO ESTÁTICO ---
        remapeado = False
        
        # Buscamos si el método de Java tradicional existe en el mapa nativo
        for humano, ofuscado in mapa_nativo_metodos.items():
            # Si el código de Forge usaba el método tradicional (ej: .getHealth())
            if f".{humano.lower()}(" in valor_forge.lower():
                # Adaptamos los argumentos dinámicamente al formato ofuscado nativo
                cuerpo_nativo = ofuscado.split("::")[-1].strip()
                # Reemplazamos las variables genéricas por los argumentos de tu macro
                # Ej: usr.a(args) -> usr.a(text)
                cuerpo_final = cuerpo_nativo.replace("args", macro_args.split(",")[-1].strip())
                jcn_lineas.append(f"{clave_forge} :: {cuerpo_final}")
                remapeado = True
                break
                
        if not remapeado:
            for humano, ofuscado in mapa_nativo_campos.items():
                if f".{humano.lower()}" in valor_forge.lower():
                    cuerpo_final = ofuscado.replace("usr", macro_args.split(",")[0].strip())
                    jcn_lineas.append(f"{clave_forge} :: {cuerpo_final}")
                    remapeado = True
                    break
                    
        # Si es un IMPORT o una estructura especial, la dejamos pasar limpia o la adaptamos
        if not remapeado:
            if "IMPORT_" in macro_nombre:
                # Quitamos la dependencia de Forge cambiando net.minecraftforge por net.minecraft
                valor_clean = valor_forge.replace("net.minecraftforge.", "net.minecraft.")
                jcn_lineas.append(f"{clave_forge} :: {valor_clean}")
            else:
                jcn_lineas.append(f"{linea_limpia} # [Vanilla Passthrough]")

# 3. Guardamos el .equ definitivo
with open("jcn-1.12.2.equ", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(jcn_lineas))

print("\n[+] ¡SINTAXIS UNIFICADA CON ÉXITO!")
print("Archivo 'jcn-1.12.2.equ' listo para usar en modo Vanilla puro.")
