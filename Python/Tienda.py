#ESTE ES EL MODELO
from app import mysql


def select_all():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Tienda where abierta =1;")
    #cur.execute("SELECT * FROM Tienda ;")
    data = cur.fetchall()
    #print(data)
    return data

def buscar_nombre_tienda(variable):
     cur = mysql.connection.cursor()
     alfa=variable
     sentens = ('SELECT * FROM TIENDAS.Tienda where Tienda.NOMBRE like"%'+alfa+'%";')
     cur.execute(sentens)
     data = cur.fetchall()
     return data
 
def listar_tiendas():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Tienda ;")
    datas = cur.fetchall()
    return datas

def listar_offline():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM TIENDAS.Tienda where abierta =1 and estado !='ONLINE';""")
    datas_2 = cur.fetchall()
    return datas_2

def agregar_tienda(CODIGONCR, NOMBRETIENDA, CODIGOSAP, IPSERVER, IPPC, IPCAMARAS, ABIERT, ESTAD):
    cur = mysql.connection.cursor()
    print(CODIGONCR, NOMBRETIENDA, CODIGOSAP, IPSERVER, IPPC, IPCAMARAS, ABIERT, ESTAD)
    cur.execute('INSERT INTO TIENDAS.Tienda (Cod_ncr, NOMBRE, CODIGO_SAP, IP_SERVER, IP_PC, IP_CAMARAS, Abierta, Estado) VALUES(%s, %s, %s, %s, %s, %s, %s, %s ); ',
                    (CODIGONCR, NOMBRETIENDA, CODIGOSAP, IPSERVER, IPPC, IPCAMARAS, ABIERT, ESTAD))
    mysql.connection.commit()
    
def actualizar_tienda(IPSERVER, IPPC, IPCAMARAS, ABIERT, ESTAD, CODIGONCR):
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE TIENDAS.Tienda
            SET IP_SERVER = %s, 
            IP_PC =  %s, 
            IP_CAMARAS=  %s, 
            Abierta =  %s, 
            Estado =  %s 
        WHERE (Cod_ncr = %s);       
        """, (IPSERVER, IPPC, IPCAMARAS, ABIERT, ESTAD, CODIGONCR))
    mysql.connection.commit()



def mostrar_tienda(CODNCR):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM Tienda where Cod_ncr ={0}'.format(CODNCR))
    dat = cur.fetchall()
    return dat
def eliminar_tienda(CODNCR):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM TIENDAS.Tienda WHERE (`Cod_ncr` = {0});'.format(CODNCR))
    mysql.connection.commit()
