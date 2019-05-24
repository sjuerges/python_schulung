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
# sys.path.insert(0,'./module')
# print(sys.path)

import modul_neu

z = modul_neu.quadrat(3)
print(z)
