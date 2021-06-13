import os
import subprocess
from subprocess import check_output

print ("Resultados de mysql.connector:")
import pymysql

miConexion = pymysql.connect( host='10.26.1.161', user= 'lisa',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()
cur.execute( """ SELECT * FROM Kardex_monitor.Conf_pos order by `Tiendas_Cod_Ncr` asc; """ )

datos = cur.fetchall()
#--nombre =input("INTRODUSCA EL NOMBRE DEL ARCHIVO : ")+".sh"
nombre = "Ejecucion_pos_Impresora.sh"
#print("El ARCHIVO SE VA ALMACENAR CON EL NOMBRE :"+nombre)
COMANDO =""" #! /bin/bash """
COMANDO=COMANDO+"""\ndate ;""" 
for shop in datos:
    IP=shop[1]
    COD_POS= shop[0]
    Clave=shop[2]
    COMANDO =COMANDO + "\nsudo sshpass  -f "+Clave+" ssh -o StrictHostKeyChecking=no root@"+IP+"""  "sum /home/reg/gd90/P_REGKEY.DAT"  > """+COD_POS+""".txt; """

COMANDO=COMANDO+"""\ndate ;""" 
archivo = open(nombre,'w')
archivo.write(COMANDO)
archivo.close()
#print(COMANDO)
miConexion.close()


