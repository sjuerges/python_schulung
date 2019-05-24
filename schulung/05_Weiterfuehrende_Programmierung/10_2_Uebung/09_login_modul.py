#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 08_login_format.py
# Lagern Sie alle Funktionen in das Modul login_mod aus.

### Module einbinden
### #########################################################################
import os

import login_mod

lopwDict = {
    'Admin': '123',
    'User': 'efg',
    'paul': 'abc'
}
anzVersuche = 3  # Maximale Anzahl der Versuche

if os.name == 'nt':
    cl = 'cls'
else:
    cl = 'clear'

if login_mod.loginCheck(lopwDict, anzVersuche, cl) == True:
    os.system(cl)
    print('Herzlich willkommen!', end='\n\n')
    print('User-Liste:', '-----------', sep='\n')
    print(login_mod.loginListeSortiert(lopwDict))
    # print(lopwDict)
else:
    os.system(cl)
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
