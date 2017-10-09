# -*- coding: utf-8 -*-
#horario UTC
import urllib2
import time

from time import gmtime,strftime

hora_local_str = strftime("20%y%m%d%H00", time.localtime(time.time()))
hora_local = time.localtime(time.time())
hora_local_log = strftime("%a, %d %b %Y %H:%M:%S", hora_local)
hora_UTC = time.gmtime()
hora_UTC_str = strftime("20%y%m%d%H00", hora_UTC)
hora_UTC_log =strftime("%a, %d %b %Y %H:%M:%S", hora_UTC)
print hora_UTC
print hora_UTC_str
print hora_UTC_log
ficheroLog = file("/home/jgodoy/Documentos/Datos_bajados_scraping/Rayos_AEMET/Log/log",'a')
URL_descarga = "http://www.aemet.es/imagenes_d/eltiempo/observacion/rayos/"+hora_UTC_str+"_r78g.gif"
print(URL_descarga)

try:
    descarga = urllib2.urlopen(URL_descarga)
    ficheroDescargado = file("/home/jgodoy/Documentos/Datos_bajados_scraping/Rayos_AEMET/"+hora_UTC_str+".gif",'w')
    ficheroDescargado.write(descarga.read())
    ficheroDescargado.close()
    ficheroLog.seek(2)
    ficheroLog.write("-----------------------------------------------------------------\n \n")
    ficheroLog.write("Archivo Descargado: \n")
    ficheroLog.write("Hora Local: "+ hora_local_log)
    ficheroLog.write("\nHora UTC: "+ hora_UTC_log)
    ficheroLog.write("\n-----------------------------------------------------------------\n \n")
    ficheroLog.close()

except urllib2.HTTPError:
    print "Archivo no descargado - HTTPError"
    ficheroLog.seek(2)
    ficheroLog.write("-----------------------------------------------------------------\n \n")
    ficheroLog.write("ERROR - Archivo no descargado - HTTPError: \n")
    ficheroLog.write("Hora Local: " + hora_local_log)
    ficheroLog.write("\nHora UTC: " + hora_UTC_log)
    ficheroLog.write("\n-----------------------------------------------------------------\n \n")
    ficheroLog.close()



