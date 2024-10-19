# Clase MenuItem para representar los elementos del menú
class MenuItem:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Q{self.precio}"
