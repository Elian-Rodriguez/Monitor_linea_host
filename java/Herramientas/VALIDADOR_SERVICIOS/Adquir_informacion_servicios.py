import os
import subprocess
from subprocess import check_output

print ("Resultados de mysql.connector:")
import pymysql

miConexion = pymysql.connect( host='10.26.1.161', user= 'lisa',port=3306, passwd='Linux-1234', db='Kardex_monitor' )
cur = miConexion.cursor()
cur.execute( """ SELECT * FROM Kardex_monitor.Tiendas order by Cod_Ncr; """ )

datos = cur.fetchall()
#--nombre =input("INTRODUSCA EL NOMBRE DEL ARCHIVO : ")+".sh"
#nombre = "Ejecucion_pos_serial.sh"
#print("El ARCHIVO SE VA ALMACENAR CON EL NOMBRE :"+nombre)
COMANDO =""" #! /bin/bash """
for shop in datos:
    Comando = "IP ES IGUAL A "+shop[3]+ "COFIGO NCR CORRESPONDE A "+ shop[0]
    print(Comando)
      #  COMANDO =COMANDO + "\nsudo sshpass  -f "+shop[2]+" ssh -o StrictHostKeyChecking=no root@"+shop[1]+"""  "sudo dmidecode -s system-serial-number"  > /home/despliegues-bogota/BOGOTA/RESULTADO_INDIVIDUAL/"""+shop[0]+""".txt; """

#COMANDO=COMANDO+adicionar  
#archivo = open(nombre,'w')
#archivo.write(COMANDO)
#archivo.close()
 
miConexion.close()

