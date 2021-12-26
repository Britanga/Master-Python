import mysql.connector  # Importa libreria de Mysql para conectarme a la BD

# Devuelve la BD y el cursor
def conectar():
    # Conecta la BD
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="master_python",
        port=3306       # Puerto donde funciona el servidor de BD en la PC
    )

    #print(database) # Comprueba si la conexión de BD funcionó (Msj. diciendo q es un objeto)

    # Activamos Cursor. permite hacer consultas
    cursor = database.cursor(buffered=True)
    # Parámetro buffered permite hacer muchas consultas usando el mismo cursor

    return [database, cursor]