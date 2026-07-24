# gestor-financiero-cli
Esto es un borrador de la razón por la que el uso de if/else no funciona en la función load_transactions del modulo json_handler.
## ❌ ¿Por qué el if / else puede fallar?
El patrón if no existe -> créalo suele fallar por dos razones comunes en programación:

1. El problema de la "condición de carrera" (Race Condition)
Entre el milisegundo en que ejecutas if ruta.is_dir() (comprobar) y la siguiente línea donde ejecutas open() (escribir), el estado de la carpeta en el sistema operativo puede cambiar o el proceso de ejecución puede perder la sincronía con la caché del disco.

2. Validar el objeto equivocado
Al separar la validación en un if ruta_data.is_dir() y luego intentar escribir en ruta_json, si ruta_data no coincide exactamente con la carpeta padre de ruta_json, el if te dirá que la carpeta existe, pero open() intentará escribir en una ruta diferente que no existe.