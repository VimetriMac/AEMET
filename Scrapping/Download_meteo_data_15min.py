# -*- coding: utf-8 -*-
import urllib2
import time
from time import gmtime,strftime
from Estaciones_AEMET import estaciones

inicio = time.time()
timelog = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
fecha = strftime("20%y%m%d%H%M%S", time.localtime(time.time()))
print fecha
estaciones_sin_datos = []
#timelog = localtime = time.strftime("20%y%m%d%H%M%S", time.localtime(time.time()))
ficheroLog = file("/home/jgodoy/Documentos/Datos_bajados_scraping/Estaciones_AEMET/Log/log_"+fecha,'w')
ficheroLog.write("-----------------------------------------------------------------\n \n")
ficheroLog.write("Momento de ejecución: \n")
ficheroLog.write(timelog +"\n \n")
ficheroLog.write("-----------------------------------------------------------------\n \n")


for i in estaciones:

    archivoDescargar = "http://www.aemet.es/es/eltiempo/observacion/ultimosdatos_"+i+"_datos-horarios.csv?k=coo&l="+i+"&datos=det&w=0"

    localtime = time.strftime("20%y%m%d%H%M%S", time.localtime(time.time()))
    now = time.time();

    print "Local current time :", localtime
    archivoGuardar = i +"_"+ str(localtime)+".csv"

    try:
        descarga = urllib2.urlopen(archivoDescargar)
        ficheroGuardar = file("/home/jgodoy/Documentos/Datos_bajados_scraping/Estaciones_AEMET/"+archivoGuardar,'w')
        ficheroGuardar.write(descarga.read())
        ficheroGuardar.close()
        elapsed =time.time()-now
        print "Descargado el fichero: %s en %0.3fs \n"%(archivoDescargar,elapsed)
        ficheroLog.write("Descargado el fichero: %s en %0.3fs \n"%(archivoDescargar,elapsed))


    except urllib2.HTTPError: # Si se produce la excepción de que no se recibe respuesta por parte
                              # de la URL correspondiente se sigue la ejecución del programa "pass"
        estaciones_sin_datos.append(i)
        print "Descarga no posible para estación AEMET: "+i
        pass


final = time.time()
duracion = inicio-final

print "Proceso de descarga completada - Duración: % 0.3fs"%(duracion)
print "No se han descargado datos para las siguientes estaciones (Total: " +str(estaciones_sin_datos.__len__())+"): "+ str(estaciones_sin_datos) +"\n \n"
ficheroLog.write("\n---------------------GENERAL LOG-------------------------------- \n \n")
ficheroLog.write("Proceso de descarga completada - Duración: % 0.3fs "%(duracion))
ficheroLog.write("\n No se han descargado datos para las siguientes estaciones (Total: " +str(estaciones_sin_datos.__len__())+"): "+ str(estaciones_sin_datos))
ficheroLog.write(" \n-----------------------------------------------------------------")