# 🚀 Javacraft Nativo — El Patrón Detrás de la Ofuscación

**"Primero hazlo manual, para poder automatizar."** — Filosofía de Javacraft

Bienvenido al repositorio que expone el **secreto mejor guardado de Mojang:** su sistema de ofuscación es una **muñeca rusa de nombres predecibles.**

Aquí no encontrarás un mod. Encontrarás **la herramienta que permite escribir mods para cualquier versión de Minecraft sin depender de Forge ni Fabric.**

---

## 📂 ¿Qué hay aquí?

### 📁 MCP (Mod Coder Pack) — La Base de Datos
| Archivo | Propósito |
|---------|-----------|
| `STATIC_METHODS.txt` | Métodos planos del juego. |
| `fields.csv` | Equivalencias de campos. |
| `joined.srg` | Conexiones entre PK, CL y todo el juego. |
| `methods.csv` | Métodos ordenados según sus campos. |

### 📁 Javacraft — El Motor
| Archivo | Propósito |
|---------|-----------|
| `build_equ.py` | Construye `mcp_nativo_1.12.2.equ` a partir de los archivos de MCP. |
| `build_jcn.py` | Toma el `.equ` nativo y lo fusiona con `jcforge-1.12.2.equ`. |
| `build_jcn_fixed.py` | Versión menos flexible: elimina equivalencias que no están en Forge. |
| `jcforge-1.12.2.equ` | El `.equ` oficial de Forge para 1.12.2. |
| `jcn2-1.12.2.equ` | Experimento generado por `build-jcn-fixed.py` (limitado). |
| `jcn-1.12.2.equ` | **El archivo clave.** Escrito a mano. Analizado. **Y contiene el patrón.** |
| `jcn_editor.py` | Editor manual v1 — demostración de que se puede editar en Python. |
| `jcn_destilador.py` | Editor manual v2 — muestra línea a línea el `.equ` nativo. |

---

## 🧠 El Patrón Oculto en la Ofuscación de Mojang

> *"Resulta que el sistema de mapeos de Mojang es... demasiado simple. Es solo un abecedario con amnesia."*

**Mira esto:**

```java
// clase a (madre)
FIELD_LOGGER(usr) :: usr.a

// clase b (hija)
FIELD_DESCRIPTION(usr) :: usr.b

// clase c (subhija)
FIELD_CAUSE(usr) :: usr.c

// clase d (sub-subhija)
FIELD_THEREPORTCATEGORY(usr) :: usr.d

// y así sucesivamente...
FIELD_CRASHREPORTSECTIONS(usr) :: usr.e
FIELD_CRASHREPORTFILE(usr) :: usr.f
FIELD_FIRSTCATEGORYINCRASHREPORT(usr) :: usr.g
FIELD_STACKTRACE(usr) :: usr.h
FIELD_KEY(usr) :: usr.a
FIELD_VALUE(usr) :: usr.b
FIELD_CRASHREPORT(usr) :: usr.a
FIELD_NAME(usr) :: usr.b
FIELD_CHILDREN(usr) :: usr.c
FIELD_STACKTRACE(usr) :: usr.d
FIELD_CRASHREPORT(usr) :: usr.a
FIELD_NETTY_LEAK_DETECTION(usr) :: usr.a
FIELD_ILLEGAL_STRUCTURE_CHARACTERS(usr) :: usr.b
FIELD_ILLEGAL_FILE_CHARACTERS(usr) :: usr.c
```

### ¿Ves el patrón?

1. **`usr.a`** es siempre la **clase base**.
2. **`usr.b`, `usr.c`, `usr.d`...** son **campos anidados**.
3. Cuando llegas a **`usr.aA`, `usr.aB`, `usr.aC`...** estás en **subcampos de segundo nivel**.

**Es una muñeca rusa de ofuscación.** Y una vez que lo ves, no puedes dejar de verlo.

---

## ⚡ ¿Por qué esto es importante?

