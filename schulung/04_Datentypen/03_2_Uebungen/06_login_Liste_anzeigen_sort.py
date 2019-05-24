#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 05_login_Listen.py
# Nach der erfolgreichen Anmeldung sollen alle 
# Logins + Passworte aufsteigend nach Login sortiert
# angezeigt werden.
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
def loginCheck(p_lopwListe: list, p_anzVersuche: int, p_cl: str) -> bool:
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

        for aktLoPw in p_lopwListe:
            if aktLoPw[0] == u_lo and aktLoPw[1] == u_pw:
                loginOK = True
                break

        i += 1
        anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(p_anzVersuche) + ' Versuche'

    return loginOK


def loginListeSortiert(p_lopwListe):
    '''
        Gibt die übergebene Liste:
        [
            ['Admin','123'],
            ....
        ]
        sortiert nach Index[x][0] zurück:
        Admin: 123
    '''
    ausgabe = ''
    '''
    # sort() manipuliert das Original:
    p_lopwListe=copy.deepcopy(p_lopwListe)
    p_lopwListe.sort(key=lambda a : a[0].lower());
    
    for aktLoPw in p_lopwListe:
        lo, pw = aktLoPw
        ausgabe+=lo+':'+pw+'\n'
  
    '''
    # sorted() gibt eine neue sortierte Liste zur�ck:
    listeSortiert = sorted(p_lopwListe, key=lambda a: a[0].lower());

    for aktLoPw in listeSortiert:
        lo, pw = aktLoPw
        ausgabe += lo + ':' + pw + '\n'

    return ausgabe


### Hauptprogramm
### #########################################################################
lopwListe = [
    ['Admin', '123'],
    ['User', '456'],
    ['paul', 'abc']
]
anzVersuche = 3  # Maximale Anzahl der Versuche

if os.name == 'nt':
    cl = 'cls'
else:
    cl = 'clear'

# help(loginListeSortiert)

if loginCheck(lopwListe, anzVersuche, cl) == True:
    os.system(cl)
    print('Herzlich willkommen!', end='\n\n')
    print('User-Liste:', '-----------', sep='\n')
    print(loginListeSortiert(lopwListe))
    # print(lopwListe)
else:
    os.system(cl)
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
