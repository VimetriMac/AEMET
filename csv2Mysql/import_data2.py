#!/usr/bin/python
import MySQLdb
import csv

mydb = MySQLdb.connect(host ='localhost', user = "root", passwd = 'lab202',db = 'aemet_new')

cursor = mydb.cursor()
csvarchivo = open('/home/jgodoy/Escritorio/nuevaEstacion.csv')
entrada = csv.reader(csvarchivo)

codigo, nombre, latitud, longitud, altura = next(entrada)


print(codigo,nombre,latitud,longitud,altura)

print codigo
csvarchivo.close()

Query = """ LOAD DATA LOCAL INFILE '/home/jgodoy/Escritorio/nuevaEstacion.csv' INTO TABLE Estaciones FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"' ESCAPED BY '"' Lines terminated by '\n' IGNORE 0 LINES """

Query_crear_tablas = "CREATE TABLE " + codigo +"(Time datetime not null PRIMARY KEY,Temperatura float NULL,WV float NULL,Wdir varchar(50) NULL,WRacha float NULL,WDirRacha varchar(50) NULL,Precipitacion float NULL,Presion float NULL,Tendencia float NULL,Humedad float NULL)";
#print(Query_crear_tablas)


cursor.execute(Query)
cursor.execute(Query_crear_tablas)
mydb.commit()
cursor.close()

#se obtiene el numero de lineas (estaciones bases en el fichero)
#lineas = len(csvarchivo.readlines())
#print ("numero de lineas: ")
#print (lineas)
#csvarchivo.close() #Necesario cerrar el fichero

#csvarchivo = open('/home/jgodoy/Escritorio/nuevaEstacion.csv')

#Codigo, nombre, latitud, longitud, altura = next(entrada)
#print(codigo,nombre,latitud,longitud,altura)
#print codigo

#for row in csvarchivo:
    #csvarchivo = open('/home/jgodoy/Escritorio/nuevaEstacion.csv')
    #entrada = csv.reader(csvarchivo)
    #codigo, nombre, latitud, longitud, altura = next(entrada)
    #print(codigo,nombre,latitud,longitud,altura)
    #print codigo

#csvarchivo.close() #Necesario cerrar el fichero
