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

5. Salir''')

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
        for categoria in CATEGORIAS:
            print(f"- {categoria}")
        categoria_valor = input("Categoría: ")
        valido = validate_category(categoria_valor, CATEGORIAS)
        if valido: break
        else: print(" Categoría inválida. Por favor vuelva a ingresar.")

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
        "id": nuevo_id,
        "tipo": tipo_valor.strip().capitalize(),
        "monto": monto_valido.strip(), 
        "categoria": categoria_valor.strip().capitalize(),
        "fecha": fecha_valor.strip(),
        "descripcion": descripcion_valor.strip()
    }

