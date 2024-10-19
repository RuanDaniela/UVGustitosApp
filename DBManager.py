import sqlite3

class DBManager:
    def __init__(self):
        self.conexion = self.conectar_db()

    def conectar_db(self):
        # Conectando a una base de datos SQLite (esto creará el archivo si no existe)
        conexion = sqlite3.connect('uvgustitos.db')
        return conexion

    def crear_tabla_user(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(255) NOT NULL,
                contrasena VARCHAR(255) NOT NULL
            )
        ''')
        self.conexion.commit()

    def crear_tabla_restaurante(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS restaurante (
                restaurante_id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_rest VARCHAR(255) NOT NULL,
                contrasena VARCHAR(255) NOT NULL
            )
        ''')
        self.conexion.commit()

    def crear_tabla_ordenes(self):
        cursor = self.conexion.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ordenes (
                id_Orden INTEGER PRIMARY KEY AUTOINCREMENT,
                producto TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL,
                usuario_id INT NOT NULL,
                restaurante_id INT NOT NULL,
                estado TEXT NOT NULL,
                FOREIGN KEY (usuario_id) REFERENCES user(usuario_id),
                FOREIGN KEY (restaurante_id) REFERENCES restaurante(restaurante_id)
            )
        ''')
        self.conexion.commit()

# Ejemplo de uso
db = DBManager()
db.crear_tabla_user()         # Primero crear la tabla de usuarios
db.crear_tabla_restaurante()  # Luego la tabla de restaurantes
db.crear_tabla_ordenes()      # Finalmente, la tabla de órdenes
