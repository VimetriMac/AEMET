#!/usr/bin/env python
# -*- coding: utf-8

import os
import MySQLdb
import _mysql_exceptions

# Variable para la ruta al directorio
path = '/home/jgodoy/Documentos/Datos_bajados_scraping/Rayos_AEMET/'


# Lista vacia para incluir las fechas de los ficheros
lstFechas =[]

# Lista con todos los ficheros del directorio:
lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros

# Crea una lista de los ficheros gif que existen en el directorio y los incluye a la lista.

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if (extension == ".gif"):
            lstFechas.append(nombreFichero)


print(lstFechas)
print ('LISTADO FINALIZADO')
print "longitud de la lista = ", len(lstFechas)

#Se abre conexión con la base de datos
mydb = MySQLdb.connect(host = 'localhost', user = "root", passwd ='lab202', db='rayos_aemet')

cursor = mydb.cursor()

for i in lstFechas:
    nombre = i
    #print nombre
    fecha = i
    fecha = str(i)
    a,b,c,d,e,f,g,h,i,j,k,l = fecha
    #print a,b,c,d,e,f,g,h,i,j,k,l
    #print fecha
    #fecha_str = g+h+"/"+e+f+"/"+a+b+c+d+ " "+ i+j+":"+k+l
    fecha_str = a+b+c+d+"/"+e+f+"/"+g+h+ " "+ i+j+":"+k+l
    print fecha_str
    #query = "INSERT INTO rayos_aemet VALUES('" + fecha_str+"'"+", '/home/jgodoy/Documents/Rayos_AEMET/"+nombre+".gif');"
    try:
        query = "INSERT INTO rayos_aemet VALUES('" + fecha_str + "'" + ", '/home/jgodoy/Documentos/Datos_bajados_scraping/Rayos_AEMET/" + nombre + ".gif');"
        print query
        cursor.execute(query)
    except _mysql_exceptions.IntegrityError: # si se va a meter un dato duplicado no se mete pero no se para la ejecución del programa
        print "Dato repetido - No se registrará dicho dato"
        pass



mydb.commit()
cursor.close()


#mv *.gif /home/jgodoy/Documents/Rayos_AEMET/
