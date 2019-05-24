#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 04_login_funktion.py
# Es sollen sich mehrere User anmelden können:
# Admin -> 123
# User  -> 456
# Paul  -> abc
# Benutzen Sie eine 2 Dimensionale Liste

### Module einbinden
### #########################################################################
import os


### Funktionen
### #########################################################################

### Mit WHILE-Schleife für die Anzahl der Versuche:
def loginCheck(p_lopwListe, p_anzVersuche, p_cl):
    ### Inline Documentation (Muss in """ Bla """ oder  ''' Bla ''' stehen):
    '''
        Return: True  bei Login erfolgreich
                False bei Login nicht erfolgreich
    '''

    loginOK = False  # Login erfolgreich = True oder nicht = False
    anzVersucheText = ''  # Anzahl der Versuche Text (1. Aufruf kein Text)
    i = 0  # Anzahl der Versuche Zähler

    while i < p_anzVersuche and not loginOK:
        os.system(p_cl)
        print(anzVersucheText)

        u_lo = input('Login    : ')
        u_pw = input('Pass     : ')

        '''
        for aktLoPw in p_lopwListe:
            #print(aktLoPw)
            if aktLoPw[0] == u_lo and aktLoPw[1] == u_pw:
                loginOK = True
                break
        '''
        if [u_lo, u_pw] in p_lopwListe:
            loginOK = True

        i += 1
        anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(p_anzVersuche) + ' Versuche'

    return loginOK


### Hauptprogramm
### #########################################################################
lopwListe = [
    ['Admin', '123'],
    ['User', '456'],
    ['Paul', 'abc']
]
anzVersuche = 3  # Maximale Anzahl der Versuche

if os.name == 'nt':
    cl = 'cls'
else:
    cl = 'clear'

if loginCheck(lopwListe, anzVersuche, cl) == True:
    print('Herzlich willkommen!')
else:
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
