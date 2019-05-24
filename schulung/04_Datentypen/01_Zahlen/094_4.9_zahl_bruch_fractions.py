#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Bei der Funktion Fraction() handelt es sich um den 
# Konstruktor der Klasse fractions

# Import des Moduls
import fractions
import math

# Bruch
z = 12
n = 28
print("Bruch:", z, "/", n)

# als Fraction
b1 = fractions.Fraction(z, n)
print("Fraction:", b1)  # Ist automatisch gekürzt!!!
print("Z, N:", b1.numerator, b1.denominator)
wert = b1.numerator / b1.denominator
print("Wert:", wert)
print()

# Umrechnen
x = 2.375
print("Zahl:", x)
b2 = fractions.Fraction(x)
print("Fraction:", b2)
print()

# ggT
print("Bruch:", z, "/", n)
print("ggT:", math.gcd(z, n))  # größter gemeinsamer Teiler - 12/28 -> 4
