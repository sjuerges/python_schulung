#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Konstanten gibt es nicht in Python
# Können aber simuliert werden

def PI():
    return 3.14


# Durch Funktionen
print('PI() ->', PI())
# PI()=10 # Kann nicht schief gehen :)

# Durch Benahmungsregeln (Konstanten komplett groß schreiben)
KONSTPI = 3.14
print('KONSTPI ->', KONSTPI)
KONSTPI = 10  # Kann schief gehen!!! :(
print('KONSTPI ->', KONSTPI)
