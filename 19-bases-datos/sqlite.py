# Importar modulo
import sqlite3

# Conexión a BD SQLite
# Crea BD en carpeta raíz/principal "Master-Python"
#conexion = sqlite3.connect('pruebas.db')    # Parámetro es el nombre de la BaseDatos
# Crea BD en carpeta específica "19-bases-datos"
conexion = sqlite3.connect('./19-bases-datos/pruebas.db')

# Crear cursor: Para poder ejecutar consultas
cursor = conexion.cursor()

# Crear tabla
"""
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"titulo varchar(255), "+
"descripcion text, "+
"precio int(255)"+
")")
o
"""
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")

# Guardar cambios: Para guardar las consultas
conexion.commit()

# Insertar datos en Tabla
"""
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción de mi producto', 550)")
conexion.commit()
"""

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

# Instertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "Buen PC", 700),
    ("Telefono movil", "Buen Telefono", 140),
    ("Placa base", "Buena placa", 80),
    ("Tablet 15", "Buena tablet", 300),
]
# Es necesario el 2do parámetro "productos" para poder pasar los valores al INSERT
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()   # Para guardar las consultas

# Update
# Actualiza el producto que tenga de precio 80 a 678
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

# Listar/Mostrar datos
#cursor.execute("SELECT * FROM productos;")  # Elige todos los datos de la tabla por el *
# Elige los datos de la tabla cuyo precio sea mayor/igual a 300
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")

productos = cursor.fetchall()    # Elige la lista completa con sus tuplas
#print(productos)                # Muestra todas las tuplas de la lista
for producto in productos:      
    #print(producto)             # Muestra c/u de las tuplas de la lista
    
    # Muestra c/u atributos de la tupla
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()     # Elige 1er registro de "titulo" o
print(producto)                  # cualquier atributo que seleccionemos

#print(cursor)                   # Muestra que es un objeto

# Cerrar conexión: Al cerrar la conexión, se guardan los cambios
conexion.close()