### 1. **Forge y Fabric NO son necesarios**
Puedes inyectar código directamente en el JAR de Minecraft. Sin overhead. Sin dependencias. **Solo Java puro.**

### 2. **Es un problema de seguridad**
Si cualquiera puede desofuscar Minecraft con un script de 30 líneas, **la seguridad de Mojang es un castillo de naipes.**

### 3. **Es una oportunidad**
Esta herramienta permite:
- Escribir mods **ultrarrápidos** (sin el overhead de los cargadores).
- Portar mods a **cualquier versión** en minutos. (por ahora 1.12.2, es cuestión de tiempo, para las demás)
- Entender cómo funciona Minecraft **por dentro**.

---

## 🔧 Cómo usar Javacraft Nativo

### 1. Genera el `.equ` nativo
```bash
python3 build_equ.py
```

### 2. Fusiona con Forge (opcional)
```bash
python3 build_jcn.py
```

### 3. Si hay errores, usa la versión fija
```bash
python3 build_jcn_fixed.py
```

### 4. Escribe tu mod en `.jc`
```java
package net.javacraft.testmod;

IMPORT_PLAYER()
IMPORT_WORLD()

public class ModActions {
    public static void giveDiamond(Player jugador) {
        GIVE_ITEM(jugador, "minecraft:diamond", 1);
        SEND_MSG(jugador, "¡Diamante recibido!");
    }
}
```

### 5. Transpila a Java
```bash
python3 javacraft.py mod.jc mod_1.12.2.java jcn-1.12.2.equ
```

### 6. Compila y ejecuta
```bash
javac mod_1.12.2.java
# Inyecta en el JAR de Minecraft o ejecuta con un lanzador personalizado
```

---

## 🧩 Filosofía del Proyecto

| **MCP** | "Hacemos millones de líneas, pero no vemos el patrón. Su ofuscador es perfecto." |
|---------|-------------------------------------------------------------------------------|
| **Forge** | "Nosotros solo le damos nombres bonitos a lo que MCP hizo." |
| **Javacraft** | **"Primero hazlo manual, para poder automatizar."** |

**No esperes a que otros resuelvan el problema. Hazlo tú. Y luego automatiza.**

---

## 🤝 Contribuir

**Necesitamos:**

1. **Equivalencias para más versiones** (1.14.4, 1.16.5, 1.20.4, etc.).
2. **Pruebas** (verificar que los mods generados funcionan).
3. **Documentación** (ejemplos, tutoriales, guías).

**Cómo empezar:**

1. Forkea el repo.
2. Ejecuta `build_equ.py` para generar el `.equ` nativo de tu versión.
3. Analiza el patrón y crea un `.equ` personalizado.
4. Haz un Pull Request.

---

## ⚠️ Advertencia

**Este proyecto es educativo.** Demuestra que la ofuscación de Mojang es predecible y frágil.

**No uses esto para crear malware.** Usa este conocimiento para construir un ecosistema de modding mejor, más rápido y más seguro.

**El poder conlleva responsabilidad.**

---

## 🏆 Créditos

- **Mojang** — por crear un juego que merece ser entendido.
- **MCP (Mod Coder Pack)** — por sentar las bases del modding.
- **Forge y Fabric** — por mantener viva la comunidad.
- **La comunidad de desofuscadores** — por no rendirse nunca.

Y especialmente:

- **Tú, que has llegado hasta aquí.** Porque ahora sabes que la ofuscación no es un muro. Es una puerta que solo necesita la llave correcta.

---

## 📜 Licencia

MIT — Haz lo que quieras, pero **no olvides de dónde viene.**

---

### 🧠 Última Reflexión

> *"No es que Mojang sea tonto. Es que su sistema de ofuscación fue diseñado para detener a usuarios normales, no a programadores determinados."*

**Tú eres un programador determinado.**

**Bienvenido a Javacraft Nativo.**
