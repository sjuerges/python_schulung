#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 03_login_3_Versuche_while.py.
# Sie soll nun eine loginCheck-Funktion bekommen.
# Die Übergabeparameter sollen das Gültige Login + Passwort
# sowie die Anzahl der Versuche sein.
# Bei erfolgreichen Login soll die Funktion 1 ansonsten 0
# zurückgeben.

### Module einbinden
### #########################################################################
import os


### Funktionen
### #########################################################################
def loginCheck(p_lo, p_pw, p_anzVersuche, p_cl):
    loginOK = False  # Login erfolgreich = True oder nicht = False
    anzVersucheText = ''  # Anzahl der Versuche Text (1. Aufruf kein Text)
    i = 0  # Anzahl der Versuche Zähler

    while i < p_anzVersuche and not loginOK:
        os.system(p_cl)
        print(anzVersucheText)

        u_lo = input('Login    : ')
        u_pw = input('Pass     : ')

        loginOK = p_lo == u_lo and p_pw == u_pw

        i += 1
        anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(p_anzVersuche) + ' Versuche'

    return loginOK


### Hauptprogramm
### #########################################################################
lo = 'Admin'  # Login Vorgabe
pw = '123'  # Passwort Vorgabe
anzVersuche = 3  # Maximale Anzahl der Versuche

if os.name == 'nt':
    cl = 'cls'
else:
    cl = 'clear'

os.system(cl)

if loginCheck(lo, pw, anzVersuche, cl) == True:
    print('Herzlich willkommen!')
else:
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
