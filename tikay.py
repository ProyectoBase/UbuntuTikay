#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
##SCRIPT PARA GENERAR REMASTERS DE UNA DISTRIBUCION UBUNTU##
#Sintaxis: tikay.py ArchivoISO[OBLIGATORIO] NombreDistro[OBLIGATORIO] DirectorioTrabajo[OBLIGATORIO]
#Prerrequisitos
#--------------
#Para la correcta ejecución el Script es obligatorio tener instalado el siguiente software adicional
#-squashfs-tools
#-genisoimage
#-chroot

#Se toman los parámetros de comando y se agregan excepciones en el caso de que no especifique un parametro obligatorio
try:
    ArchivoISO= sys.argv[1] # Nombre del archivo ISO. Formato: archivo.iso [OBLIGATORIO]
except IndexError:
    print "No se especifica archivo ISO para trabajar"
    sys.exit(0)

try:
    NombreDistro= sys.argv[2] # Nombre de la Distro. Formato: "Nombre que quieras" [OBLIGATORIO]
except IndexError:
    print "No se especifica nombre de la Distro"
    sys.exit(0)

try:
    DirectorioTrabajo=sys.argv[3] #Directorio de Trabajo(DOnde se descomprimira el ISO). Por defecto: "CarpetaActual/trabajo [OPCIONAL]
except:
    DirectorioTrabajo="trabajo"

#Realizadas las comprobaciones de rigor, se sigue con la ejecución de los scripts de creacion.
#Se ejecutan scripts Bash, pensando en la reimplementación del Software para distintas distros.
#En el caso de que se quiera utilizar para otra distro, simplemente se deben modificar lo que se desee en el script bash y no este archivo.

#PASO 1 -EXTRACCIÓN DE LA ISO-
print "PASO 1 -Extracción de la ISO-"
print "A continuación se extraerá la ISO en la carpeta de trabajo."
print "Se le solicitará su contraseña de administrador."
print "La operación puede demorar unos minutos."
raw_input ("-Presione [ENTRAR] para continuar..-")

#PASO 2 -CREACIÓN DE LA JAULA-
print ""
print "PASO 2 -Creación de la Jaula"
print "A continuación se creará la jaula(chroot) para poder trabajar sobre la distro"
print "Tikay puede generar la jaula automáticamente y abrir un terminal(xterm por defecto)"
print "Sin embargo usted puede enjaular desde otro terminal, mediante la herramienta enjaular.py sobre el directorio de trabajo"
print "¿Qué desea hacer?"
print "1=Abrir terminal por defecto en una nueva ventana"
print "2=Enjaular desde otro terminal con enjaular.py"

while True:
    eleccion=raw_input("Opción: ")

    if eleccion=="1":
        #Escribir instrucciones para abrir otro terminal
        raw_input ("Una vez que haya terminado de customizar la distro, presione [ENTRAR] para continuar...")
        break
    if eleccion=="2":
        print "Para enjaular desde otra terminal escribir ejecutar enjaular [directoriodetrabajo]"
        raw_input ("Una vez que haya terminado de customizar la distro, presione [ENTRAR] para continuar...")
        break

#PASO 3 -PREPROCESO DE CREACION DE LA IMAGEN .ISO
print ""
print "PASO 3 -Preproceso de creación de imagen.ISO"
print "Antes de terminar es necesario actualizar los datos de booteo"
raw_input("Presione [ENTRAR] tecla para continuar...")

#PASO 4 -CREACIÓN DE IMAGEN ISO
print ""
print "PASO 4 -Creación de la imagen "+ NombreDistro+".iso"
print "Para finalizar se generará la imagen ISO de tu distro"
print "Este proceso puede llevar varios minutos."
raw_input("Presione [ENTRAR] tecla para continuar...")

print ""
print "----------------------------------------"
print "¡SE FINALIZO LA CREACIÓN DE LA DISTRO!"
print "----------------------------------------"
