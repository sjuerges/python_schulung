#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# mehrdimensionale Liste, unterschiedliche Objekte
x = [
    ["Paris", "Fr", 3500000],
    ["Rom", "It", 4200000]
]
print(x)

# Teilliste
print(x[0])

# einzelne Elemente
print(x[0][0], "hat", x[0][2], "Einwohner")
print(x[1][0], "hat", x[1][2], "Einwohner")

# Teile von Elementen
print(x[0][1][0:1])

### Listen komplett verarbeiten:
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j])

for landListe in x:
    for wert in landListe:
        print(wert)
