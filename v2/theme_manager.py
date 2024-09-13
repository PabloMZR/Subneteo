# theme_manager.py

def apply_dark_mode(root, text_widget, labels, entries):
    """Aplica el tema oscuro a la ventana principal."""
    root.config(bg="black")
    text_widget.config(bg="gray20", fg="white", insertbackground="white")
    for label in labels:
        label.config(bg="black", fg="white")
    for entry in entries:
        entry.config(bg="gray20", fg="white", insertbackground="white")

def apply_light_mode(root, text_widget, labels, entries):
    """Aplica el tema claro a la ventana principal."""
    root.config(bg="white")
    text_widget.config(bg="white", fg="black", insertbackground="black")
    for label in labels:
        label.config(bg="white", fg="black")
    for entry in entries:
        entry.config(bg="white", fg="black", insertbackground="black")
