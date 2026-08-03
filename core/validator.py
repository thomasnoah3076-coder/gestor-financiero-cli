from datetime import datetime, date
from config import CATEGORIAS
# Es importante destacar que la "doble importación" en realidad no es lo que aparenta, sino que es un por su modulo y otra por la función 
def validate_type(type_transaction):
    if type_transaction.lower().strip() == "ingreso":
        return True
    elif type_transaction.lower().strip() == "gasto":
        return True
    else:
        return False

def validate_amount (amount_str):
        try:
            amount_float = float(amount_str)
            if amount_float > 0:
                return True, amount_float
            else:
                return False, None
        except ValueError:
            print("El dato no es correcto. Por favor ingrese un número válido.")
            return False, None
# Válida el monto de la transacción.

def validate_category (category_str):
    for category in CATEGORIAS:
        if category.lower() == category_str.lower().strip():
            return True
    return False
# Válida la categoría de la transacción.

def validate_date (date_str):
    try:
        datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return True
    except ValueError:
        print ("Formato de la fecha incorrecto.")
        return False
#  Válida la fecha de la transacción.

