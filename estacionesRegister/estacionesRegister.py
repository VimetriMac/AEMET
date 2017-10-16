import MySQLdb
import os
import _mysql_exceptions



# Variable para la ruta al directorio
path = '/home/jgodoy/Documentos/Datos_bajados_scraping/Estaciones_AEMET/'

# Lista vacia para incluir los ficheros
lstFiles = []

#Lista para almacenar los nombres de las estaciones
estaciones = []

# Lista con todos los ficheros del directorio:
lstDir = os.walk(path)  # os.walk()Lista directorios y ficheros

# Crea una lista de los ficheros jpg que existen en el directorio y los incluye a la lista.

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if (extension == ".csv"):
            lstFiles.append(nombreFichero + extension)
            # print (nombreFichero+extension)

print(lstFiles)
print ('LISTADO FINALIZADO')
print "longitud de la lista = ", len(lstFiles)

mydb = MySQLdb.connect(host = 'localhost', user="root", passwd='lab202', db='aemet_new1')
cursor = mydb.cursor()

for i in lstFiles:
    fichero = i
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,y = i
    nombre_estacion = a+b+c+d+e
    nombre_estacion_min = nombre_estacion.lower()
    print nombre_estacion_min
    #print nombre_estacion

    try:
        comillas = '"'
        salto = "\r\n"

        print comillas
        #query = "LOAD DATA LOCAL INFILE '"+path+fichero+" INTO TABLE "+str(nombre_estacion_min)+" FIELDS TERMINATED BY ',' ENCLOSED BY '"+comillas+"' ESCAPED BY '' LINES TERMINATED BY '\+"n" IGNORE 4 LINES (@Time, Temperatura, WV, Wdir, WRacha, WDirRacha, Precipitacion, Presion, Tendencia, Humedad) SET time = STR_TO_DATE(@Time, '%d/%m/%Y %H%i%s');"
        #query =  "LOAD DATA LOCAL INFILE "+"'"+path+fichero+"'"+" INTO TABLE "+str(nombre_estacion_min)+" FIELDS TERMINATED BY ',' ENCLOSED BY '""" "ESCAPED BY '' LINES TERMINATED BY '\r\n' IGNORE 4 LINES (@Time, Temperatura, WV, Wdir, WRacha, WDirRacha, Precipitacion, Presion, Tendencia, Humedad) SET time = STR_TO_DATE(@Time,'%d/%m/%Y %H:%i:s');"
        query1 = "LOAD DATA LOCAL INFILE "+"'"+path+fichero+"'"+" INTO TABLE "+str(nombre_estacion_min)+" FIELDS TERMINATED BY ',' ENCLOSED BY'"+comillas+"'ESCAPED BY '' LINES TERMINATED BY '\r\n' IGNORE 4 LINES (@Time, Temperatura, WV, Wdir, WRacha, WDirRacha, Precipitacion, Presion, Tendencia, Humedad) SET time = STR_TO_DATE(@Time,'%d/%m/%Y %H:%i:s');"
        print query1
        cursor.execute(query1)
    except _mysql_exceptions:
        print "Dato repetido - No se registrara dicho dato"
        pass

mydb.commit()
cursor.close()


