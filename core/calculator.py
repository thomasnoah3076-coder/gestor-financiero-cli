
def calculate_totals (transactions):
    total_ingresos = 0
    total_gastos = 0 
    for transaction in transactions:
        if transaction["Tipo:"] == "ingreso":
            total_ingresos += transaction["Monto:"]
        elif transaction["Tipo:"] == "gasto":
            total_gastos += transaction["Monto:"]
        else:
            print("El tipo de transacción no es válido. Por favor verifique.")
    saldo_neto ={
        "Total de ingresos:":total_ingresos,
        "Total de gastos:":total_gastos,
        "Balance:": total_ingresos - total_gastos
    }
    return saldo_neto

def calculate_category_totals (transactions):
    alimentacion_total = 0
    transporte_total = 0
    servicios_total = 0
    entretenimiento_total = 0
    salud_total = 0 
    regalos_total = 0
    otros_total = 0
    for transaction in transactions:
        if transaction["Tipo:"] == "gasto":
            match transaction["Categoria:"].strip():
                case "Alimentación":
                    alimentacion_total += transaction["Monto:"]
                case "Transporte":
                    transporte_total += transaction["Monto:"]
                case "Servicios":
                    servicios_total += transaction["Monto:"]
                case "Entretenimiento":
                    entretenimiento_total += transaction["Monto:"]
                case "Salud":
                    salud_total += transaction["Monto:"]
                case "Regalos":
                    regalos_total += transaction["Monto:"]
                case "Otros":
                    otros_total += transaction["Monto:"]
                case _:
                    otros_total += transaction["Monto:"]
    gastos_categorias = {
        "Alimentación":alimentacion_total, 
        "Transporte": transporte_total,
        "Servicios": servicios_total,
        "Entretenimiento": entretenimiento_total, 
        "Salud": salud_total, 
        "Regalos" : regalos_total,
        "Otros" : otros_total
    }
    return gastos_categorias