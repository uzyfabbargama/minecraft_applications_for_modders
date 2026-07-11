# =====================================================================
# GENERATOR JAVACRAFT NATIVO (JCN) - FORZADO HARDCODED DE BAJO NIVEL
# =====================================================================

# 1. Cargamos el archivo nativo que ya generamos para buscar los códigos ofuscados reales
mapa_nativo = {}
with open("mcp_nativo_1.12.2.equ", "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if "::" in linea:
            clave, valor = linea.split("::", 1)
            mapa_nativo[clave.strip()] = valor.strip()

# 2. Diccionario de equivalencia directa: Tu Macro -> Macro de MCP Nativo
# Esto asegura que conectamos tu sintaxis limpia con el binario real de Mojang
equivalencias_directas = {
    "SEND_MSG(usr, text)": mapa_nativo.get("MC_SENDMESSAGE(usr, args)", "usr.a(text)").replace("args", "new net.minecraft.util.text.TextComponentString(text)"),
    "GET_HEALTH(usr)": mapa_nativo.get("MC_GETHEALTH(usr, args)", "usr.cd()").replace("(args)", "()"),
    "SET_HEALTH(usr, val)": mapa_nativo.get("MC_SETHEALTH(usr, args)", "usr.c(val)").replace("args", "val"),
    "GET_WORLD(usr)": "usr.l", # En Vanilla 1.12.2, el campo world de Entity es .l
}

# 3. Generamos el archivo jcn-1.12.2.equ definitivo
jcn_lineas = [
    "# =====================================================================",
    "# JAVACRAFT NATIVO (JCN) - MINECRAFT 1.12.2 VANILLA SEGURO",
    "# Sintaxis unificada directa al binario ofuscado (Zero Abstracción)",
    "# =====================================================================\n"
]

# Añadimos los IMPORTS limpios de Minecraft Vanilla (adiós Forge/Bukkit)
jcn_lineas.append("IMPORT_PLAYER() :: import net.minecraft.entity.player.EntityPlayer;")
jcn_lineas.append("IMPORT_WORLD() :: import net.minecraft.world.World;")
jcn_lineas.append("IMPORT_CHAT() :: import net.minecraft.util.text.TextComponentString;")

# Inyectamos las macros procesadas directas
for macro_usr, codigo_ofuscado in equivalencias_directas.items():
    jcn_lineas.append(f"{macro_usr} :: {codigo_ofuscado}")

# Guardamos el archivo
with open("jcn-1.12.2.equ", "w", encoding="utf-8") as f_out:
    f_out.write("\n".join(jcn_lineas))

print("[+] ¡jcn-1.12.2.equ unificado y forzado con éxito!")
