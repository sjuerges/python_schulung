#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 10_login_oop.py
# privates Dictionary : lo_pw wird aus Datei gelesen

import os
import sys

from loKlasse import loKlasse

objLo = loKlasse(sys.path[0] + '/lo_pw.txt')

# help(objLo)

spaltenUeberschriften = ['Login', 'Password'];

if os.name == 'nt':
    cl = 'cls'
else:
    cl = 'clear'

# Erneutes anmelden
if objLo.loginCheck() == True:
    os.system(cl)
    print('Herzlich willkommen!', end='\n\n')
    print('User-Liste:', '-----------', '', sep='\n')
    print(objLo.loginListeSortiert(spaltenUeberschriften))
else:
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
