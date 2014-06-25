#!/usr/bin/python

# Para cada linea el formato es:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab
# Nos interesan los elementos 2 (tienda) y 4 (precio)
# Los resultados se escriben por la salida estandar, separados por un tabulador
import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    # Defensive code: Nos aseguramos que la línea contienen el número de campos adecuado
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print '%s\t%s' % (tienda, cost)