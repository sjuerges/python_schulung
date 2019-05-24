#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tname = "Robinson Crusoe"

try:
    tname[3] = "e"
except:
    print("Fehler")

try:
    tname[3:5] = "el"
except:
    print("Fehler")

tname = tname[:3] + 'el' + tname[5:]
print(tname)
