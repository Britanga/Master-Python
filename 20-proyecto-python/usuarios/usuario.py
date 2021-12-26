import datetime         # Importa el modulo que ya viene en Python datetime
import hashlib          # Importa el modulo que ya viene en Python Cifrar Contraseña
import usuarios.conexion as conexion    # Importa el modulo "conexion" del paquete "usuarios" y un alias "conexion" igual q el modulo "conexion"

# Llama al método conectar dentro del modulo "conexion"
connect = conexion.conectar()
# Creamos variables para acceder a la BD y al cursor
database = connect[0]           # Crea variable "database" y guarda el índice 0 q es el parámetro BD
cursor = connect[1]             # Crea variable "cursor" y guarda el índice 1 q es el parámetro cursor

# Contiene 1 constructor y 2 funciones (registrar e identificar)
class Usuario:

    # Definir constructor. Para inicializar y dar un valor las dif. variables de la clase
    def __init__(self, nombre, apellidos, email, password):
      # self.variable = variable q introdujo el usuario
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
      # No es necesario setter y getter en c/u variables, xq el programa no lo usará

    # Devuelve n° usuarios guardados y sus datos de la BD
    def registrar(self):
        fecha = datetime.datetime.now()    # Declaramos la fecha antes de usarla en la tupla
        
        # Declaramos variable "cifrado" = el método sha256
        cifrado = hashlib.sha256()
        # Cifrar contraseña
        cifrado.update(self.password.encode('utf8')) # encode convierte de string a byte

        # %s Sustituye datos de una tupla
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        # Creamos la tupla
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        # cifrado.hexdigest() = guarda la contraseña en string hexadecimal en la BD

        try:    
            # Ejecutar consulta
            # (1erParámetro "la consulta"/2doParámetro "datos del usuario")
            cursor.execute(sql,usuario)
            # Indispensable, guarda la consulta en la BD
            database.commit()
            # rowcount Muestra n° registrados (siempre es 1, xq registra 1x1 el programa)
            result = [cursor.rowcount, self]    
        except: # Limpia líneas de error (email repetido) y devuelve un 0 q muestra msj...
            result = [0, self] # Msj. "No te haz registrado correctamente!!!"
        # devuelve el n° registros modificados y el propio objeto con sus atributos  
        return result

    # Devuelve la tupla de la tabla "usuarios" del usuario actual si es que esta en la BD
    def identificar(self):
        # Consulta q comprueba si el email existe y la contraseña sea correcta
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Declaramos variable "cifrado" = el método sha256
        cifrado = hashlib.sha256()
        # Cifrar contraseña
        cifrado.update(self.password.encode('utf8')) # encode convierte de string a byte

        # Declaramos los Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())
        # cifrado.hexdigest() = elige la contraseña en string hexadecimal en la BD

        # Ejecuta Consulta(1er parámetro=Consulta, 2do parámetro=Datos)
        cursor.execute(sql, usuario)

        # Guarda la tupla de la tabla "usuarios" en "result" que sea = datos email y contraseña ingresados x el usuario
        result = cursor.fetchone()

        # Devuelve el resultado
        return result