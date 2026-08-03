# 💰 Gestor Financiero CLI

Herramienta de línea de comandos escrita en **Python** para administrar finanzas personales de forma local: registra ingresos y gastos, consulta resúmenes y filtra por categoría, todo guardado en un archivo JSON en tu propio equipo.

> Repositorio de práctica orientado a reforzar buenas prácticas de Python (manejo de archivos, validaciones, formateo de datos y estructura modular).

---

## 📋 Tabla de contenidos

- [Características](#-características)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Categorías disponibles](#-categorías-disponibles)
- [Almacenamiento de datos](#-almacenamiento-de-datos)
- [Notas técnicas de desarrollo](#-notas-técnicas-de-desarrollo)
- [Autor](#-autor)

---

## ✨ Características

- **Resumen financiero:** total de ingresos, total de gastos y balance neto.
- **Registro de transacciones:** ingresos o gastos con monto, categoría, fecha y descripción.
- **Historial de transacciones** en formato de tabla legible (usando `tabulate`).
- **Filtrado por categoría** para ver cuánto se ha gastado en cada rubro.
- **Persistencia local** en un archivo `transactions.json`, sin necesidad de bases de datos externas.
- **Validaciones de entrada** para tipo de transacción, monto, categoría y fecha.

---

## 🗂 Estructura del proyecto

```
gestor-financiero-cli/
├── main.py                  # Punto de entrada: menú principal y flujo del programa
├── config.py                # Rutas de datos, categorías y tipos de transacción válidos
├── cli/
│   ├── menu.py               # Muestra el menú y captura los datos de una transacción
│   └── formatter.py          # Formatea moneda, tablas y resúmenes en consola
├── core/
│   ├── calculator.py         # Cálculo de totales generales y por categoría
│   └── validator.py          # Validación de tipo, monto, categoría y fecha
├── storage/
│   └── json_handler.py       # Carga y guardado de transacciones en JSON
└── data/
    └── transactions.json     # Archivo donde se guardan las transacciones (se crea automáticamente)
```

---

## ✅ Requisitos

- Python 3.10 o superior (usa `match/case`, disponible desde Python 3.10).
- Librería [`tabulate`](https://pypi.org/project/tabulate/).

---

## ⚙️ Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/thomasnoah3076-coder/gestor-financiero-cli.git
cd gestor-financiero-cli

# 2. (Opcional) crea un entorno virtual
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate

# 3. Instala las dependencias
pip install tabulate
```

---

## ▶️ Uso

Ejecuta el programa desde la raíz del proyecto:

```bash
python main.py
```

Al iniciar verás un menú con las siguientes opciones:

```
1. Ver resumen de finanzas (Ingresos, Gastos, Saldo).
2. Registrar nueva transacción (Ingreso/Gasto).
3. Ver historial de transacciones.
4. Filtrar por categoría.
5. Salir del programa.
```

- **Opción 1:** muestra el total de ingresos, total de gastos y el balance neto.
- **Opción 2:** solicita tipo (Ingreso/Gasto), monto, categoría, fecha (`YYYY-MM-DD`, o Enter para usar la fecha de hoy) y una descripción breve.
- **Opción 3:** imprime el historial completo en una tabla con formato `fancy_grid`.
- **Opción 4:** pide una categoría y muestra el total gastado/ingresado en ella.
- **Opción 5:** guarda y cierra el programa.

---

## 🏷 Categorías disponibles

```
Alimentación · Transporte · Servicios · Entretenimiento · Salario · Salud · Regalos · Otros
```

---

## 💾 Almacenamiento de datos

Las transacciones se guardan en `data/transactions.json`. Si el archivo o la carpeta `data/` no existen, el programa los crea automáticamente en el primer arranque (patrón "verificar y crear" de forma idempotente, ver notas técnicas más abajo).

---

## 🧠 Notas técnicas de desarrollo

Resumen de las lecciones y decisiones de diseño registradas durante la construcción del proyecto (versión sintetizada del README original).

<details>
<summary><strong>¿Por qué el patrón "si no existe → créalo" puede fallar con if/else?</strong></summary>

Separar la verificación (`if ruta.is_dir()`) de la acción (`open()`) es riesgoso por dos motivos:

1. **Condición de carrera:** el estado del sistema de archivos puede cambiar entre el momento en que se verifica y el momento en que se escribe.
2. **Validar el objeto equivocado:** si la carpeta que se valida no es exactamente la carpeta padre del archivo que se va a crear, el `if` puede dar un falso positivo.

Por eso `load_transactions` usa `ruta_json.parent.mkdir(parents=True, exist_ok=True)`, una operación idempotente que crea la carpeta solo si hace falta, sin lanzar error si ya existe.
</details>

<details>
<summary><strong>Manejo de fechas con <code>datetime</code></strong></summary>

El módulo `datetime` se usa para registrar y validar fechas. Claves:

- `datetime.now()` / `date.today()` para obtener el momento actual.
- `strftime()` convierte un objeto de fecha a texto; `strptime()` convierte texto a un objeto de fecha (útil para validar el formato `YYYY-MM-DD` ingresado por el usuario).
- `timedelta` permite sumar/restar días, semanas u horas, y calcular diferencias entre fechas.

| Código | Significado          | Ejemplo |
|--------|-----------------------|---------|
| `%d`   | Día (2 dígitos)       | `01`–`31` |
| `%m`   | Mes (2 dígitos)       | `01`–`12` |
| `%Y`   | Año (4 dígitos)       | `2026` |
| `%H`   | Hora (24h)            | `00`–`23` |
| `%M`   | Minutos               | `00`–`59` |
| `%S`   | Segundos              | `00`–`59` |
</details>

<details>
<summary><strong>Formateo de moneda con f-strings</strong></summary>

El proyecto usa **f-strings** por legibilidad y rendimiento. Como Python formatea números en notación anglosajona, se reemplazan los separadores para obtener el formato local (punto de miles, coma decimal):

```python
valor = 1234567.89
moneda_co = f"${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
# Resultado: $1.234.567,89
```

Esta solución no depende de la configuración regional (`locale`) del sistema donde se ejecute, es rápida y fácil de auditar.
</details>

<details>
<summary><strong>Tablas en consola con <code>tabulate</code></strong></summary>

```bash
pip install tabulate
```

```python
from tabulate import tabulate

inventario = {
    "Producto": ["Laptop", "Mouse", "Teclado"],
    "Precio ($)": [999.99, 25.50, 45.00],
    "Stock": [12, 50, 30]
}

print(tabulate(inventario, headers="keys", tablefmt="fancy_grid", floatfmt=".2f"))
```

`tabulate` es la librería usada por `cli/formatter.py` para mostrar el historial de transacciones como tabla.
</details>

---

## 👤 Autor

Proyecto de práctica desarrollado por **Thomas Chaparro** ([@thomasnoah3076-coder](https://github.com/thomasnoah3076-coder)). Agradecimientos a **Santiago Duarte** por los consejos https://github.com/Santiago-Duarte.
