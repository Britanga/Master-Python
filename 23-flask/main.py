from flask import Flask, flash, redirect, url_for, render_template, request # Para usar Flask, flash, redirect, url_for, render_template, request
from datetime import datetime # Para usar fecha en el pie de página
from flask_mysqldb import MySQL # Para conexión a la BD MySQL

# Crear app de Flask
app = Flask(__name__)

# Crear clave secreta para poder mostrar msj flash
app.secret_key = 'clave_secreta_flask'

# Conexión BD
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectoflask'

mysql = MySQL(app)

# Crear context processors
@app.context_processor
def date_now():

    # Devuelve gracias a la funcion utcnow la fecha actual
    return {
        'now': datetime.utcnow()
    }

# Crear una ruta para mostrar que funciona (Endpoints)
@app.route('/')
# Ruta vinculada a un metodo o funcion
def index():

    edad = 101
    personas = ['Jesús', 'Paco', 'Francisco', 'David']

    #return "Aprendiendo Flask con Jesús Brito"
    # Pasar datos a la template
    return render_template('index.html',
                            edad=edad,
                            dato1="Valor",
                            dato2="Valor2",
                            lista=["uno", "dos", "tres"],
                            personas=personas
                        )

# Multiples Rutas
# Ruta con parámetros
#@app.route('/informacion/<string:nombre>/<int:apellidos>')
#def informacion(nombre, apellidos): # parámetro nombre debe llamarse igual que en '/informacion/<nombre>'
#    #return f"<h1>Página de información {nombre}</h1>" # 1 sola linea
#    return f"""
#            <h1>Página de información</h1>
#            <p>Esta es la página de información</p>
#            <h3>Bienvenido, {nombre} {apellidos}</h3>
#    """ # Multiples lineas

# Ruta con parametro opcional
@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<apellidos>')
def informacion(nombre = None, apellidos = None):

    texto = ""
    if nombre != None and apellidos != None: # Si nombre y apellidos exiten, muestra msj
        #texto = f"<h3>Bienvenido, {nombre} {apellidos}</h3>"
        texto = f"Bienvenido, {nombre} {apellidos}"

    #return f"""
    #        <h1>Página de información</h1>
    #        <p>Esta es la página de información</p>
    #        {texto}
    #""" # Multiples lineas
    return render_template('informacion.html',
                            texto=texto
                        )

# Redirecciones en Flask
@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion = None):

    if redireccion is not None: # Si es diferente a None
        return redirect(url_for('lenguajes'))

    #return "<h1>Página de contacto</h1>"
    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    #return "<h1>Página de lenguajes</h1>"
    return render_template('lenguajes.html')

# Insertar datos en MySQL
"""
@app.route('/insertar-coche')
def insertar_coche():
    # Crear cursor para declarar consulta
    cursor = mysql.connection.cursor()
    # Declara consulta
    cursor.execute(f"INSERT INTO coches VALUES(NULL, 'Lambo', 'Gallardo', '100000', 'Los Angeles')")
    # Guarda consulta
    cursor.connection.commit()

    # Redirige a la pagina de inicio
    return redirect(url_for('index'))
"""

@app.route('/crear-coche', methods=['GET','POST']) # Habilitar métodos para guardar datos del formulario
def crear_coche():
    if request.method == 'POST':

        # Manera de guardar datos del usuario
        # Recibo los datos del formulario
        marca = request.form['marca'] # [''] son los name del fichero "crear_coche.html"
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        # Devuelve los datos del formulario
        #return f"{marca} {modelo} {precio} {ciudad}"

        # Crear cursor para declarar consulta
        cursor = mysql.connection.cursor()
        # Declara consulta
        cursor.execute("INSERT INTO coches VALUES(NULL, %s, %s, %s, %s)", (marca, modelo, precio, ciudad))
        # Guarda consulta
        cursor.connection.commit()
        # Crear msj. flash
        flash('Has creado el coche correctamente!!')

        # Manera de guardar datos ya establecidos
        """
        # Crear cursor para declarar consulta
        cursor = mysql.connection.cursor()
        # Declara consulta
        cursor.execute(f"INSERT INTO coches VALUES(NULL, 'Lambo', 'Gallardo', '100000', 'Los Angeles')")
        # Guarda consulta
        cursor.connection.commit()
        """

        # Redirige a la pagina de inicio
        return redirect(url_for('index'))

    return render_template('crear_coche.html')

# Método de listado de coches
@app.route('/coches')
def coches():
    # Crear cursor para declarar consulta
    cursor = mysql.connection.cursor()
    # Declara consulta
    # Ordena de más nuevo a más viejo
    cursor.execute("SELECT * FROM coches ORDER BY id DESC")
    # Saco toda la info. de la tabla
    coches = cursor.fetchall()
    # Cierro ejecución del cursor
    cursor.close()

    # Pasar datos a la template
    return render_template('coches.html', coches=coches)

# Método de detalles del coche
@app.route('/coche/<coche_id>')
def coche(coche_id):
    # Crear cursor para declarar consulta
    cursor = mysql.connection.cursor()
    # Declara consulta
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    # Saco toda la info. de la tabla
    coche = cursor.fetchall()
    # Cierro ejecución del cursor
    cursor.close()

    # Pasar datos a la template
    return render_template('coche.html', coche=coche[0])

# Método eliminar registro del coche
@app.route('/borrar-coche/<coche_id>')
def borrar_coche(coche_id):
    # Crear cursor para declarar consulta
    cursor = mysql.connection.cursor()
    # Declara consulta
    cursor.execute(f"DELETE FROM coches WHERE id = {coche_id}")
    # Guarda consulta
    mysql.connection.commit()
    # Msj. flash
    flash('El coche ha sido eliminado !!')

    # Redirige a la pagina de inicio
    return redirect(url_for('coches'))

# Método de editar el coche
@app.route('/editar-coche/<coche_id>', methods=['GET','POST'])
def editar_coche(coche_id):
    # Para actualizar los datos editados
    if request.method == 'POST':

        # Manera de guardar datos del usuario
        # Recibo los datos del formulario
        marca = request.form['marca'] # [''] son los name del fichero "crear_coche.html"
        modelo = request.form['modelo']
        precio = request.form['precio']
        ciudad = request.form['ciudad']

        # Crear cursor para declarar consulta
        cursor = mysql.connection.cursor()
        # Declara consulta
        # Actualiza el registro cuyo "id" coincida con el que se esta pasando por la URL
        # (actualiza todos los atributos de la tabla indicada)
        cursor.execute("""
            UPDATE coches
            SET marca = %s,
                modelo = %s,
                precio = %s,
                ciudad = %s
            WHERE id = %s
        """, (marca, modelo, precio, ciudad, coche_id))
        # Guarda consulta
        cursor.connection.commit()
        # Crear msj. flash
        flash('Has editado el coche correctamente!!')

        # Redirige al listado de coches
        return redirect(url_for('coches'))


    # Sino, crea coche
    # Crear cursor para declarar consulta
    cursor = mysql.connection.cursor()
    # Declara consulta
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    # Saco toda la info. de la tabla
    coche = cursor.fetchall()
    # Cierro ejecución del cursor
    cursor.close()

    # Pasar datos a la template
    return render_template('crear_coche.html', coche=coche[0])

# Comprobar que funciona
# Sirve para identificar que este archivo es el fichero principal
if __name__ == '__main__':
    # True xq necesitamos que el servidor de Flask funcione perfectamente y además
    # cuando hay un cambio en el codigo hace que el servidor recargue y se reinicie automaticamente
    app.run(debug=True)