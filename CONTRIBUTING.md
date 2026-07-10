# Cómo Contribuir a Javacraft

## ¿Qué necesitamos?
- **Equivalencias para nuevas versiones**: 1.14.4, 1.15.2, 1.16.5, 1.18.2, 1.19.4, 1.20.4, Fabric, NeoForge.
- **Pruebas**: Verificar que las equivalencias funcionan.
- **Documentación**: Mejorar ejemplos y guías.

## ¿Cómo empezar?
1. Forkea el repositorio.
2. Crea un archivo `.equ` para la versión que quieras en `src/equ/`.
3. Copia las macros existentes y adapta la sintaxis Java.
4. Prueba con `javacraft.py` y un `.jc` de prueba.
5. Haz un Pull Request.

## Reglas importantes
- **Nombres de archivos**: `forge-1.12.2.equ`, `fabric-1.20.4.equ`, etc.
- **No rompas la sintaxis**: Si una macro funciona, no la cambies; agrega nuevas si es necesario.
- **Documenta**: Explica qué cambia entre versiones si es necesario.

¡Gracias por ayudar a hacer el modding más portable!
