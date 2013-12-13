#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Esta función se encarga de convertir información que envía la estación
metereogica en una linea a un diccionario.

De esto:
WIND 	   6.5	  277

A esto:
['WIND',6.5,277]

Pablo: Estuve probando con los datos tal cual los copiamos en una consola python y encontré que hay que usar tabuladores debido a esto: 
import re
raw_line = "WIND 	   6.5	  277"
>>> raw_line
'WIND \t   6.5\t  277'

Entonces probando: 
>>> print re.split(r'\t', raw_line)
['WIND ', '   6.5', '  277']

Quitando los espacios:
split_line = re.split(r'\t', raw_line)
>>> WIND = [x.strip(' ') for x in split_line]
>>> WIND
Tuve problemas con el print

"""
import re


def getValue(raw_line):
    print "Datos raw: " + raw_line
    split_line = re.split(r'\t', raw_line)
    print "Datos split: "
    print split_line
    #Compruebo que tipo de datos son si es WIND o PTU utilizando la variable con datos sin procesar raw_line
    tipoWIND = re.match(r'WIND.*(\d+)\.(\d+).*(\d+)$', raw_line)
    if tipoWIND:
        WIND = [x.strip(' ') for x in split_line]
        print "Datos WIND Encontrados:"
        print WIND
    tipoPTU = re.match(r'.*PTU.*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+)$', raw_line)
    if tipoPTU:
        PTU = [x.strip(' ') for x in split_line]
        print "Datos PTU Encontrados:", PTU
    tipoPTU2 = re.match(r'(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+)', raw_line)
    if tipoPTU2:
        PTU2 = [x.strip(' ') for x in split_line]
        print "Datos PTU2 Encontrados:", PTU2
"""
Estas líneas todavía no funcionan y parece que no se precisa la línea 3, la dejo comentada para seguir probando. 
Tengo que agregar algo para que los datos PTU3 no tome lo mismo que aparece en PTU2
        tipoPTU3 = re.match(r'.*(\d+).*(\d+).*(\d+)(\x03\r\n)', raw_line)
    if tipoPTU3:
        PTU3 = [x.strip(' ') for x in split_line]
        print "Datos PTU3 Encontrados:", PTU3
"""    



if __name__ == "__main__":
# Datos WIND de prueba:
    #a = "WIND 	   6.5	  27"
# Datos PTU de prueba:
    #a = "\x01PTU\x02\t23.5  \t23.9  \t22.8  \t70  \t75  \t69  \t17.9  \t18.4  \t17.4  \t1"
# Datos PTU2 de prueba (linea2):
    #a = "006.2\t1007.1\t1006.1\t225  \t495  \t142  \t0.0   \t0.0   \t0.0   \t0.0  "
# Datos PTU3 de prueba (linea3): 
    #a = " \t0.0   \t0.0   \t0.0   \t\x03\r\n"
    getValue(a)
  
  
"""
example: 
from get_value import getValue
getValue("WIND 6.34 234")
RAW LINE: WIND 6.34 234
Agregados datos de salida PTU:
Received '\x01PTU\x02\t23.5  \t23.9  \t22.8  \t70  \t75  \t69  \t17.9  \t18.4  \t17.4  \t1'
match: r'.*PTU.*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*(\d+).*$'
Received '006.2\t1007.1\t1006.1\t225  \t495  \t142  \t0.0   \t0.0   \t0.0   \t0.0  '
Received ' \t0.0   \t0.0   \t0.0   \t\x03\r\n'
"""