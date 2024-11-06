# Clase Restaurant para gestionar restaurantes y menús
class Restaurant:
    def __init__(self, nombre, tiempo_entrega, pedidos):
        self.nombre = nombre
        self.tiempo_entrega = tiempo_entrega
        self.pedidos = pedidos

    def agregar_item_menu(self, item):
        self.menu.append(item)

    def obtener_menu(self):
        return self.menu
