import json
from pathlib import Path
import config

def load_transactions (ruta_json):
    ruta_json.parent.mkdir(parents=True, exist_ok=True)
    # Se utiliza esta forma de verificar la existencia de la carpeta data por que no va a fallar.
    # Es un codigo idempotente que dice, si no existe alguna de las carpetas padre no existe creala, y si ya la craste no lanzes un error.
    if ruta_json.is_file():
        try:
            print ("El archivo transactions.json existe.")
            with open(ruta_json, "r", encoding="utf-8") as a_lectura:
                return json.load(a_lectura) # Se usa la funcion json.load () para convertir el contenido del json en datos reales (listas/diccionarios) en python. Si se usa la función realines se interpreta como texto plano.
        except json.decoder.JSONDecodeError:
            print("El archivo json esta corrupto o vacio.")
            return []
    else:
        print("El archivo no existe :( No te preocupes vamos a crearlo ahora :)")
        with open(ruta_json, "w", encoding="utf-8") as a_escritura: # El modo w o write tambien sirve para crear un archivo si este no se encuentra
            json.dump([], a_escritura, indent=4, ensure_ascii=False)
        return []

# Verifica si el archivo exite, si existe y tiene contenido lo imprime.
# Si existe y no tiene contenido o esta corrupto lanzara el error json.decoder.JSONDecodeError se capturara y se manejara mostrando un lista vacia.
# Si no existe el archivo lo crea e inicliza con una lista vacia.

def save_transactions (ruta_json, transacciones):
    with open(ruta_json, "w", encoding="utf-8") as a_escritura:
        json.dump(transacciones, a_escritura, indent=4, ensure_ascii=False)

# Gurdara las nueva transacciones que se le envien en sus parametros