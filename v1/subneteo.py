import tkinter as tk
from tkinter import messagebox

def ip_to_int(ip):
    """Convierte una dirección IP en su representación entera."""
    return sum(int(octet) << (8 * i) for i, octet in enumerate(reversed(ip.split('.'))))

def int_to_ip(num):
    """Convierte un entero en una dirección IP."""
    return '.'.join(str((num >> (8 * i)) & 255) for i in reversed(range(4)))

def calculate_subnet(ip_base, num_users):
    """Calcula la subred basada en la IP base y el número de usuarios."""
    try:
        ip_int = ip_to_int(ip_base)
        
        # Calcula el número de bits necesarios para representar los usuarios + 2 (red y broadcast)
        host_bits = (num_users + 2).bit_length()
        subnet_bits = 32 - host_bits
        
        if subnet_bits < 0:
            raise ValueError("La cantidad de usuarios excede el rango posible de direcciones IP.")
        
        # Calcula la máscara de subred
        """
        Este cálculo genera la máscara de subred.
        0xFFFFFFFF es el número hexadecimal que representa 32 bits todos en 1: 11111111 11111111 11111111 11111111.
        El operador << host_bits realiza un desplazamiento hacia la izquierda de los bits de 0xFFFFFFFF por la cantidad de bits destinados a los hosts. Esto esencialmente coloca ceros en las posiciones de los bits de host, creando la máscara de subred.
        Luego, se usa & 0xFFFFFFFF para asegurarse de que el resultado sea de 32 bits, limitando los resultados a los primeros 32 bits.

        Por ejemplo, si host_bits = 8, el desplazamiento sería de 8 bits, lo que dejaría una máscara de subred de 255.255.255.0.
        """
        subnet_mask = (0xFFFFFFFF << host_bits) & 0xFFFFFFFF
        network_address = ip_int & subnet_mask
        broadcast_address = network_address | (0xFFFFFFFF >> subnet_bits)
        
        first_usable = network_address + 1
        last_usable = broadcast_address - 1
        
        return {
            "Red base": int_to_ip(network_address),
            "Primera IP asignable": int_to_ip(first_usable),
            "Última IP asignable": int_to_ip(last_usable),
            "Broadcast": int_to_ip(broadcast_address),
            "Máscara de subred": int_to_ip(subnet_mask)
        }
    except Exception as e:
        raise ValueError(f"Error en el cálculo: {str(e)}")

def validate_ip(ip):
    """Valida que la dirección IP tenga un formato correcto."""
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    return all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)

def show_result():
    """Muestra el resultado del cálculo en la interfaz gráfica."""
    try:
        ip_base = ip_entry.get()
        if not validate_ip(ip_base):
            raise ValueError("Formato de IP inválido.")
        
        num_users = int(users_entry.get())
        if num_users < 1:
            raise ValueError("El número de usuarios debe ser mayor a 0.")
        
        result = calculate_subnet(ip_base, num_users)
        result_text.delete(1.0, tk.END)
        for key, value in result.items():
            result_text.insert(tk.END, f"{key}: {value}\n")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
        result_text.delete(1.0, tk.END)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Subred")

tk.Label(root, text="IP Base:").grid(row=0, column=0, padx=10, pady=5)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Cantidad de Usuarios:").grid(row=1, column=0, padx=10, pady=5)
users_entry = tk.Entry(root)
users_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calcular", command=show_result)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()