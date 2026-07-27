from datetime import datetime
# Es importante destacar que la "doble importación" en realidad no es lo que aparenta, sino que es un por su modulo y otra por la función 

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

def validate_category (category_str, valid_categories):
    for category in valid_categories:
        if category.lower() == category_str.lower().strip():
            return True
        else:
            print("La categoría que se busco no sé encuentra disponible. Verifique por favor.")
            return False
# Válida la categoría de la transacción.

def validate_date (date_str):
    try:
        fecha = datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        print ("Formato de la fecha incorrecto.")
        return False
#  Válida la fecha de la transacción.

