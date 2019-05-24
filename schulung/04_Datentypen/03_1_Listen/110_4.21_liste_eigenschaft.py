#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Liste von Zahlen
z = [3, 6, 12.5, -8, 5.5]
print(z)  # gesamte Liste
print(z[0])  # ein Element
print(z[0:3])  # Slice

# Liste von Zeichenketten
s = ["Hamburg", "Augsburg", "Berlin"]
print(s)

# Anzahl Elemente
print("Anzahl:", len(s))

# Liste komplett verarbeiten
for i in range(len(s)):
    print(s[i])

for wert in s:
    print(wert)
