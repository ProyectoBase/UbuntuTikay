#!/bin/bash
#Script para crear jaula(Chroot)
#Se crean las carpetas de trabajo
#Parámetro $1 = Ruta de Instalacion
#Se crea carpeta de trabajo
sudo mount --bind /dev/ $1/edit/dev
sudo chroot edit
mount -t proc none /proc
mount -t sysfs none /sys
mount -t devpts none /dev/pts
