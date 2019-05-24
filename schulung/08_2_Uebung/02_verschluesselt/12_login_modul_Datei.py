#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 11_login_modul_Datei.py
# Mit Verschlüsselung
# lo_pw.txt - Passworte sind mit hashlib.sha512(bytes('123',encoding='utf-8')).hexdigest() verschlüsselt!!!

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
