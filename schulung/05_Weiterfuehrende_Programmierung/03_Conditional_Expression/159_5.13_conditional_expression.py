#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = -12
y = 15

if x > y:
    max = x
else:
    max = y
# Ausdruck zur Zuweisung
max = x if x > y else y
print(max)

# Ausdruck zur Ausgabe
print("positiv" if x > 0 else "negativ oder 0")
