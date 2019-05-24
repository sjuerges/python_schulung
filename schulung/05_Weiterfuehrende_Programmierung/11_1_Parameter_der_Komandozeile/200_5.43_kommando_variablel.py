#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Aufruf:
# python 200_5.43_kommando_variablel.py 3 6.2 5

import sys

summe = 0

try:
    for i in sys.argv[1:]:
        summe += float(i)
    print("Ergebnis:", summe)
except:
    print("Parameterfehler")
