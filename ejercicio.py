#Laura Sanz Ruano G.ITT

#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
dicc = {}

for linea in lineas:
    elementos = linea.split(':')
    usuario = elementos[0]
    shell = elementos[-1][:-1]
    
    dicc [usuario] = shell
 
try:
    print "Root: ", dicc ["root"]
    print "Imaginario: ", dicc ["imaginario"]

except:
    print "No existe ese usuario"   

fd.close()
