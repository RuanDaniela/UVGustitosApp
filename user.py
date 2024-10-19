# Clase User para gestionar la autenticación
class User:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.autenticado = False

    def iniciar_sesion(self, usuario_ingresado, contrasena_ingresada):
        if self.nombre_usuario == usuario_ingresado and self.contrasena == contrasena_ingresada:
            self.autenticado = True
            return True
        else:
            return False