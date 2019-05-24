#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 11_login_modul_Datei.py
# mit Verschlüsselung
# lo_pw.txt - Passworte sind mit hashlib.sha512(bytes('123',encoding='utf-8')).hexdigest() verschlüsselt!!!

### Module einbinden
### #########################################################################
import os

from loKlasse import loKlasse

### Hauptprogramm
### #########################################################################

objLo = loKlasse(os.path.dirname(__file__) + '/lo_pw.xml')

# help(objLo)

anzVersuche = 3  # Maximale Anzahl der Versuche
spaltenUeberschriften = ['Login', 'Password'];

if os.name == 'nt':
    cl = 'cls'
else:
    cl = 'clear'

# print(objLo.zeigeLogins(spaltenUeberschriften, 10))

if objLo.loginCheck(anzVersuche, cl) == True:
    os.system(cl)
    print('Herzlich willkommen!', end='\n\n')
    print('User-Liste:', '-----------', sep='\n')
    print(objLo.zeigeLogins(spaltenUeberschriften))
else:
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
