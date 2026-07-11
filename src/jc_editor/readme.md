### 📦 **Instalación (1 minuto)**

```bash
git clone https://github.com/uzyfabbargama/minecraft_applications_for_modders
cd minecraft_applications_for_modders
python3 jcn_IDE.py
```

**No necesitas nada más.** Solo Python 3 y el archivo `.equ` generado.

---

## 🔥 **¿CÓMO FUNCIONA EN LA PRÁCTICA?**

*(Imagina la escena)*

Estás en tu computadora, escribiendo un mod en Nano. No recuerdas cómo se llama la macro para compresión de red.

**Escribes en tu terminal:**

```bash
python3 jcn_IDE.py
Buscar macro >>> net compression
```

**Y el script te devuelve:**
```
MC_GETNETWORKCOMPRESSIONTHRESHOLD_FIELD(usr) -> usr.aG
```

*(Aprieta el puño)*

**Eso es magia.**

---
### 🧪 **Ejemplo de Uso Real**

```bash
$ python3 jcn_IDE.py
=== JAVACRAFT LEXICON DICTIONARY ===
Buscar macro >>> player health
MC_GETHEALTH_FIELD(usr) -> usr.cd
MC_SETHEALTH_FIELD(usr, val) -> usr.setHealth(val)
```

**Ahora puedes usar esa macro en tu `.jc` sin buscar en miles de líneas.**

---

## 💀 **LA PREGUNTA QUE ME HACE TIC**

*(Inclino la cabeza)*

**¿Es posible integrar esto con Nano o Vim?**

Porque si se hace un plugin que:
1. Detecta cuando escribes una macro incompleta.
2. La busca en el diccionario (.equ).
3. La autocompleta en tiempo real.

**Tendríamos un autocompletado más rápido y ligero que cualquier IDE.**

---
### 🤝 **Contribuir (La Parte Más Importante)**

**Si quieres ayudar, necesitamos:**

1. **Más versiones.** Genera el `.equ` para 1.14.4, 1.16.5, 1.20.4...
2. **Pruebas.** Verifica que las macros funcionan en juegos reales.
3. **Plugins.** ¿Alguien se anima a un plugin para Nano/Vim?

**El proceso es simple:**

1. Forkea el repo.
2. Ejecuta `build_equ.py` para tu versión.
3. Prueba con un mod simple.
4. Haz un Pull Request.

**No necesitas ser un experto. Solo necesitas curiosidad.**

---

## 🗿 **MI VEREDICTO**


**Ecosistema completo:**

1. **Javacraft** → transpila.
2. **Desofuscador** → entiende a Mojang.
3. **Fuzzy Finder** → te ayuda a recordar.

**Y todo en menos de 1 MB.**

**Ahora dime: ¿vamos a probar usarlo con el `.equ` de 1.16.5?**

Porque si funciona con todas las versiones... **tenemos un asistente de modding universal.**
