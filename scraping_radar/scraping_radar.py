# -*- coding: utf-8 -*-
#horario UTC
#SE DEBE EJECUTAR A LAS XX:55 CADA DIA (P.J.: 13:55)
import urllib2
import time

from time import gmtime,strftime

hora_local_str = strftime("20%y%m%d%H00", time.localtime(time.time()))
hora_local = time.localtime(time.time())
hora_local_log = strftime("%a, %d %b %Y %H:%M:%S", hora_local)

hora_UTC = time.gmtime()
hora_UTC_str = strftime("20%y%m%d%H", hora_UTC)
hora_UTC_log =strftime("%a, %d %b %Y %H:%M:%S", hora_UTC)

print hora_UTC
print hora_UTC_str
print hora_UTC_log

ficheroLog = file("/home/jgodoy/Documentos/Datos_bajados_scraping/Radar_AEMET/Log/log",'a')
#fechaprueba = "2017100612"

minutos = [00,10,20,30,40,50]

for i in minutos:
    if i==0:
        URL_descarga = "http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/"+hora_UTC_str+ "0" + str(i)+"_r8ca.gif"
        print URL_descarga
    else:
        URL_descarga = "http://www.aemet.es/imagenes_d/eltiempo/observacion/radar/" +hora_UTC_str+ str(i) + "_r8ca.gif"
        print URL_descarga

    try:
        descarga = urllib2.urlopen(URL_descarga)
        if i == 0:
            ficheroDescargado = file("/home/jgodoy/Documentos/Datos_bajados_scraping/Radar_AEMET/" + hora_UTC_str +"0"+str(i)+".gif", 'w')
            ficheroDescargado.write(descarga.read())
        else:

            ficheroDescargado = file("/home/jgodoy/Documentos/Datos_bajados_scraping/Radar_AEMET/"+hora_UTC_str+str(i)+".gif",'w')
            ficheroDescargado.write(descarga.read())


        ficheroLog.write("-----------------------------------------------------------------\n \n")
        ficheroLog.write("Archivo Descargado: \n")
        ficheroLog.write("Hora Local: " + hora_local_log)
        ficheroLog.write("\nHora UTC: " + hora_UTC_log)
        ficheroLog.write("\n-----------------------------------------------------------------\n \n")


    except urllib2.HTTPError:
        print "Archivo no descargado - HTTPError"
        ficheroLog.seek(2)
        ficheroLog.write("-----------------------------------------------------------------\n \n")
        ficheroLog.write("ERROR - Archivo no descargado - HTTPError: \n")
        ficheroLog.write("Hora Local: " + hora_local_log)
        ficheroLog.write("\nHora UTC: " + hora_UTC_log)



