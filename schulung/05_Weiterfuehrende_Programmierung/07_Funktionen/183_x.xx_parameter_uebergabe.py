#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Lösung: Kopie einer Liste an Funktion übergeben

# Gleiche id -> gleiches Objektreferenz!!!

# siehe auch: http://www.python-kurs.eu/parameter.php

def sum(liste):
    print('id(liste)', id(liste))
    summe = 0
    for merke in liste:
        summe += merke
    liste[0] = 100;
    return summe


werte = [1, 2, 3, 4, 5]
print(werte)
print('id(werte)', id(werte))
print()
print('Kopie der Liste übergeben: sum(werte[:])')
print(sum(werte[:]))
print(werte)
print()
print('Referenz der Liste übergeben: sum(werte)')
print(sum(werte))
print(werte)
