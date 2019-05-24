#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standardmäßig sucht Python das Modul in folgenden
# Verzeichnissen:
# import sys
# print(sys.path)
# sys.path kann in jeden Script geändert werden:
# import sys
# sys.path=['C:\\']
# VORSICHT: Besser wäre ein Einfügen des eigenen Pfades am
#           Anfang der Liste!!!

import modul_neu as mn

z = mn.quadrat(3)
print(z)
