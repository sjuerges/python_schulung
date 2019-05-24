#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 02_login_3_Versuche.py die for-Schleife in eine
# while-Schleife

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
aktVers = 0

while aktVers < anzVers and not loginOk:
    os.system(cl)
    print(fehlerText)

    u_lo = input('Login    : ')
    u_pw = input('Pass     : ')

    loginOk = lo == u_lo and pw == u_pw

    aktVers += 1

    fehlerText = 'Versuch ' + str(aktVers + 1) + \
                 ' von ' + str(anzVers) + ' Versuche'

os.system(cl)
if loginOk:
    print('Herzlich willkommen!')
else:
    print('Ungültige Login/Passwort Kombination!')

print()
input('Schließen mit Return')
