from tabulate import tabulate
from config import CATEGORIAS

def format_currency (amount):
    monto_EEUU = f"{amount:,.2f}"
    # Se transforma el monto que es un float a un string y se le da formato en moneda estado unidense con el uso de un f-string.
    # La letra f antes de las comillas le indica a Python que dentro de las comillas debe buscar {} y pegar su contenido.
    # La coma , añade separador de miles, el .2 define dos decimales, y la f al final indica que es un número flotante.
    monto_co = monto_EEUU.replace(",","X").replace(".",",").replace("X",".")
    # Se reemplaza las comas por un caracter intermedio. 1X234X567.89
    # Reemplazamos el punto de decimales por una coma. 1X234X567,89
    # Y finalmente se reemplaza el caracter intermedio, por los puntos. 1.234.567,89
    return monto_co

def format_trasaction_table (transactions):
    return tabulate(transactions, headers="keys", tablefmt="fancy_grid")
    # Se debe instalar la librería tabulate para que este método funcione correctamente, se logra con el comando pip install tabulate

def print_summary (totals):
    summary =""
    for clave, valor in totals.items():
        summary += f"{clave}"+f" {format_currency(valor)}\n"
    return print(summary)

def print_category_summary ():
    for categoria in CATEGORIAS:
        print(f"- {categoria}.")