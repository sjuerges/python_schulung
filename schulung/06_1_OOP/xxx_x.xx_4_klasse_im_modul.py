#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Statische Methode können über den Klassennamen aufgerufen
# werden.

import sys

# Beachten Sie die lustige Pfadangabe
# r - vor dem ' sollte eigentlich dafür sorgen das \ nicht als
# Escape- zeichen interpretiert wird. Dies klapt auch fast.
# Nur leider für die Kombination \' am Ende der Zeichenkette # nicht! Deshalb nur dort \\!!!
sys.path.append(r'module')

from klassen import statischeM

statischeM.meine()
try:
    statischeM.deine()
except:
    print('deine() ist keine statische Methode!')

t = statischeM()
t.deine();
