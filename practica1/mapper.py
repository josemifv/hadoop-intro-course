#!/usr/bin/env python

import sys

# Lectura de datos de la entrada estandar
for line in sys.stdin:
    # Eliminamos espacios en blanco al comienzo y al final
    line = line.strip()
    # Partimos la linea en palabras
    words = line.split()
    # Incrementamos los contadores
    for word in words:
        # Escritura de los datos por la salida estandar
        # La salida del mapper sera la entrada del reducer
        # En esta version se separan clave y valor por un tabulador
        print '%s\t%s' % (word, 1)