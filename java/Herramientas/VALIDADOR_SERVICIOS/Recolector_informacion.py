import mysql.connector
import os
import subprocess
from subprocess import check_output

import pymysql



miConexion = pymysql.connect( host='10.26.1.161', user= 'lisa',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()
cur.execute( """ SELECT * FROM Kardex_monitor.Tiendas order by Cod_Ncr; """ )
i=0
datos = cur.fetchall()

nombre = "00_Consulta_modelo_pos.sh"

COMANDO =""" #! /bin/bash """
for shop in datos:
    ip=shop[3]
    tienda=shop[0]
    COMANDO=COMANDO+"""\n sudo sshpass  -f NCR ssh -o StrictHostKeyChecking=no root@"""+ip+"""  "sh /home/NCRServices/ServiceStatus.sh"  > """+str(tienda)+""".txt;"""

nombre="01_Adquir_informacion_servidor.sh"  



archivo = open(nombre,"w")
archivo.write(str(COMANDO))
archivo.close()


miConexion.close()


 