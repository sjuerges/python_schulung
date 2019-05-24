#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 06_login_Liste_anzeigen_sort.py
# Verwenden Sie nun ein Dictionary
#
# Herzlich willkommen!
# User-Liste:
# -----------
# Admin:123
# Paul:abc
# User:456

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


def loginListeSortiert(p_lopwDict):
    ausgabe = ''

    # Nach Login sortiert 
    for aktKey in sorted(p_lopwDict, key=lambda a: a.lower()):
        ausgabe += aktKey + ':' + p_lopwDict[aktKey] + '\n'

    ausgabe += '\n'
    # Nach Passwort sortiert  
    for aktKey in sorted(p_lopwDict, key=lambda a: p_lopwDict[a].lower(), reverse=True):
        ausgabe += aktKey + ':' + p_lopwDict[aktKey] + '\n'

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
