import sys
sys.path.append('..')
from cli.formatter import print_category_summary
from config import CATEGORIAS
from datetime import datetime
from core.validator import validate_amount, validate_category, validate_date, validate_type
def display_menu ():
    print('''
Bienvenido al gestor de finanzas de Thomas Chaparro. Por favor escriba el numero de una de las opciones para continuar.
    
1. Ver resumen de finanzas (Ingresos, Gastos, Saldo).

2. Registrar nueva transacción (Ingreso/Gasto).

3. Ver historial de transacciones.

4. Filtrar por categoría.

5. Salir del programa.\n''')

from datetime import datetime

# Nota: Asegúrate de tener tus funciones de validación (validate_type, etc.) 
# y la lista CATEGORIAS definidas arriba en tu archivo.

def get_transaction_input(id_actual):
    # Incrementamos el ID que recibimos por argumento
    print("\n--- Registrar Nueva Transacción ---")

    nuevo_id = id_actual + 1
    
    while True:
        tipo_valor = input("Ingrese el tipo de transacción (Gasto/Ingreso): ")
        valido = validate_type(tipo_valor)
        if valido: break
        else: print(" Tipo de transacción inválida. Por favor vuelva a ingresar.")

    while True:
        monto_valor = input("Ingrese el monto de la transacción: ")
        valido, monto_valido = validate_amount(monto_valor)
        if valido: break
        else: print(" Monto inválido. Por favor vuelva a ingresar.")

    while True:
        print("\nIngrese una de las categorías válidas:")
        print_category_summary()
        categoria_valor = input("Categoría: ")
        valido = validate_category(categoria_valor)
        if valido: break
        else: print(" Categoría inválida. Por favor, si ingreso una categoría correcta, verfique su correcta escritura.")

    while True:
        fecha_valor = input("Ingrese la fecha de la transacción (YYYY-MM-DD) o Enter para hoy: ")
        if not fecha_valor.strip():
            fecha_valor = datetime.today().strftime("%Y-%m-%d")
        valido = validate_date(fecha_valor)
        if valido: break
        else:print(" Formato de fecha inválido. Por favor vuelva a ingresar.")

    descripcion_valor = input("Escriba una pequeña descripción por favor: ")

    # Limpiamos los textos con .strip() y formateamos montos/letras
    return {
        "Id": nuevo_id,
        "Tipo": tipo_valor.strip().capitalize(),
        "Monto": monto_valido, 
        "Categoría": categoria_valor.strip().capitalize(),
        "Fecha": fecha_valor.strip(),
        "Descripción": descripcion_valor.strip()
    }

