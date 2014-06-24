#!/usr/bin/env python

import sys

# Lectura de datos de la entrada estándar
for line in sys.stdin:
    # Eliminamos espacios en blanco al comienzo y al final
    line = line.strip()
    # Partimos la línea en palabras
    words = line.split()
    # Incrementamos los contadores
    for word in words:
        # Escritura de los datos por la salida estándar
        # La salida del mapper será la entrada del reducer
        # En esta versión se separan clave y valor por un tabulador
        print '%s\t%s' % (word, 1)