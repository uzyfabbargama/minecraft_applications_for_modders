# Bienvenidos al source, aquí se explica que hay en cada carpeta

## equ
  Acá están las diferentes equivalencias, lo colocas para cada versión
  **ejemplo:**
    SEND_MSG(usr, text) :: usr.sendMessage(new ChatComponentText(text))
    Javacraft code :: java original code with args
  **Lo que no hay que hacer**
    SEND_MSG12(usr, text) :: (minecraft java 1.12.2 code)
    Para eso tienes que crear un nuevo .equ, y poner todas las equivalencias de 1.12.2, sin romper la sintaxis de javacraft

## motor
  Acá está el código en Python que se encarga de hacer funcionar todo lo del transpilado, no usa funciones, usa macros, para acelerar el rendimiento, y permitir que cualquier programador de bajos recursos pueda integrarse al equipo.

## examples
  Acá hay un código de ejemplo, que le da diamantes y envía un mensaje al jugador


## uso

  bash
  ```
  python3 javacraft.py <origen> <destino> <equivalencia> #aquí en equivalencia, se pondrían las versiones
  ## Uso del ejemplo

  #1. Transpila el código:
  python3 ./motor/javacraft.py tu-mod.jc tu-mod_1.12.2.java ./equ/1.12.2.equ
  ```
  2. Compila el Java generado con tu IDE o Gradle.
  3. ¡Ejecuta en Minecraft y recibe tu diamante!
