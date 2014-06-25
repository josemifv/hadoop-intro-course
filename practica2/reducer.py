#!/usr/bin/python

import sys

salesTotal = 0
oldKey = None

# La clave será la tienda, y el valor el precio de la venta
# Como los datos llegan ordenados, un cambio de clave significa
# que ya no hay más ventas de la tienda anterior

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

if oldKey != None:
    print oldKey, "\t", salesTotal