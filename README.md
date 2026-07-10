# 🚀 Javacraft (JC) — Zero-Overhead Multi-Version Transpiler for Minecraft Mods

Javacraft es un transpilador de ultra-bajo nivel desarrollado bajo una filosofía de diseño basada en registros lógicos y punteros planos de memoria. Su objetivo es resolver de raíz el problema histórico más grande en el desarrollo de mods de Minecraft (Forge, Fabric, NeoForge): **la fragmentación de versiones y APIs.**

Con Javacraft, escribís la lógica de tu mod **una sola vez** en un archivo híbrido `.jc` y, mediante tablas de equivalencias intercambiables `.equ`, generás código Java puro, optimizado y nativo para cualquier versión del juego (1.12.2, 1.16.5, 1.20.4, etc.) en milisegundos.

---

## 🛠️ La Suite de Herramientas: ¿Cómo funciona el ecosistema?

El proyecto se divide en tres pilares fundamentales que trabajan en pipeline lineal:

### 1. ¿Qué hace `macrosy` (`macrosy6.py`)?
Es nuestro preprocesador y expansor de macros estructurales de bajo nivel. Inspirado en la sintaxis clásica de NASM (Netwide Assembler), `macrosy` procesa directivas como `%macro` y `%endmacro` de forma plana y lineal. 
En lugar de depender de pesados intérpretes, utiliza una arquitectura de reemplazo textual limpia para inyectar bloques lógicos repetitivos o generar la estructura base del transpilador a partir de plantillas sin generar sobrecarga en el sistema.

### 2. ¿Por qué Python?
Porque no queríamos combatir la burocracia corporativa de Java usando más Java. Python nos permite manipular el código fuente como buffers de texto puros y cadenas de bytes a gran velocidad. Al ser un script directo ejecutado desde la terminal (ideal para entornos ligeros como Lubuntu), no requiere tiempos de compilación previos, interfaces pesadas, ni suites corporativas que devoren gigabytes de memoria RAM o desgasten discos mecánicos (HDD). Es computación limpia, quirúrgica y directa.

### 3. ¿Qué hace `javacraft.py`?
Es el núcleo del transpilador. Implementa un analizador léxico ciego guiado por un sistema de **Registros Simulados de Trabajo** (`h1`, `h2`, `dedos`) y un algoritmo de acumulación por desplazamiento de bits llamado **Xorid Hash** (`h2 ^= h1; h2 <<= 1`).
* **Bypass de Compatibilidad Total:** Gracias a su *Filtro Antipájaros* integrado, el motor detecta si una palabra es una macro en mayúsculas. Si lo es, la traduce. Si encuentra código Java nativo (operadores de bits, llaves, declaraciones complejas), el analizador realiza un rollback instantáneo y copia el carácter intacto. Esto permite mezclar libremente macros de JC y Java optimizado en el mismo archivo.

### 4. El Entorno de Equivalencias (`.equ`)
El archivo `.equ` es la ROM de mapeos del sistema. No es código; es una tabla plana que define cómo se traduce cada macro de Javacraft a la sintaxis real de una versión específica de Minecraft. 
Es **100% modificable por el usuario**. Si Mojang cambia el nombre de un método en la versión 1.21, no tocás tu código fuente; solo actualizás una línea en tu `.equ`.



Sintaxis unificada:
```text
SET_BLOCK(world, x, y, z, id) :: world.getBlockAt(x, y, z).setType(Material.id)
SEND_MSG(usr, text) :: usr.sendMessage(new ChatComponentText(text))
```

## 📦 Proyecto de Ejemplo: Un solo código, múltiples eras de Minecraft

Imaginemos que diseñamos un bloque o comando que le da un diamante al jugador y le manda un mensaje. Con Javacraft, escribimos este archivo mod.jc único:

Java
```
package net.javacraft.testmod;

public class AccionMod {
    public static void ejecutar(Player jugador, String nombreItem) {
        // Código híbrido: Mezcla de Java Puro con Macros JC
        if (jugador.isOnline()) {
            GIVE_ITEM(jugador, nombreItem, 1);
            SEND_MSG(jugador, "¡Recibiste tu item de forma branchless!");
        }
    }
}
```
Al procesarlo con diferentes entornos .equ, el motor genera automáticamente las variantes estructurales exactas requeridas por cada API histórica:

### Salida Generada para Minecraft 1.12.2 (API Clásica de Bukkit/Forge)

Java
```
package net.javacraft.testmod;

public class AccionMod {
    public static void ejecutar(Player jugador, String nombreItem) {
        if (jugador.isOnline()) {
            jugador.getInventory().addItem(new ItemStack(Material.getMaterial(nombreItem), 1));
            jugador.sendMessage(new ChatComponentText("¡Recibiste tu item de forma branchless!"));
        }
    }
}
```

### Salida Generada para Minecraft 1.14.4 (Mapeos Intermedios)

Java
```
package net.javacraft.testmod;

public class AccionMod {
    public static void ejecutar(Player jugador, String nombreItem) {
        if (jugador.isOnline()) {
            jugador.getInventory().add(new ItemStack(Items.DIAMOND, 1));
            jugador.sendMessage(new TextComponent("¡Recibiste tu item de forma branchless!"));
        }
    }
}
```

### Salida Generada para Minecraft 1.16.5+ (Estructura de Componentes Moderna)

Java
```
package net.javacraft.testmod;

public class AccionMod {
    public static void ejecutar(Player jugador, String nombreItem) {
        if (jugador.isOnline()) {
            jugador.getInventory().add(new ItemStack(Registry.ITEM.get(new ResourceLocation(nombreItem)), 1));
            jugador.sendMessage(Component.literal("¡Recibiste tu item de forma branchless!"));
        }
    }
}
```

## 🚀 Modo de Uso en Consola (Estilo Lubuntu / Unix Plano)

Para transpilar tu fuente híbrido de forma instantánea, ejecutás en tu terminal:

Bash
```
python3 javacraft.py src/mod.jc build/generated/1.12.2/mod.java src/equ/1.12.2.equ
```

Si querés generar la versión moderna usando el mismo fuente:

Bash
```
python3 javacraft.py src/mod.jc build/generated/1.16.5/mod.java src/equ/1.16.5.equ
```

¡Zero overhead en tiempo de ejecución, compatibilidad absoluta en tiempo de compilación!

## ¡¡ATENCIÓN!!

Necesitamos colaboradores, para completar los .equ, sólo necesitamos que vean el ejemplo del jc.equ, y agregen las versiones, así todos podemos usarlo, y tener nuestros mods favoritos

Gracias por su colaboración
