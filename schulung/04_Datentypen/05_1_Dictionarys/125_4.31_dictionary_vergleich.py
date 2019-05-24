#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Zwei Dictionarys
alter1 = {"Julia": 28, "Peter": 30}
alter2 = {"Peter": 30, "Julia": 28}

# Vergleich
if alter1 == alter2:
    print("Gleich")

# <, > ging noch unter Python2 aber mit ungewissen Ausgang!!
try:
    if alter1 < alter2:
        print("1 < 2")
    else:
        print("nicht 1 < 2")
except:
    print("Fehler")
