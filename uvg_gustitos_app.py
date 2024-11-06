import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from user import User
from menu_item import MenuItem
from restaurant import Restaurant

# Clase principal UVGustitosApp para la aplicación con Tkinter
class UVGustitosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UVGustitos - Selección de Rol")
        self.root.geometry("900x700")  # Tamaño más grande de la ventana

        # Fondo verde para toda la app
        self.root.configure(bg="#87A96B")  # Color verde

        # Crear los usuarios para la autenticación (Restaurantes y Consumidor)
        self.consumidor = User("consumidor1", "pass123")

        # Usuarios para cada restaurante
        self.restaurante_usuarios = {
            "Panitos": User("panitos_user", "panitos_pass"),
            "Mixtas Frankfurt": User("mixtas_user", "mixtas_pass"),
            "Café Barista": User("barista_user", "barista_pass")
        }

        # Lista de pedidos (falsos) para cada restaurante
        self.pedidos_restaurantes = {
            "Panitos": ["Pedido 1: Pan de Roast Beef, Pan de Pollo", "Pedido 2: Pan de Carne Adobada", "Pedido 3: Pan de Roast Beef"],
            "Mixtas Frankfurt": ["Pedido 1: Mixtas de Salchicha", "Pedido 2: Nachos con Queso y Carne Asada", "Pedido 3: Shuko de Salchicha"],
            "Café Barista": ["Pedido 1: Panini Bungiorno", "Pedido 2: Baguette de Ensalada de Pollo", "Pedido 3: Panini de Pollo y Pesto"]
        }

        # Tiempos de entrega para cada restaurante
        self.tiempos_entrega = {
            "Panitos": 15,
            "Mixtas Frankfurt": 25,
            "Café Barista": 30
        }

        # Imágenes para cada restaurante (logo y menú)
        self.imagenes_restaurantes = {
            "Panitos": "panitos.png",
            "Mixtas Frankfurt": "mixtas.png",
            "Café Barista": "barista.png"
        }

        # Imágenes para los menús de cada restaurante
        self.imagenes_menus = {
            "Panitos": "panitos2.png",
            "Mixtas Frankfurt": "mixtas2.png",
            "Café Barista": "barista2.png"
        }

        # Imagen del logo de la aplicación
        self.logo_path = "UVGustosImagen.png"  # Ruta de la imagen del logo

        # Lista de restaurantes
        self.restaurantes = []
        self.inicializar_restaurantes()

        # Crear la interfaz gráfica de selección de rol
        self.crear_pantalla_seleccion_rol()

    # Método para ocultar todos los frames (útil al cambiar de pantalla)
    def ocultar_frames(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

    # Pantalla de selección de rol (Restaurante o Consumidor)
    def crear_pantalla_seleccion_rol(self):
        self.ocultar_frames()

        self.frame_seleccion = tk.Frame(self.root, bg="#87A96B")
        self.frame_seleccion.pack(pady=20)

        # Cargar y mostrar el logo
        logo_img = Image.open(self.logo_path)
        logo_img = logo_img.resize((250, 250), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        tk.Label(self.frame_seleccion, image=logo_photo, bg="#87A96B").pack(pady=10)
        self.frame_seleccion.logo = logo_photo  # Mantener la referencia a la imagen

        tk.Label(self.frame_seleccion, text="¿Quién eres?", font=("Arial", 22, "bold"), bg="#87A96B").pack(pady=20)

        tk.Button(self.frame_seleccion, text="Soy un Consumidor", command=self.crear_pantalla_login_consumidor, bg="#6C8EAD", fg="#16423C", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.frame_seleccion, text="Soy un Restaurante", command=self.crear_pantalla_login_restaurante, bg="#6C8EAD", fg="#16423C", font=("Arial", 16)).pack(pady=10)

    # Pantalla de inicio de sesión para Consumidores
    def crear_pantalla_login_consumidor(self):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un nuevo frame para el inicio de sesión del consumidor
        self.frame_login_consumidor = tk.Frame(self.root, bg="#87A96B")
        self.frame_login_consumidor.pack(pady=20)

        # Cargar y mostrar el logo del consumidor en la pantalla de inicio de sesión
        self.logo_user = "Consumidor.png"  # Cambia la ruta del logo aquí
        logo_img = Image.open(self.logo_user)
        logo_img = logo_img.resize((200, 200), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        tk.Label(self.frame_login_consumidor, image=logo_photo, bg="#87A96B").pack(pady=10)
        self.frame_login_consumidor.logo = logo_photo

        # Etiqueta para indicar inicio de sesión
        tk.Label(self.frame_login_consumidor, text="¡Bienvenido a UVGustitos!", font=("Arial", 24), bg="#87A96B").pack(pady=10)
        tk.Label(self.frame_login_consumidor, text="Inicio de sesión - Consumidor", font=("Arial", 15), bg="#87A96B").pack(pady=10)

        # Campo de entrada para el nombre de usuario
        tk.Label(self.frame_login_consumidor, text="Nombre de usuario:", bg="#87A96B").pack()
        self.entry_usuario_consumidor = tk.Entry(self.frame_login_consumidor, width=30)
        self.entry_usuario_consumidor.pack(pady=5)

        # Campo de entrada para la contraseña
        tk.Label(self.frame_login_consumidor, text="Contraseña:", bg="#87A96B").pack()
        self.entry_contrasena_consumidor = tk.Entry(self.frame_login_consumidor, show="*", width=30)
        self.entry_contrasena_consumidor.pack(pady=5)

        self.root.update()
        # Botón para iniciar sesión
        tk.Button(self.frame_login_consumidor, text="Iniciar Sesión", command=self.iniciar_sesion_consumidor, bg="#6C8EAD", fg="black").pack(pady=10)
        #tk.Label(self.frame_login_consumidor, text="Me confundí, soy un restaurante", font=("Arial", 14), bg="#87A96B").pack(pady=10)
        tk.Button(self.frame_login_consumidor, text="Regresar", command=self.crear_pantalla_seleccion_rol, bg="#6C8EAD", fg="black").pack(pady=10)



    # Pantalla de inicio de sesión para Restaurantes
    def crear_pantalla_login_restaurante(self):
        self.ocultar_frames()  # Ocultar cualquier frame previo

        # Crear un nuevo frame para el inicio de sesión del restaurante
        self.frame_login_restaurante = tk.Frame(self.root, bg="#87A96B")
        self.frame_login_restaurante.pack(pady=20)

        # Cargar y mostrar el logo en la pantalla de inicio de sesión
        self.logo_user = "Restaurante.png"  # Cambia la ruta del logo aquí
        logo_user = Image.open(self.logo_user)
        logo_user = logo_user.resize((200, 200), Image.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_user)
        tk.Label(self.frame_login_restaurante, image=logo_photo, bg="#87A96B").pack(pady=10)
        self.frame_login_restaurante.logo = logo_photo

        # Etiqueta para indicar inicio de sesión
        tk.Label(self.frame_login_restaurante, text="¡Bienvenido a UVGustitos!", font=("Arial", 20), bg="#87A96B").pack(pady=10)
        tk.Label(self.frame_login_restaurante, text="Inicio de sesión - Restaurante", font=("Arial", 15), bg="#87A96B").pack(pady=10)

        # Campo de entrada para el nombre de usuario del restaurante
        tk.Label(self.frame_login_restaurante, text="Nombre de usuario:", bg="#87A96B").pack()
        self.entry_usuario_restaurante = tk.Entry(self.frame_login_restaurante, width=30)
        self.entry_usuario_restaurante.pack(pady=5)

        # Campo de entrada para la contraseña del restaurante
        tk.Label(self.frame_login_restaurante, text="Contraseña:", bg="#87A96B").pack()
        self.entry_contrasena_restaurante = tk.Entry(self.frame_login_restaurante, show="*", width=30)
        self.entry_contrasena_restaurante.pack(pady=5)

        self.root.update()
        tk.Button(self.frame_login_restaurante, text="Iniciar Sesión", command=self.iniciar_sesion_restaurante, bg="#6C8EAD", fg="black").pack(pady=10)
        tk.Button(self.frame_login_restaurante, text="Regresar", command=self.crear_pantalla_seleccion_rol, bg="#6C8EAD", fg="black").pack(pady=10)
    
    # Método para manejar el inicio de sesión como Consumidor
    def iniciar_sesion_consumidor(self):
        nombre_usuario = self.entry_usuario_consumidor.get()
        contrasena = self.entry_contrasena_consumidor.get()

        if self.consumidor.iniciar_sesion(nombre_usuario, contrasena):
            messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso como Consumidor")
            self.mostrar_pantalla_restaurantes_consumidor()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas para Consumidor")

    # Método para manejar el inicio de sesión como Restaurante
    def iniciar_sesion_restaurante(self):
        nombre_usuario = self.entry_usuario_restaurante.get()
        contrasena = self.entry_contrasena_restaurante.get()

        # Validar si el restaurante existe y las credenciales son correctas
        for restaurante, usuario in self.restaurante_usuarios.items():
            if usuario.iniciar_sesion(nombre_usuario, contrasena):
                messagebox.showinfo("Inicio de sesión", f"Inicio de sesión exitoso como {restaurante}")
                self.mostrar_pedidos_restaurante(restaurante)
                return

        messagebox.showerror("Error", "Credenciales incorrectas para Restaurante")

    # Método para mostrar los pedidos hechos al restaurante junto con el tiempo de entrega y logo
    def mostrar_pedidos_restaurante(self, restaurante):
        self.ocultar_frames()

        self.frame_pedidos = tk.Frame(self.root, bg="#87A96B")
        self.frame_pedidos.pack(pady=20)

        # Mostrar el logo del restaurante
        img_path = self.imagenes_restaurantes.get(restaurante)
        img = Image.open(img_path)
        img = img.resize((200, 200), Image.LANCZOS)  # Imagen más grande del logo
        photo = ImageTk.PhotoImage(img)

        # Etiqueta con el logo
        tk.Label(self.frame_pedidos, image=photo, bg="#87A96B").pack()
        self.frame_pedidos.image = photo  # Mantener referencia a la imagen

        tk.Label(self.frame_pedidos, text=f"Pedidos para {restaurante}", font=("Arial", 18), bg="#87A96B").pack(pady=10)

        lista_pedidos = tk.Listbox(self.frame_pedidos, width=70, height=10)  # Cuadro blanco más grande
        for pedido in self.pedidos_restaurantes[restaurante]:
            lista_pedidos.insert(tk.END, pedido)
        lista_pedidos.pack()

        # Mostrar el tiempo de entrega del restaurante
        tiempo_entrega = self.tiempos_entrega.get(restaurante, 20)  # Tiempo por defecto de 20 minutos si no se encuentra
        tk.Label(self.frame_pedidos, text=f"Tiempo de entrega estimado: {tiempo_entrega} minutos", bg="#87A96B", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.frame_pedidos, text="Cerrar Sesión", command=self.crear_pantalla_seleccion_rol, bg="#6C8EAD", fg="white").pack(pady=10)

    # Método para mostrar la pantalla de selección de restaurantes (Consumidor)
    def mostrar_pantalla_restaurantes_consumidor(self):
        self.ocultar_frames()
        self.root.update()
        
        # Crear el frame principal primero
        self.frame_restaurantes = tk.Frame(self.root, bg="#87A96B")
        self.frame_restaurantes.pack(pady=20)

        # Cargar y mostrar la imagen principal en la parte superior
        img_inicio_path = "BienvenidaUser.png"  # Cambia esto por la ruta de tu imagen
        img_inicio = Image.open(img_inicio_path)
        img_inicio = img_inicio.resize((400, 170), Image.LANCZOS)  # Ajusta el tamaño según necesites
        self.photo_inicio = ImageTk.PhotoImage(img_inicio)

        # Mostrar la imagen en el frame
        tk.Label(self.frame_restaurantes, image=self.photo_inicio, bg="#87A96B").pack(pady=10)
        # Mostrar imagen de cada restaurante y agregar botón para seleccionar
        for restaurante in self.restaurantes:
            img_path = self.imagenes_restaurantes.get(restaurante.nombre_restaurante)
            img = Image.open(img_path)
            img = img.resize((150, 150), Image.LANCZOS)  # Imagen más grande
            photo = ImageTk.PhotoImage(img)

            frame_restaurante = tk.Frame(self.frame_restaurantes, bg="#87A96B")
            frame_restaurante.pack(pady=10)

            # Etiqueta con imagen y nombre del restaurante
            tk.Label(frame_restaurante, image=photo, bg="#87A96B").pack(side=tk.LEFT, padx=10)
            tk.Label(frame_restaurante, text=restaurante.nombre_restaurante, font=("Arial", 16), bg="#87A96B").pack(side=tk.LEFT, padx=20)

            # Botón para seleccionar restaurante
            tk.Button(frame_restaurante, text="Seleccionar", command=lambda r=restaurante: self.mostrar_menu_restaurante(r), bg="#6C8EAD", fg="black", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)

            # Mantener la referencia de las imágenes
            frame_restaurante.image = photo

        # Botón de regreso
        tk.Button(self.frame_restaurantes, text="Regresar", command=self.crear_pantalla_seleccion_rol, bg="#6C8EAD", fg="white", font=("Arial", 14)).pack(pady=10)

    # Método para mostrar el menú del restaurante seleccionado
    def mostrar_menu_restaurante(self, restaurante):
        self.ocultar_frames()

        # Crear un frame para el scroll y un canvas para el contenido desplazable
        self.frame_menu_scroll = tk.Frame(self.root)
        self.frame_menu_scroll.pack(pady=20, fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(self.frame_menu_scroll, bg="#87A96B")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.frame_menu_scroll, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        # Crear un frame dentro del canvas para el contenido
        frame_contenido = tk.Frame(canvas, bg="#87A96B")
        canvas.create_window((0, 0), window=frame_contenido, anchor="nw")

        # Cargar la imagen al inicio
        img_inicio_path = "LogoMenus.png"  # Asegúrate de que esta sea la ruta correcta
        img_inicio = Image.open(img_inicio_path)
        img_inicio = img_inicio.resize((400, 170), Image.LANCZOS)  # Ajustar tamaño según lo necesario
        self.photo_inicio = ImageTk.PhotoImage(img_inicio)

        # Mostrar la imagen al principio (centrada en el frame)
        img_label = tk.Label(frame_contenido, image=self.photo_inicio, bg="#87A96B")
        img_label.pack(pady=10, anchor="center")

        # Agregar el texto y el menú
        tk.Label(frame_contenido, text=f"Menú de {restaurante.nombre_restaurante}", font=("Arial", 18), bg="#87A96B").pack(pady=10, anchor="center")

        # Crear el Listbox para el menú
        self.lista_menu = tk.Listbox(frame_contenido, selectmode=tk.MULTIPLE, width=50, height=10)
        for item in restaurante.obtener_menu():
            self.lista_menu.insert(tk.END, str(item))
        self.lista_menu.pack(pady=10, anchor="center")

        # Mostrar la imagen del menú del restaurante (debajo del menú)
        img_path = self.imagenes_menus.get(restaurante.nombre_restaurante)
        img = Image.open(img_path)
        img = img.resize((300, 300), Image.LANCZOS)  # Ajuste de tamaño de la imagen del menú
        photo = ImageTk.PhotoImage(img)

        # Etiqueta con la imagen del menú (centrada)
        img_menu_label = tk.Label(frame_contenido, image=photo, bg="#87A96B")
        img_menu_label.pack(pady=10, anchor="center")
        frame_contenido.image = photo  # Mantener la referencia de la imagen

        # Botones de acción (centrados)
        tk.Button(frame_contenido, text="Hacer Pedido", command=lambda: self.mostrar_resumen_pedido(restaurante), bg="#6C8EAD", fg="black", font=("Arial", 14)).pack(pady=10, anchor="center")
        tk.Button(frame_contenido, text="Regresar a Restaurantes", command=self.mostrar_pantalla_restaurantes_consumidor, bg="#6C8EAD", fg="black", font=("Arial", 14)).pack(pady=10, anchor="center")

        # Actualizar la región visible para que el canvas se ajuste al contenido
        frame_contenido.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    # Método para mostrar el resumen del pedido con el tiempo de espera
    def mostrar_resumen_pedido(self, restaurante):
        seleccionados = self.lista_menu.curselection()
        if seleccionados:
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

            # Crear el resumen del pedido
            resumen = "\n".join([f"{item.nombre} - Q{item.precio}" for item in items_seleccionados])
            messagebox.showinfo("Resumen del Pedido", f"Has pedido:\n{resumen}\n\n"
                                                     f"Total: Q{total}\n"
                                                     f"Tiempo de espera estimado: {tiempo_espera} minutos")
            self.mostrar_pantalla_restaurantes_consumidor()

    # Inicializar los restaurantes con sus menús
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

        self.restaurantes.append(panitos)
        self.restaurantes.append(mixtas_frankfurt)
        self.restaurantes.append(cafe_barista)


if __name__ == "__main__":
    root = tk.Tk()
    app = UVGustitosApp(root)
    root.mainloop()