#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Sollen Strings oder Numbers über die Funktion
# manipuliert werden, geht dies nur über die Rückgabewerte

# Sortierfunktion
def sortieren(eins, zwei):
    if eins < zwei:
        return zwei, eins
    else:
        return eins, zwei


# Beispiel 1
x = 24
y = 29
x, y = sortieren(x, y)
print("x =", x, "y =", y)

# Beispiel 2
x = 124
y = 29
x, y = sortieren(x, y)
print("x =", x, "y =", y)
