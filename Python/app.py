#ESTE ES EL CONTROLADOR
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

import Tienda 
app = Flask(__name__)


#Conexion Mysql
app.config['MYSQL_HOST'] = '10.26.1.161'
app.config['MYSQL_USER'] = 'lisa'
app.config['MYSQL_PASSWORD'] = 'Linux-1234'
app.config['MYSQL_DB'] = 'TIENDAS'
mysql = MySQL(app)

#Configurar sesion
app.secret_key = "mysecretkey"

#RUTA PRINCIPAL, INDEX O PAGINA DE INICIO
@app.route('/')
def index():
    data=Tienda.select_all()
    return render_template('index.html', shops=data)

#CARGUE DE LA PAGINA DE LOGIN DE ADMINISTRACION 
@app.route('/login')
def login():
    return render_template('login.html')


#VISTA RETORNANDO BUSQUEDA
@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        buscar = request.form['Buscador']
        data=Tienda.buscar_nombre_tienda(buscar) 
    return render_template('Search.html', shops=data)

#INDEX PARA ADMINISTRADOR  O PAGIANA DE ADMINISTRACION
@app.route('/index_admin',  methods=['POST'])
def index_admin():
    if request.method == 'POST':
        usuario = request.form['user']
        password = request.form['pass']
        print("usuario : " + usuario)
        print("clave : " + password)
        if (usuario == "Homero" and password == "Linux-2020"):
            data = Tienda.listar_tiendas()
            data_2=Tienda.listar_offline()
            menssanges = 'Ingreso Autorizado'
            flash(menssanges)
            return render_template('index_admin.html', shops=data, offlines=data_2)
        else:
            menssanges = 'Ingreso Incorrecto, Intente Nuevamente'
            flash(menssanges)
            return redirect(url_for('login'))

#MENU DE CREACION DE TIENDA NUEVA
@app.route('/add_shop', methods=['POST'])
def add_shop():
    if request.method == 'POST':
        CODIGO_NCR = request.form['CODIGO_NCR']
        NOMBRE_TIENDA = request.form['NOMBRE_TIENDA']
        CODIGO_SAP = request.form['CODIGO_SAP']
        IP_SERVER = request.form['IP_SERVER']
        IP_PC = request.form['IP_PC']
        IP_CAMARAS = request.form['IP_CAMARAS']
        ESTADO = request.form['ESTADO']
        ABIERTA = request.form['ABIERTA']
        Tienda.agregar_tienda(CODIGO_NCR, NOMBRE_TIENDA, CODIGO_SAP, IP_SERVER, IP_PC, IP_CAMARAS, ABIERTA, ESTADO)
        menssanges = 'Store Added Satisfactorily'
        flash(menssanges)
    return redirect(url_for('index'))

#RETORNO DE BUSQUEDA DE TIENDA Y MENU DE EDICION
@app.route('/update_shop/<string:CODIGO_NCR>', methods=['POST'])
def update_shop(CODIGO_NCR):
    if request.method == 'POST':
        IP_SERVER = request.form['IP_SERVER']
        IP_PC = request.form['IP_PC']
        IP_CAMARAS = request.form['IP_CAMARAS']
        ESTADO = request.form['ESTADO']
        ABIERTA = request.form['ABIERTA']
        Tienda.actualizar_tienda(IP_SERVER, IP_PC, IP_CAMARAS, ABIERTA, ESTADO, CODIGO_NCR)
        menssanges = 'Store Update Satisfactorily'
        flash(menssanges)
        return redirect(url_for('index'))

#ACTUALIZACION DE TIENSA SOLO PERMITE IP Y ESTADO
@app.route('/edit_shop/<string:CODIGO_NCR>')
def get_shop(CODIGO_NCR):
    data = Tienda.mostrar_tienda(CODIGO_NCR)
    print(data[0])
    menssanges = 'Store found Satisfactorily'
    flash(menssanges)
    return render_template('edit-shop.html', shop=data[0])

#ELIMINAR TIENDA 
@app.route('/delete_shop/<string:CODIGO_NCR>')
def delete_shop(CODIGO_NCR):
    Tienda.eliminar_tienda(CODIGO_NCR)
    menssanges = 'Store Removed Satisfactorily'
    flash(menssanges)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0", debug=True)
    #app.run(port=3030, host="0.0.0.0", debug=True)
#host="0.0.0.0"
