import config
from pathlib import Path
from storage.json_handler import load_transactions, save_transactions
from core.validator import validate_amount, validate_date, validate_category
from core.calculator import calculate_category_totals, calculate_totals

def main ():
    load_transactions(config.RUTA_JSON)
    lista_prueba = [{"amount": 100, "category": "Otros"}]
    save_transactions(config.RUTA_JSON, lista_prueba)
    print(validate_amount("150.50"))  # Debería ser exitoso
    print(validate_amount("-20"))      # Debería fallar
    print(validate_date("2026-07-26")) # Debería ser exitoso
    print(validate_date("26-07-2026")) # Debería fallar
    test_data = [
    {"Monto:": 1000, "Tipo:": "ingreso", "Categoria:": "Salario"},
    {"Monto:": 50, "Tipo:": "gasto", "Categoria:": "Alimentación"},
    {"Monto:": 30, "Tipo:": "gasto", "Categoria:": "Alimentación"},
    {"Monto:": 20, "Tipo:": "gasto", "Categoria:": "Transporte"},
    ]
    print(calculate_totals(test_data))

    print(calculate_category_totals(test_data))

if __name__ == "__main__":
    main()