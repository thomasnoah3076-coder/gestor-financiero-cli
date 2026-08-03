import cli
from config import RUTA_JSON, RUTA_DATA, CATEGORIAS
from pathlib import Path
from storage.json_handler import load_transactions, save_transactions
from core.validator import  validate_category
from core.calculator import calculate_category_totals, calculate_totals
from cli.formatter import format_trasaction_table, print_category_summary, print_summary
from cli.menu import get_transaction_input, display_menu

def main ():
    # Guardamos las transacciones cargadas desde el archivo JSON
    transactions = load_transactions(RUTA_JSON)

    display_menu()

    while True:
        option = input("Ingrese su opción: ")
        match option:
            case "1":
                # Mostrar resumen de finanzas
                    totals = calculate_totals(transactions)
                    print_summary(totals)
                    display_menu()
            case "2":
                # Registrar nueva transacción
                id_actual = 0
                if transactions: id_actual = transactions[-1]["Id"] 
                # Obtiene el numero de ID de la ultima transaccion registrada, si no hay transacciones registradas el id_actual sera 0.
                nueva_transaccion = get_transaction_input(id_actual)
                transactions.append(nueva_transaccion)
                save_transactions(RUTA_JSON, transactions)
                print("-----Transacción registrada exitosamente.-----")
                display_menu()
            case "3":
                # Ver historial de transacciones
                print(format_trasaction_table(transactions))
                display_menu()
            case "4":
                # Filtrar por categoría
                print_category_summary()
                categoria = input("Ingrese la categoría a filtrar: ")
                if validate_category(categoria):
                    trasactions_category = calculate_category_totals(transactions)
                    for key, value in trasactions_category.items():
                        if key.lower() == categoria.lower().strip():
                            print(f"Total de gastos en {key}: {value}")
                    display_menu()
                else:
                    print("Categoría inválida. Por favor, si ingreso una categoría correcta. Verfique su correcta escritura.")
                    display_menu()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Por favor intente nuevamente.")



if __name__ == "__main__":
    main()