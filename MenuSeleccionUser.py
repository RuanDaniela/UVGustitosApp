import tkinter as tk
from tkinter import messagebox

class MenuSeleccion:
    def __init__(self, root):
        self.root = root
        self.pedido = []  # Lista para almacenar los alimentos seleccionados

        # Título del menú
        tk.Label(root, text="Escoge lo que deseas ordenar:", font=("Arial", 16)).pack(pady=10)

        # Lista de alimentos con sus precios
        self.alimentos = {
            "Pizza": 50,
            "Hamburguesa": 30,
            "Ensalada": 25,
            "Pasta": 40,
            "Refresco": 10
        }

        # Crear botones para cada alimento
        for alimento, precio in self.alimentos.items():
            button = tk.Button(root, text=f"{alimento} - Q{precio}", font=("Arial", 12),
                               command=lambda a=alimento: self.agregar_al_pedido(a))
            button.pack(pady=5)

        # Botón para confirmar pedido
        confirmar_btn = tk.Button(root, text="Confirmar Pedido", font=("Arial", 14),
                                  command=self.confirmar_pedido)
        confirmar_btn.pack(pady=20)

    def agregar_al_pedido(self, alimento):
        """Añade el alimento seleccionado al pedido"""
        self.pedido.append(alimento)
        messagebox.showinfo("Pedido Actualizado", f"Has añadido {alimento} a tu pedido.")

    def confirmar_pedido(self):
        """Muestra el pedido completo del usuario"""
        if not self.pedido:
            messagebox.showwarning("Pedido vacío", "No has seleccionado ningún alimento.")
        else:
            pedido_texto = "\n".join(self.pedido)
            messagebox.showinfo("Tu Pedido", f"Has ordenado:\n{pedido_texto}")
            # Aquí puedes proceder con el siguiente paso del pedido, como el pago

