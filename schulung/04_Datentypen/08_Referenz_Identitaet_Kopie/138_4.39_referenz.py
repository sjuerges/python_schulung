#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Kopie einer Zahl
print("Zahl:")
x = 12.5
y = x
print("y = x gleiches Objekt:", x is y)
y = 15.8
print("y = 15.8 gleiches Objekt:", x is y)
print("y = 15.8 gleicher Inhalt:", x == y)
print()

# Kopie eines Strings
print("String:")
x = "Robinson"
y = x
print("y = x gleiches Objekt:", x is y)
y = "Freitag"
print("y = 'Freitag' gleiches Objekt:", x is y)
print("gleicher Inhalt:", x == y)
print()

# Zweite Referenz auf eine Liste
print("Liste:")
x = [23, "hallo", -7.5]
y = x
print("y = x gleiches Objekt:", x is y)
y[1] = "welt"
print("y[1] = 'welt' gleiches Objekt:", x is y)
print(x)
