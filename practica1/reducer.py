#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

# Lectura de datos de la entrada estandar
for line in sys.stdin:
    # Eliminamos espacios en blanco al comienzo y al final
    line = line.strip()

    # Parseamos la salida del mapper.py
    word, count = line.split('\t', 1)

    # Convertimos el numero de ocurrencias a entero
    try:
        count = int(count)
    except ValueError:
        # Error al convertir a entero
        # Se descarta la linea silenciosamente
        continue

    # Este IF funciona porque Hadoop ejecuta la etapa de SORT
    # Ordena las entradas al reducer por clave
    if current_word == word:
        current_count += count
    else:
        # Hack para controlar el caso de la primera linea
        if current_word:
            # Escritura de los datos por la salida estándar
            print '%s\t%s' % (current_word, current_count)
        current_count = count
        current_word = word

# ¡No hay que olvidar la ultima entrada!
if current_word == word:
    print '%s\t%s' % (current_word, current_count)