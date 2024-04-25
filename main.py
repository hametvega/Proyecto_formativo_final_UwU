from flask import Flask, render_template, redirect, request, url_for,flash, session

app = Flask(__name__)
app.secret_key = 'Dani_Server';

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
