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
    DirectorioTrabajo="Trabajo"

#Realizadas las comprobaciones de rigor, se sigue con la ejecución de los scripts de creacion.
#Se ejecutan scripts Bash, pensando en la reimplementación del Software para distintas distros.
#En el caso de que se quiera utilizar para otra distro, simplemente se deben modificar lo que se desee en el script bash y no este archivo.

#PASO 1 -Extracción de la ISO-
print "PASO 1 -Extracción de la ISO-"
print "A continuación se extraerá la ISO en la carpeta de trabajo."
print "La operación puede demorar unos minutos."
raw_input ("-Presione una tecla para continuar..-")
