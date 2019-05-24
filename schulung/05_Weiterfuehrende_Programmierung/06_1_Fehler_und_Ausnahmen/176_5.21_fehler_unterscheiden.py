#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HINWEIS: Der Name der Exception steht im Fehlermeldungstext:
# Test mit abc ->
# ...\170_5.18_fehler_unterscheiden.py", line 8, in <module>
#     zahl = float(input("Eine positive Zahl: "))
# ValueError: could not convert string to float: 'abc'
# ---------- !!!

# Liste der Built-In-Exceptions
# http://docs.python.org/3.6/library/exceptions.html#concrete-exceptions

# Wiederholte Eingabe
fehler = True
while fehler:
    try:
        zahl = float(input("Eine positive Zahl: "))
        if zahl == 0:
            raise RuntimeError("Zahl gleich 0")
        if zahl < 0:
            raise RuntimeError("Zahl zu klein")
        kw = 1.0 / zahl
        fehler = False
    # except ValueError:
    #    print("Fehler: keine Zahl") # Bei Eingabe von: abc
    except ZeroDivisionError:
        print("Fehler: Zahl 0 eingegeben")  # Bei Eingabe von: 0
    except RuntimeError as e:
        print("Fehler:", e)

# Ausgabe
print("Der Kehrwert von", zahl, "ist", kw)
