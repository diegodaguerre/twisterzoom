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
raw_line = "WIND       6.5    277"
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
    WIND = [x.strip(' ') for x in split_line]
    print "Datos WIND Procesados:"
    print WIND
    



if __name__ == "__main__":
    a = "WIND 	   6.5	  27"
    getValue(a)
  
  
"""
example: 
from get_value import getValue
getValue("WIND 6.34 234")
RAW LINE: WIND 6.34 234
"""