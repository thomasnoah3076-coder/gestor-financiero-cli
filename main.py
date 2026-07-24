import config
from pathlib import Path
from storage.json_handler import load_transactions, save_transactions

def main ():
    load_transactions(config.RUTA_JSON)
    lista_prueba = [{"amount": 100, "category": "Otros"}]
    save_transactions(config.RUTA_JSON, lista_prueba)


if __name__ == "__main__":
    main()