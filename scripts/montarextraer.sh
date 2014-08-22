#!/bin/bash
#Script para extraer y montar la imagen a modificar
#Se crean las carpetas de trabajo
#Parámetro $1 = ArchivoISO
#Parámetro $2 = Ruta de Instalacion
#Se crea carpeta de trabajo
mkdir $2
#Se crea carpeta mnt
mkdir $2/mnt
#Se crea carpeta extract-cd
mkdir $2/extract-cd

#Se crea la carpeta edit
mkdir $2/edit

#Se monta la ISO en modo loop sobre mnt
sudo mount -o loop $1 $2/mnt

#Se extrae el contenido de la ISO en la carpeta de trabajo
sudo rsync --exclude=/casper/filesystem.squashfs -a $2/mnt/ $2/extract-cd

#Se extrae el sistema de escritorio en $2/edit
sudo unsquashfs $2/mnt/casper/filesystem.squashfs
sudo mv squashfs-root $2/edit

