#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modul math
import math

# Trigonom. Funktionen und Konstanten
# Alle Funktionen beziehen sich auf Winkelangaben im Bogenmaß
x = 30
xbm = x / 180 * math.pi
print("Sinus  ", x, "Grad:", math.sin(xbm))
print("Cosinus", x, "Grad:", math.cos(xbm))
print("Tangens", x, "Grad:", math.tan(xbm))
