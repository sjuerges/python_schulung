#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Beispiel
test = "Das ist ein Beispielsatz"
print("Text:", test)

# Beginn, Ende
if test.startswith("Das"):
    print("Text beginnt mit Das")
if not test.endswith("Das"):
    print("Text endet nicht mit Das")

# Zerlegung
teile = test.partition("ei")
print("vor der 1. Teilung:", teile[0])
print("hinter der 1. Teilung:", teile[2])

teile = test.rpartition("ei")
print("vor der 2. Teilung:", teile[0])
print("hinter der 2. Teilung:", teile[2])

# Zerlegung in Liste
# ACHTUNG: die String - Funktion split() kann nicht mit
#          Regulären Ausdrücken umgehen und hat eine
#          andere Syntax als die split() - Funktion im
#          re (regular expression) - Modul
wliste = test.split()
for i in range(0, 3):
    print("Element:", i, wliste[i])
