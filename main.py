from flask import Flask, render_template, redirect, request, url_for,flash, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'Dani_Server';

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "",
    database = "farm_to_cell")

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

@app.route('/Informacion_Adicional')
def Pagina_De_Info_Extra():
    
    print('This is another route. :D')

    return render_template('Info_Extra.html');

@app.route('/Registro_personas', methods=['GET', 'POST'])
def Registrando_p():
        if request.method == 'POST': #si el metodo es GET si suelta error
            nombre_p = request.form.get['name']
            apellido_p = request.form.get['Lastname']
            telefono_p = request.form.get['telefono']
            correo_p = request.form.get['Email']
            direccion_p = request.form.get['Adress']
            contraseña_p = request.form.get['Password']

            # Validar que todos los campos estén llenos
            if not (nombre_p and apellido_p and telefono_p and direccion_p and correo_p and contraseña_p):
                return render_template('registrar.html', error='Por favor, complete todos los campos del formulario.')

            try:
                cursor.execute("INSERT INTO registro_personas (Nombre_persona, Apellido_person, Celular, Dirección, Email, Contraseña) VALUES (%s, %s, %s, %s, %s, %s)", 
                            (nombre_p, apellido_p, telefono_p, direccion_p, correo_p, contraseña_p))
                db.commit()
                return redirect(url_for('Registrando_p'))
            except mysql.connector.errors.IntegrityError as e:
                return render_template('registrar.html', error=str(e))
        
        return render_template('Login_Registro.html')
#Los datos no se guardan en la tabla sin embargo no suelta error 

##

# @app.route('/Registro_personas', methods=['GET', 'POST'])
# def Registrando_p():
    
#     if request.method == 'GET':
#         nombre_p = request.form.get["Name"]
#         apellido_p = request.form.get['Lastname']
#         telefono_p = request.form.get['telefono']
#         correo_p = request.form.get['Email']
#         direccion_p = request.form.get['Adress']
#         contraseña_p = request.form.get['Password']

#         cursor.execute("Insert Into registro_personas (Nombre_persona, Apellido_person, Celular, Dirección, Email, Contraseña) Values (%s, %s, %s, %s, %s, %s)", 
#                                 (nombre_p, apellido_p, telefono_p, direccion_p, correo_p, contraseña_p))
#         db.commit()
#         return redirect(url_for('Registrando_p'))
    
#     return render_template('registrar.html')