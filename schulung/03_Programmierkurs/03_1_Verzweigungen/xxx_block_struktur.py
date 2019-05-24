#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Anfang und Ende von if elif und else wird durch die 
# Einrückung bestimmt!!!
# Dies gilt auch für Schleifen, Funktionen ...

# ### WICHTIG:
# Die Einrückungen eines Blocks müssen exakt aus den
# gleichen Zeichen (Art und Anzahl) bestehen!
# Sonst Fehler: 
# IndentationError: unindent does not match any outer 
# indentation level

# Test 1 mit 12
# Test 2 mit -12

x = 12
# x = -12
print("x:", x)

if x > 0:
    print("Diese Zahl ist positiv")
# print('Falsch')
else:
    print("Diese Zahl ist 0")
    print("oder negativ")

print('ENDE');
