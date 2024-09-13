# Calculadora de Subred V1

Esta aplicación es una calculadora de subredes con interfaz gráfica implementada en Python utilizando la biblioteca Tkinter.

# Características

- Calcula subredes basadas en una dirección IP base y un número de usuarios
- Interfaz gráfica de usuario fácil de usar
- Validación de entrada para direcciones IP y número de usuarios
- Muestra información detallada de la subred calculada

# Requisitos

- Python 3.x
- Tkinter (generalmente viene pre-instalado con Python)

# Instalación

1. Clona este repositorio o descarga el archivo Python.
2. Asegúrate de tener Python 3.x instalado en tu sistema.

# Uso

1. Ejecuta el script Python:
   ```
   python subnet_calculator.py
   ```
2. En la interfaz gráfica:
   - Ingresa la dirección IP base en el campo "IP Base"
   - Ingresa el número de usuarios en el campo "Cantidad de Usuarios"
   - Haz clic en el botón "Calcular"

3. Los resultados se mostrarán en el área de texto, incluyendo:
   - Dirección de red
   - Primera IP asignable
   - Última IP asignable
   - Dirección de broadcast
   - Máscara de subred

# Funcionamiento Interno

El programa utiliza las siguientes funciones principales:

- `ip_to_int()`: Convierte una dirección IP en su representación entera.
- `int_to_ip()`: Convierte un entero en una dirección IP.
- `calculate_subnet()`: Realiza los cálculos de subred basados en la IP y el número de usuarios.
- `validate_ip()`: Verifica que la dirección IP ingresada tenga un formato válido.

# Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

