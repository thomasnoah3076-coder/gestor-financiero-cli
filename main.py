import config
from pathlib import Path
from storage.json_handler import load_transactions, save_transactions
from core.validator import validate_amount, validate_date, validate_category

def main ():
    load_transactions(config.RUTA_JSON)
    lista_prueba = [{"amount": 100, "category": "Otros"}]
    save_transactions(config.RUTA_JSON, lista_prueba)
    print(validate_amount("150.50"))  # Debería ser exitoso
    print(validate_amount("-20"))      # Debería fallar
    print(validate_date("2026-07-26")) # Debería ser exitoso
    print(validate_date("26-07-2026")) # Debería fallar


if __name__ == "__main__":
    main()