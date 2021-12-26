import usuarios.conexion as conexion # Importa el modulo "conexion" del paquete "usuarios" y un alias "conexion" igual q el modulo "conexion"

# Llama al método conectar dentro del modulo "conexion"
connect = conexion.conectar()
# Creamos variables para acceder a la BD y al cursor
database = connect[0]           # Crea variable "database" y guarda el índice 0 q es el parámetro BD
cursor = connect[1]             # Crea variable "cursor" y guarda el índice 1 q es el parámetro cursor

# Contiene 1 constructor y 3 funciones (guardar, listar y eliminar)
class Nota:

    # Definir constructor. Para inicializar y dar un valor las dif. variables de la clase
    def __init__(self, usuario_id, titulo = "", descripcion = ""):  # titulo/descripcion = "" significa q son campos opcionales (ahorra esas "" como parámetro de funcion "mostrar" modulo "acciones" paquete "notas")
        # self.variable = variable q introdujo el usuario
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion

    # Devuelve n° notas guardadas del usuario actual en la BD y datos de la nota
    def guardar(self):
        # Declaramos la consulta (%s Sustituye datos de una tupla)
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"   # NOW() automaticamente guarda la fecha actual
        # Creamos la tupla
        nota = (self.usuario_id, self.titulo, self.descripcion)

        # Ejecutar consulta(1erParámetro=Consulta, 2doParámetro=Datos)
        cursor.execute(sql, nota)
        # Indispensable, guarda la consulta en la BD
        database.commit()

        # Devuelve [n°Registros, DatosTupla]
        return [cursor.rowcount, self]

    # Devuelve todas las tuplas de tabla notas del usuario actual de la BD
    def listar(self):
        """ Declaramos consulta para acceder a todas las notas de un usuario en concreto
        (Elige todas notas cuando "usuario_id" = al objeto "usuario" elegido actual)"""
        sql = f"SELECT * FROM notas WHERE usuario_id = {self.usuario_id}"

        # Ejecutar consulta(1erParámetro=Consulta)
        cursor.execute(sql)
        
        # Guarda el resultado de la consulta (fetchall xq queremos todas las tuplas de tabla notas del usuario actual)
        result = cursor.fetchall()

        # Devuelve el resultado
        return result

    # Devuelve el n° de notas eliminadas y datos de la nota eliminada del usuario actual en la BD
    def eliminar(self): # Parámetro "self" = datos de la nota que será eliminada
        """Declaramos consulta para borrar la nota de un usuario en concreto
        [Borra la nota cuando ("usuario_id" = al objeto "usuario" elegido actual)
        Y (titulo sea igual al titulo que llega por parámetro pero cuando este esté contenido en el titulo de la propia nota)]
        LIKE = usa comodines para buscar ese título de la nota"""
        sql = f"DELETE FROM notas WHERE usuario_id = {self.usuario_id} AND titulo LIKE '%{self.titulo}%'"  # los % en '%{self.titulo}%' significa cuando el título este contenido dentro del título que tengo guardado en la BD

        # Ejecutar consulta(1erParámetro=Consulta)
        cursor.execute(sql)
        # Indispensable, guarda la consulta en la BD
        database.commit()

        return [cursor.rowcount, self]  # rowcount = n° de notas eliminadas / self = datos de la nota eliminada