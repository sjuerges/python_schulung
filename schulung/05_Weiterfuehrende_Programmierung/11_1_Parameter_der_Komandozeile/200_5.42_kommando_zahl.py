#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Aufruf:
# python 200_5.42_kommando_zahl.py 3 6.2

import sys

try:
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    z = x + y
    print("Ergebnis:", z)
except:
    print("Parameterfehler")
