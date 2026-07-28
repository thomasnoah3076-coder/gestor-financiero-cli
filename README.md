
# gestor-financiero-cli

El proyecto **gestor-financiero-cli** es una herramienta de línea de comandos para administrar finanzas personales de forma local y eficiente.

---

## 🛠️ Guía de Desarrollo y Arquitectura

### ¿Por qué el if / else puede fallar en el método load_transactions?
Aquí se explica la razón por la que el uso de if/else no funciona en la función `load_transactions` del módulo `json_handler`.

El patrón *si no existe -> créalo* suele fallar por dos razones comunes en programación:

1. **El problema de la "condición de carrera":**
Entre el milisegundo en que ejecutas `if ruta.is_dir()` (comprobar) y la siguiente línea donde ejecutas `open()` (escribir), el estado de la carpeta en el sistema operativo puede cambiar o el proceso de ejecución puede perder la sincronía con la caché del disco.

2. **Validar el objeto equivocado:**
Al separar la validación en un `if ruta_data.is_dir()` y luego intentar escribir en `ruta_json`, si `ruta_data` no coincide exactamente con la carpeta padre de `ruta_json`, el `if` te dirá que la carpeta existe, pero `open()` intentará escribir en una ruta diferente que no existe.

---

## 🐍 Módulo `datetime` en Python

El módulo nativo `datetime` permite manipular fechas y horas en Python de forma sencilla. Es fundamental para registrar eventos, calcular plazos o dar formato legible a marcas de tiempo.

### 🚀 Conceptos Clave (Clases)
El módulo se compone principalmente de cuatro clases esenciales:
1. `datetime`: Contiene tanto la fecha como la hora (Año, mes, día, hora, minuto, segundo).
2. `date`: Maneja únicamente el calendario (Año, mes, día).
3. `time`: Maneja únicamente el reloj (Hora, minuto, segundo, microsegundo).
4. `timedelta`: Representa una duración o diferencia de tiempo (Días, semanas, horas).

### 🛠️ Métodos Más Útiles

#### 1. Obtener el tiempo actual
```python
from datetime import datetime, date

# Fecha y hora exacta actual
ahora = datetime.now()  # Ej: 2026-07-26 20:48:15.123456

# Solo la fecha de hoy
hoy = date.today()      # Ej: 2026-07-26
```

#### 2. Conversiones (Texto ⇄ Objeto)
La clave para no confundirlos está en la última letra del método:
*   **`strftime()` (Format):** Convierte un objeto de fecha a un **String** legible.
*   **`strptime()` (Parse):** Analiza un **String** y lo convierte en un objeto de fecha utilizable.

```python
from datetime import datetime

# Objeto ➔ Texto
objeto = datetime.now()
texto = objeto.strftime("%d/%m/%Y")  # "26/07/2026"

# Texto ➔ Objeto
texto_usuario = "15-08-2026"
fecha_objeto = datetime.strptime(texto_usuario, "%d-%m-%Y")
```

#### 3. Operaciones matemáticas con el tiempo (`timedelta`)
Permite sumar o restar días, semanas, horas, minutos o segundos a cualquier fecha.

```python
from datetime import datetime, timedelta

hoy = datetime.now()

# Sumar tiempo (Plazos futuros)
dentro_de_una_semana = hoy + timedelta(weeks=1)
en_tres_horas = hoy + timedelta(hours=3)

# Restar tiempo (Historial)
hace_cinco_dias = hoy - timedelta(days=5)

# Calcular la diferencia entre dos fechas
fecha_inicio = datetime(2026, 7, 1)
fecha_fin = datetime(2026, 7, 26)
diferencia = fecha_fin - fecha_inicio  # Devuelve un objeto timedelta
print(diferencia.days)                 # 25
```

### 📋 Tabla de Códigos de Formato Comunes
Úsalos dentro de `strftime()` y `strptime()` para definir la estructura de tus textos:

| Código | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `%d` | Día del mes con dos dígitos | `01` al `31` |
| `%m` | Mes con dos dígitos | `01` al `12` |
| `%Y` | Año completo con cuatro dígitos | `2026` |
| `%y` | Año resumido con dos dígitos | `26` |
| `%H` | Hora en formato 24 horas | `00` al `23` |
| `%I` | Hora en formato 12 horas | `01` al `12` |
| `%M` | Minutos con dos dígitos | `00` al `59` |
| `%S` | Segundos con dos dígitos | `00` al `59` |
| `%p` | Indicador de mañana o tarde | `AM` o `PM` |

---

## ✍️ Formateo de Cadenas con F-Strings

En este proyecto utilizamos **F-Strings** (Literal String Interpolation) para el manejo y formateo de texto en Python. Es el estándar profesional debido a su legibilidad, velocidad de ejecución y control total sobre la presentación de los datos.

### ⚙️ Sintaxis Básica
Basta con anteponer la letra `f` a las comillas de la cadena e incluir las variables o expresiones entre llaves `{}`:

```python
nombre = "Desarrollador"
print(f"Hola, {nombre}!")  # Resultado: Hola, Desarrollador!
```

### 💵 Formateo de Moneda (Estándar Local)
Dado que Python implementa por defecto la notación anglosajona, aplicamos un formateo nativo y reemplazamos los caracteres para cumplir con la norma de puntos para miles y comas para decimales:

```python
valor = 1234567.89

# Formato final con separadores corregidos
moneda_co = f"${valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(moneda_co)  # Resultado: $1.234.567,89
```

### 🧠 ¿Por qué usamos esta solución en producción?
1. **Independencia del Servidor:** No depende de la configuración regional (`locale`) del sistema operativo donde se despliegue (Docker, AWS, etc.).
2. **Rendimiento:** El formateo ocurre a nivel de bytecode, siendo la opción más rápida en Python.
3. **Mantenibilidad:** El código es explícito, fácil de leer y de auditar.

---

## 📊 Visualización de Datos en Consola con Tabulate

Este proyecto utiliza la librería `tabulate` para formatear diccionarios y listas en tablas de texto limpias y legibles dentro de la terminal.

### ⚙️ Instalación
```bash
pip install tabulate
```

### 🚀 Ejemplo de Uso
```python
from tabulate import tabulate

# Estructura de datos (Diccionario de listas)
inventario = {
    "Producto": ["Laptop", "Mouse", "Teclado"],
    "Precio (\$)": [999.99, 25.50, 45.00],
    "Stock": [12, 50, 30]
}

# Imprimir la tabla con formato de cuadrícula estilizada
print(tabulate(inventario, headers="keys", tablefmt="fancy_grid", floatfmt=".2f"))
```

### 🖥️ Resultado en Terminal

| Producto | Precio ($) | Stock |
| :--- | :---: | :---: |
| Laptop | 999.99 | 12 |
| Mouse | 25.50 | 50 |
| Teclado | 45.00 | 30 |
