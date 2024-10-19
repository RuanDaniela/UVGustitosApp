import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from user import User
from menu_item import MenuItem
from restaurant import Restaurant

# Clase principal UVGustitosApp para la aplicación con Tkinter
class UVGustitosApp:
    def __init__(self, root):
        self.root = root  # Ventana principal (root) de Tkinter
        self.root.title("UVGustitos - Selección de Rol")  # Título de la ventana
        self.root.geometry("900x700")  # Tamaño de la ventana

        # Fondo verde para toda la app
        self.root.configure(bg="#87A96B")  # Color de fondo verde

        # Crear los usuarios para la autenticación (Restaurantes y Consumidor)
        self.consumidor = User("consumidor1", "pass123")  # Usuario de prueba para el consumidor

        # Usuarios para cada restaurante con sus credenciales
        self.restaurante_usuarios = {
            "Panitos": User("panitos_user", "panitos_pass"),
            "Mixtas Frankfurt": User("mixtas_user", "mixtas_pass"),
            "Café Barista": User("barista_user", "barista_pass")
        }

        # Lista de pedidos ficticios para cada restaurante
        self.pedidos_restaurantes = {
            "Panitos": ["Pedido 1: Pan de Roast Beef, Pan de Pollo", "Pedido 2: Pan de Carne Adobada", "Pedido 3: Pan de Roast Beef"],
            "Mixtas Frankfurt": ["Pedido 1: Mixtas de Salchicha", "Pedido 2: Nachos con Queso y Carne Asada", "Pedido 3: Shuko de Salchicha"],
            "Café Barista": ["Pedido 1: Panini Bungiorno", "Pedido 2: Baguette de Ensalada de Pollo", "Pedido 3: Panini de Pollo y Pesto"]
        }

        # Tiempos de entrega para cada restaurante
        self.tiempos_entrega = {
            "Panitos": 15,  # 15 minutos para Panitos
            "Mixtas Frankfurt": 25,  # 25 minutos para Mixtas Frankfurt
            "Café Barista": 30  # 30 minutos para Café Barista
        }

        # Imágenes para los logos de los restaurantes
        self.imagenes_restaurantes = {
            "Panitos": "panitos.png",  # Imagen de Panitos
            "Mixtas Frankfurt": "mixtas.png",  # Imagen de Mixtas Frankfurt
            "Café Barista": "barista.png"  # Imagen de Café Barista
        }

        # Imágenes para los menús de cada restaurante
        self.imagenes_menus = {
            "Panitos": "panitos2.png",  # Imagen del menú de Panitos
            "Mixtas Frankfurt": "mixtas2.png",  # Imagen del menú de Mixtas Frankfurt
            "Café Barista": "barista2.png"  # Imagen del menú de Café Barista
        }

        # Imagen del logo de la aplicación
        self.logo_path = "logo1.png"  # Ruta de la imagen del logo de la aplicación

        # Lista donde se guardarán los objetos restaurante
        self.restaurantes = []
        self.inicializar_restaurantes()  # Llamar al método que inicializa los restaurantes

        # Crear la interfaz gráfica de selección de rol (consumidor o restaurante)
        self.crear_pantalla_seleccion_rol()

    # Método para ocultar todos los frames cuando se cambia de pantalla
    def ocultar_frames(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()  # Ocultar todos los elementos de la ventana actual

    # Pantalla de selección de rol (Consumidor o Restaurante)
    def crear_pantalla_seleccion_rol(self):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un nuevo frame para la selección de rol
        self.frame_seleccion = tk.Frame(self.root, bg="#87A96B")
        self.frame_seleccion.pack(pady=20)  # Empaquetar el frame con padding de 20

        # Cargar y mostrar el logo en la pantalla de selección
        logo_img = Image.open(self.logo_path)  # Abrir la imagen del logo
        logo_img = logo_img.resize((150, 150), Image.LANCZOS)  # Redimensionar la imagen
        logo_photo = ImageTk.PhotoImage(logo_img)  # Convertir la imagen en un formato que Tkinter pueda usar
        tk.Label(self.frame_seleccion, image=logo_photo, bg="#87A96B").pack(pady=10)  # Mostrar el logo
        self.frame_seleccion.logo = logo_photo  # Mantener una referencia para evitar que se borre la imagen

        # Etiqueta de título
        tk.Label(self.frame_seleccion, text="¿Quién eres?", font=("Arial", 22, "bold"), bg="#87A96B").pack(pady=20)

        # Botones para seleccionar si es consumidor o restaurante
        tk.Button(self.frame_seleccion, text="Soy un Consumidor", command=self.crear_pantalla_login_consumidor, bg="#6C8EAD", fg="white", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.frame_seleccion, text="Soy un Restaurante", command=self.crear_pantalla_login_restaurante, bg="#6C8EAD", fg="white", font=("Arial", 16)).pack(pady=10)

    # Pantalla de inicio de sesión para consumidores
    def crear_pantalla_login_consumidor(self):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un nuevo frame para el inicio de sesión del consumidor
        self.frame_login_consumidor = tk.Frame(self.root, bg="#87A96B")
        self.frame_login_consumidor.pack(pady=20)

        # Cargar y mostrar el logo en la pantalla de inicio de sesión
        logo_img = Image.open(self.logo_path)
        logo_img = logo_img.resize((150, 150), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        tk.Label(self.frame_login_consumidor, image=logo_photo, bg="#87A96B").pack(pady=10)
        self.frame_login_consumidor.logo = logo_photo

        # Etiqueta para indicar inicio de sesión
        tk.Label(self.frame_login_consumidor, text="Inicio de sesión - Consumidor", font=("Arial", 18), bg="#87A96B").pack(pady=10)

        # Campo de entrada para el nombre de usuario
        tk.Label(self.frame_login_consumidor, text="Nombre de usuario:", bg="#87A96B").pack()
        self.entry_usuario_consumidor = tk.Entry(self.frame_login_consumidor, width=30)
        self.entry_usuario_consumidor.pack(pady=5)

        # Campo de entrada para la contraseña
        tk.Label(self.frame_login_consumidor, text="Contraseña:", bg="#87A96B").pack()
        self.entry_contrasena_consumidor = tk.Entry(self.frame_login_consumidor, show="*", width=30)
        self.entry_contrasena_consumidor.pack(pady=5)

        # Botón para iniciar sesión
        tk.Button(self.frame_login_consumidor, text="Iniciar Sesión", command=self.iniciar_sesion_consumidor, bg="#6C8EAD", fg="white").pack(pady=10)

    # Pantalla de inicio de sesión para restaurantes
    def crear_pantalla_login_restaurante(self):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un nuevo frame para el inicio de sesión del restaurante
        self.frame_login_restaurante = tk.Frame(self.root, bg="#87A96B")
        self.frame_login_restaurante.pack(pady=20)

        # Cargar y mostrar el logo en la pantalla de inicio de sesión
        logo_img = Image.open(self.logo_path)
        logo_img = logo_img.resize((150, 150), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        tk.Label(self.frame_login_restaurante, image=logo_photo, bg="#87A96B").pack(pady=10)
        self.frame_login_restaurante.logo = logo_photo

        # Etiqueta para indicar inicio de sesión
        tk.Label(self.frame_login_restaurante, text="Inicio de sesión - Restaurante", font=("Arial", 18), bg="#87A96B").pack(pady=10)

        # Campo de entrada para el nombre de usuario del restaurante
        tk.Label(self.frame_login_restaurante, text="Nombre de usuario:", bg="#87A96B").pack()
        self.entry_usuario_restaurante = tk.Entry(self.frame_login_restaurante, width=30)
        self.entry_usuario_restaurante.pack(pady=5)

        # Campo de entrada para la contraseña del restaurante
        tk.Label(self.frame_login_restaurante, text="Contraseña:", bg="#87A96B").pack()
        self.entry_contrasena_restaurante = tk.Entry(self.frame_login_restaurante, show="*", width=30)
        self.entry_contrasena_restaurante.pack(pady=5)

        # Botón para iniciar sesión
        tk.Button(self.frame_login_restaurante, text="Iniciar Sesión", command=self.iniciar_sesion_restaurante, bg="#6C8EAD", fg="white").pack(pady=10)

    # Método para manejar el inicio de sesión como consumidor
    def iniciar_sesion_consumidor(self):
        # Obtener el nombre de usuario y la contraseña ingresados
        nombre_usuario = self.entry_usuario_consumidor.get()
        contrasena = self.entry_contrasena_consumidor.get()

        # Verificar si las credenciales son correctas
        if self.consumidor.iniciar_sesion(nombre_usuario, contrasena):
            messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso como Consumidor")
            self.mostrar_pantalla_restaurantes_consumidor()  # Mostrar la pantalla de selección de restaurantes
        else:
            messagebox.showerror("Error", "Credenciales incorrectas para Consumidor")  # Mostrar error si las credenciales no son correctas

    # Método para manejar el inicio de sesión como restaurante
    def iniciar_sesion_restaurante(self):
        nombre_usuario = self.entry_usuario_restaurante.get()  # Obtener el nombre de usuario
        contrasena = self.entry_contrasena_restaurante.get()  # Obtener la contraseña

        # Validar si las credenciales son correctas para el restaurante
        for restaurante, usuario in self.restaurante_usuarios.items():
            if usuario.iniciar_sesion(nombre_usuario, contrasena):
                messagebox.showinfo("Inicio de sesión", f"Inicio de sesión exitoso como {restaurante}")
                self.mostrar_pedidos_restaurante(restaurante)  # Mostrar los pedidos del restaurante
                return

        messagebox.showerror("Error", "Credenciales incorrectas para Restaurante")  # Mostrar error si las credenciales no son correctas

    # Método para mostrar los pedidos hechos a un restaurante
    def mostrar_pedidos_restaurante(self, restaurante):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un frame para mostrar los pedidos
        self.frame_pedidos = tk.Frame(self.root, bg="#87A96B")
        self.frame_pedidos.pack(pady=20)

        # Mostrar el logo del restaurante
        img_path = self.imagenes_restaurantes.get(restaurante)
        img = Image.open(img_path)
        img = img.resize((200, 200), Image.LANCZOS)  # Redimensionar el logo
        photo = ImageTk.PhotoImage(img)

        # Etiqueta con el logo del restaurante
        tk.Label(self.frame_pedidos, image=photo, bg="#87A96B").pack()
        self.frame_pedidos.image = photo  # Mantener referencia a la imagen

        # Etiqueta con el nombre del restaurante y los pedidos
        tk.Label(self.frame_pedidos, text=f"Pedidos para {restaurante}", font=("Arial", 18), bg="#87A96B").pack(pady=10)

        # Lista de pedidos para el restaurante
        lista_pedidos = tk.Listbox(self.frame_pedidos, width=70, height=10)
        for pedido in self.pedidos_restaurantes[restaurante]:
            lista_pedidos.insert(tk.END, pedido)  # Insertar cada pedido en la lista
        lista_pedidos.pack()

        # Mostrar el tiempo de entrega estimado
        tiempo_entrega = self.tiempos_entrega.get(restaurante, 20)  # Tiempo de entrega por defecto si no se encuentra
        tk.Label(self.frame_pedidos, text=f"Tiempo de entrega estimado: {tiempo_entrega} minutos", bg="#87A96B", font=("Arial", 16)).pack(pady=10)

        # Botón para cerrar sesión y regresar a la pantalla de selección de rol
        tk.Button(self.frame_pedidos, text="Cerrar Sesión", command=self.crear_pantalla_seleccion_rol, bg="#6C8EAD", fg="white").pack(pady=10)

    # Pantalla de selección de restaurantes para los consumidores
    def mostrar_pantalla_restaurantes_consumidor(self):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un nuevo frame para la selección de restaurantes
        self.frame_restaurantes = tk.Frame(self.root, bg="#87A96B")
        self.frame_restaurantes.pack(pady=20)

        tk.Label(self.frame_restaurantes, text="Selecciona un Restaurante", font=("Arial", 18), bg="#87A96B").pack(pady=10)

        # Mostrar el logo y el nombre de cada restaurante
        for restaurante in self.restaurantes:
            img_path = self.imagenes_restaurantes.get(restaurante.nombre_restaurante)
            img = Image.open(img_path)
            img = img.resize((180, 180), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            frame_restaurante = tk.Frame(self.frame_restaurantes, bg="#87A96B")
            frame_restaurante.pack(pady=20)

            # Etiqueta con el logo del restaurante
            tk.Label(frame_restaurante, image=photo, bg="#87A96B").pack(side=tk.LEFT, padx=10)
            tk.Label(frame_restaurante, text=restaurante.nombre_restaurante, font=("Arial", 16), bg="#87A96B").pack(side=tk.LEFT, padx=20)

            # Botón para seleccionar un restaurante
            tk.Button(frame_restaurante, text="Seleccionar", command=lambda r=restaurante: self.mostrar_menu_restaurante(r), bg="#6C8EAD", fg="white", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)

            frame_restaurante.image = photo  # Mantener la referencia de la imagen

        # Botón para regresar a la pantalla de selección de rol
        tk.Button(self.frame_restaurantes, text="Regresar", command=self.crear_pantalla_seleccion_rol, bg="#6C8EAD", fg="white", font=("Arial", 14)).pack(pady=10)

    # Pantalla para mostrar el menú de un restaurante
    def mostrar_menu_restaurante(self, restaurante):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un nuevo frame para mostrar el menú
        self.frame_menu = tk.Frame(self.root, bg="#87A96B")
        self.frame_menu.pack(pady=20)

        tk.Label(self.frame_menu, text=f"Menú de {restaurante.nombre_restaurante}", font=("Arial", 18), bg="#87A96B").pack(pady=10)

        # Crear una lista para mostrar los ítems del menú
        self.lista_menu = tk.Listbox(self.frame_menu, selectmode=tk.MULTIPLE, width=50, height=10)
        for item in restaurante.obtener_menu():
            self.lista_menu.insert(tk.END, str(item))  # Insertar cada ítem del menú
        self.lista_menu.pack(pady=10)

        # Mostrar la imagen del menú del restaurante
        img_path = self.imagenes_menus.get(restaurante.nombre_restaurante)
        img = Image.open(img_path)
        img = img.resize((300, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)

        # Etiqueta con la imagen del menú
        tk.Label(self.frame_menu, image=photo, bg="#87A96B").pack()
        self.frame_menu.image = photo  # Mantener la referencia a la imagen

        # Botón para hacer un pedido
        tk.Button(self.frame_menu, text="Hacer Pedido", command=lambda: self.mostrar_resumen_pedido(restaurante), bg="#6C8EAD", fg="white", font=("Arial", 14)).pack(pady=10)

        # Botón para regresar a la selección de restaurantes
        tk.Button(self.frame_menu, text="Regresar a Restaurantes", command=self.mostrar_pantalla_restaurantes_consumidor, bg="#6C8EAD", fg="white", font=("Arial", 14)).pack(pady=10)

    # Pantalla para mostrar el resumen del pedido
    def mostrar_resumen_pedido(self, restaurante):
        seleccionados = self.lista_menu.curselection()  # Obtener los ítems seleccionados
        if seleccionados:
            # Crear una lista con los ítems seleccionados
            items_seleccionados = [restaurante.obtener_menu()[i] for i in seleccionados]

            # Calcular el total del pedido
            total = sum(item.precio for item in items_seleccionados)

            # Definir el tiempo de espera según el restaurante
            tiempos_espera = {
                "Panitos": 15,
                "Mixtas Frankfurt": 25,
                "Café Barista": 30
            }
            tiempo_espera = tiempos_espera.get(restaurante.nombre_restaurante, 20)

            # Mostrar un resumen del pedido y el tiempo de espera
            resumen = "\n".join([f"{item.nombre} - Q{item.precio}" for item in items_seleccionados])
            messagebox.showinfo("Resumen del Pedido", f"Has pedido:\n{resumen}\n\nTotal: Q{total}\nTiempo de espera estimado: {tiempo_espera} minutos")

            self.mostrar_pantalla_restaurantes_consumidor()  # Regresar a la pantalla de selección de restaurantes

    # Método para inicializar los restaurantes con sus menús
    def inicializar_restaurantes(self):
        panitos = Restaurant("Panitos")
        panitos.agregar_item_menu(MenuItem("Pan de Roast Beef", 25))
        panitos.agregar_item_menu(MenuItem("Pan de Pollo", 25))
        panitos.agregar_item_menu(MenuItem("Pan de Carne Adobada", 25))

        mixtas_frankfurt = Restaurant("Mixtas Frankfurt")
        mixtas_frankfurt.agregar_item_menu(MenuItem("Mixtas de Salchicha con Todo", 35))
        mixtas_frankfurt.agregar_item_menu(MenuItem("Shuko de Salchicha con Todo", 35))
        mixtas_frankfurt.agregar_item_menu(MenuItem("Nachos con Queso, Aguacate y Carne Asada", 40))

        cafe_barista = Restaurant("Café Barista")
        cafe_barista.agregar_item_menu(MenuItem("Panini Bungiorno", 40))
        cafe_barista.agregar_item_menu(MenuItem("Baguette de Ensalada de Pollo", 35))
        cafe_barista.agregar_item_menu(MenuItem("Panini de Pollo y Pesto", 40))

        # Agregar los restaurantes a la lista
        self.restaurantes.append(panitos)
        self.restaurantes.append(mixtas_frankfurt)
        self.restaurantes.append(cafe_barista)


# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de Tkinter
    app = UVGustitosApp(root)  # Crear una instancia de la aplicación
    root.mainloop()  # Iniciar el loop principal de la ventana
