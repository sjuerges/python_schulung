#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 12_login_modul.py
# User Angaben befinden sich in der logindb Tabelle usertab
# Achtung Passworte sind md5 - verschlüsselt

### Module einbinden
### #########################################################################
import os

from loKlasse import loKlasse

### Hauptprogramm
### #########################################################################

config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'logindb',
    # 'charset':'latin1',
    ### Bei Datenänderungen mit SQL für MySQL folgende Optionen setzten:
    # 'raise_on_warnings': True,
    # 'sql_mode':'strict_trans_tables,strict_all_tables'
}

objLo = loKlasse(config)

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
