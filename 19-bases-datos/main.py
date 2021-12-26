import mysql.connector

# Conexión a BD MySQL
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"  # Al tener la BD creada, entra a la BD "master_python"
)

# ¿La conexión ha sido correcta?
#print(database) # Muestra que es un objeto de mysql.connector

# Crear cursor: Para poder ejecutar consultas
cursor = database.cursor(buffered=True)
# Parámetro buffered permite hacer muchas consultas usando el mismo cursor

# Crear BD MySQL
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python") # Sino existe, crea BaseDatos

cursor.execute("SHOW DATABASES")    # Obtiene todos los datos de las BaseDatos

for bd in cursor:
    print(bd)   # Muestra c/u de las BaseDatos
"""

# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,            # Puede tener max. 10 cifras y 2 decimales
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)  # Define PrimaryKey "id"
)
""")
"""
cursor.execute("SHOW TABLES")               # Cursor obtiene todas las tablas de la BD

for table in cursor:
    print(table)                            # Muestra c/u de las tablas de BD "master_python"
"""
# Insertar registro
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
#database.commit()   # Indispensable, guarda la consulta en la BD

# Insertar varios registros
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)
]

# %s = marca, modelo y precio. Usar "coches" como 2do parámetro para guardar esos datos.
#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()   # Indispensable, guarda la consulta en la BD

# Listar/Mostrar datos
# Elige todos los datos de la tabla
cursor.execute("SELECT * FROM vehiculos")
# Elige los datos de la tabla cuyo precio sea menor/igual a 5000 y marca sea 'Seat'
#cursor.execute("SELECT * FROM vehiculos WHERE precio <= 5000 AND marca = 'Seat'")

result = cursor.fetchall()  # Elige la lista completa con sus tuplas

print("---- TODOS MIS COCHES ----")
for coche in result:
    #print(coche)            # Muestra c/u de las tuplas de la lista

    # Muestra c/u atributos de la tupla
    print(coche[1], coche[2], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()   # Guarda la 1era tupla de la tabla vehiculos en coche
print(coche)                # Muestra la 1era tupla de coche

# Borrar tupla completa si la marca = 'Renault'
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()   # Indispensable, guarda la consulta en la BD

print(cursor.rowcount, "borrados!!")    # Muestra cuántos ha borrado

# Actualizar
# Actualiza el vehiculo que tenga de modelo 'Seat' a 'León'
cursor.execute("UPDATE vehiculos SET modelo='León' WHERE marca='Seat'")
database.commit()   # Indispensable, guarda la consulta en la BD

print(cursor.rowcount, "actualizados!!")