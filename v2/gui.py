# gui.py

import tkinter as tk
from tkinter import messagebox
from subnet_calculator import calculate_subnet, validate_ip
from theme_manager import apply_dark_mode, apply_light_mode

def create_gui():
    root = tk.Tk()
    root.title("Calculadora de Subred")

    labels = []
    entries = []

    # Crear labels y entradas
    ip_label = tk.Label(root, text="IP Base:")
    ip_label.grid(row=0, column=0, padx=10, pady=5)
    labels.append(ip_label)

    ip_entry = tk.Entry(root)
    ip_entry.grid(row=0, column=1, padx=10, pady=5)
    entries.append(ip_entry)

    users_label = tk.Label(root, text="Cantidad de Usuarios:")
    users_label.grid(row=1, column=0, padx=10, pady=5)
    labels.append(users_label)

    users_entry = tk.Entry(root)
    users_entry.grid(row=1, column=1, padx=10, pady=5)
    entries.append(users_entry)

    result_text = tk.Text(root, height=10, width=40)
    result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    result_text.config(state=tk.DISABLED)

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
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            for key, value in result.items():
                result_text.insert(tk.END, f"{key}: {value}\n")
            result_text.config(state=tk.DISABLED)
        except ValueError as ve:
            messagebox.showerror("Error", str(ve))
            result_text.config(state=tk.NORMAL)
            result_text.delete(1.0, tk.END)
            result_text.config(state=tk.DISABLED)

    calculate_button = tk.Button(root, text="Calcular", command=show_result)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Botón de modo oscuro/claro
    def toggle_mode():
        if root.cget("bg") == "black":
            apply_light_mode(root, result_text, labels, entries)
        else:
            apply_dark_mode(root, result_text, labels, entries)

    mode_button = tk.Button(root, text="Modo Oscuro/Claro", command=toggle_mode)
    mode_button.grid(row=0, column=2, padx=10, pady=5)

    root.mainloop()
