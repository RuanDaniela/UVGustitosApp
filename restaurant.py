# Clase Restaurant para gestionar restaurantes y menús
class Restaurant:
    def __init__(self, nombre_restaurante):
        self.nombre_restaurante = nombre_restaurante
        self.menu = []

    def agregar_item_menu(self, item):
        self.menu.append(item)

    def obtener_menu(self):
        return self.menu
