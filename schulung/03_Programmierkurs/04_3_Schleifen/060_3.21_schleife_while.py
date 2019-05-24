#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Modul importieren
import random

# Zufallsgenerator initialisieren
random.seed()

# Initialisierung
summe = 0

# while-Schleife
while summe < 30:
    # Zufallswert von 1 bis 8 erzeugen
    zzahl = random.randint(1, 8)
    summe = summe + zzahl
    print("Zahl:", zzahl, "Zwischensumme:", summe)

print("Ende")
