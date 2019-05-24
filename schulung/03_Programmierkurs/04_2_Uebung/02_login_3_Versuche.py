#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie die Übung 01_login.py so das der Anwender 3 Versuche hat.
# ... Uebung>02_login_3_Versuche.py

# Login    :
# Pass     :

# Versuch 2 von 3 Versuche
# Login    :
# Pass     :

# Versuch 3 von 3 Versuche
# Login    : Admin
# Pass     : 123
# Herzlich willkommen!

import os

if os.name == 'posix':
    cl = 'clear'
else:
    cl = 'cls'

lo = 'Admin'
pw = '123'
anzVers = 3
fehlerText = ''
loginOk = False

for aktVers in range(anzVers):
    os.system(cl)
    print(fehlerText)

    u_lo = input('Login    : ')
    u_pw = input('Pass     : ')

    loginOk = lo == u_lo and pw == u_pw

    if loginOk:
        break

    fehlerText = 'Versuch ' + str(aktVers + 2) + ' von ' + str(anzVers) + ' Versuche'

os.system(cl)
if loginOk:
    print('Herzlich willkommen!')
else:
    print('Ungültige Login/Passwort Kombination!')

print()
input('Schließen mit Return')
