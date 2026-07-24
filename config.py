# Se define la ruta del archivo json

from pathlib import Path

RUTA_DATA = Path(__file__).resolve().parent

# Path(__file__) Trae la ruta del archivo donde esta posicionada la función.
# .resolve() es un funcion que transforma cualquier ruta relativa en absoluta.
# .parente sube una carpeta, es decir, se va a obtener al ruta de la carpeta contenedora.

RUTA_JSON =RUTA_DATA / "data" / "transactions.json"

# Se definen las categorias de transacción disponibles

CATEGORIAS = {"Alimentación", "Transporte", "Servicios", "Entretenimiento", "Salario", "Otros", "Salud", "Regalos"}

# Se definem los tipos de transacción válidos

TIPOS_TRANSACCION = {"Ingreso","Gasto"}

