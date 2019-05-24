#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Keine .pyc - Dateien f�r das eingebundene Module erstellen
# Muss im eigentlichen Programm vor der Moduleinbindung mit
# import oder from stehen!
import sys

sys.dont_write_bytecode = True

from modul_neu import quadrat

z = quadrat(3)
print(z)
