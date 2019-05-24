#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 08_login_format.py
# Spaltenbreite soll abhänig von der Länge der Inhalte sein.
#
# Herzlich willkommen!
#
# User-Liste:
# -----------
# 
# +-------+----------+
# | Login | Password |
# +-------+----------+
# | Admin | 123      |
# | paul  | abc      |
# | User  | efg      |
# +-------+----------+

### Module einbinden
### #########################################################################
import os


### Funktionen
### #########################################################################

### Mit WHILE-Schleife für die Anzahl der Versuche:
def loginCheck(p_lopwDict, p_anzVersuche, p_cl):
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
        if u_lo in p_lopwDict and p_lopwDict[u_lo] == u_pw:
            loginOK = True
        '''
        if (u_lo, u_pw) in p_lopwDict.items():
            loginOK = True

        i += 1
        anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(p_anzVersuche) + ' Versuche'

    return loginOK


def maxLaenge(werteListe, ueberschrift):
    laengenListe = list(map(len, werteListe))
    # laengenListe=[]
    # for i in werteListe:
    #    laengenListe.append(len(i))
    laengenListe.append(len(ueberschrift))
    return max(laengenListe)


def loginListeSortiert(p_lopwDict):
    breiteSpalte1 = maxLaenge(p_lopwDict.keys(), 'login')
    breiteSpalte2 = maxLaenge(p_lopwDict.values(), 'password')

    ausgabe = ''

    trennzeile = '+' + ('-' * (breiteSpalte1 + 2) + '+') + ('-' * (breiteSpalte2 + 2) + '+') + '\n'

    ausgabe += trennzeile
    ausgabe += f'| {"Login":<{breiteSpalte1}} | {"Password":<{breiteSpalte2}} |\n'
    ausgabe += trennzeile

    # Nach Login sortiert
    ausgabe += 'Nach Login sortiert\n'
    for aktKey in sorted(p_lopwDict, key=lambda a: a.lower()):
        ausgabe += f'| {aktKey:<{breiteSpalte1}} | {p_lopwDict[aktKey]:<{breiteSpalte2}} |\n'

    ausgabe += 'Nach Passwort sortiert\n'
    # Nach Passwort sortiert  
    for aktKey in sorted(p_lopwDict, key=lambda a: p_lopwDict[a].lower()):
        ausgabe += f'| {aktKey:<{breiteSpalte1}} | {p_lopwDict[aktKey]:<{breiteSpalte2}} |\n'

    ausgabe += trennzeile

    # from tabulate import tabulate
    # print(tabulate(p_lopwDict.itemes(), headers=['Login', 'Password']))

    return ausgabe


### Hauptprogramm
### #########################################################################
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

if loginCheck(lopwDict, anzVersuche, cl) == True:
    os.system(cl)
    print('Herzlich willkommen!', end='\n\n')
    print('User-Liste:', '-----------', sep='\n')
    print(loginListeSortiert(lopwDict))
    # print(lopwDict)
else:
    os.system(cl)
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
