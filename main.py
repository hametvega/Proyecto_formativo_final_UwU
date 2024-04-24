from flask import Flask, render_template, redirect, request, url_for,flash, session

import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "",
    database = "farm_to_cell")

app = Flask(__name__)
app.secret_key = 'Dani_Server';

cursor =  db.cursor()

#Definir rutas
@app.route('/')
def Pagina_Principal():
    
    print('This is a route. :)')
    
    return render_template('Index.html');

@app.route('/Ayuda_Agraria')
def Pagina_De_Ayuda():

    print('This is another route. :/')

    return render_template('Agro_Help.html');

@app.route('/Productos')
def Pagina_De_Productos():

    print('This is another route. :D')

    return render_template('Registro_Product.html');

@app.route('/Registro_personas', methods=['GET', 'POST'])
def Registrando_p():
        if request.method == 'POST': #si el metodo es GET si suelta error
            nombre_p = request.form.get['txtNombre']
            apellido_p = request.form.get['txtApellido']
            celular_p = request.form.get['txtCelular']
            direccion_p = request.form.get['txtDireccion']
            correo_p = request.form.get['txtEmail']
            contraseña_p = request.form.get['txtContraseña']

            # Validar que todos los campos estén llenos
            if not (nombre_p and apellido_p and celular_p and direccion_p and correo_p and contraseña_p):
                return render_template('Pagina_De_Registro_E_Inicio_Sesion.html', error='Por favor, complete todos los campos del formulario.')

            try:
                cursor.execute("INSERT INTO registro_personas (Nombre_persona, Apellido_person, Celular, Dirección, Email, Contraseña) VALUES (%s, %s, %s, %s, %s, %s)", 
                            (nombre_p, apellido_p, celular_p, direccion_p, correo_p, contraseña_p))
                db.commit()
                return redirect(url_for('Registrando_p'))
            except mysql.connector.errors.IntegrityError as e:
                return render_template('Pagina_De_Registro_E_Inicio_Sesion.html', error=str(e))
        
        return render_template('Pagina_De_Registro_E_Inicio_Sesion.html')
#Los datos no se guardan en la tabla sin embargo no suelta error 