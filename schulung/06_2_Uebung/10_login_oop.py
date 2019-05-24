#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ändern Sie in der Übung 09_login_modul.py
# Erstellen Sie eine Klasse loKlasse mit folgenden Eigenschaften
# und Methoden:
# Eigenschaft         : anzVersuche = 3
# Dictionary          : lo_pw = {'admin':'pass'}
#                       Welches über eine setLo_Pw mit einen neuen Dictionary
#                       überschrieben werden darf.
# Methode             : setLo_Pw()
# Methode             : loginCheck()
# Methode             : loPwDictloPwDict loginListeSortiert() 
#                       Welche nur nach erfolgreichen login funktionieren darf!!!

import copy
### Module einbinden
### #########################################################################
import os


### Klasse erstellen
### #########################################################################
class loKlasse:
    '''
        Eine Klasse für eine Login Funktionalität
    '''

    ### Eigenschaften
    ### #########################################################################
    __loPwDict = {
        'admin': 'pass'
    }
    __loginOK = False  # Login erfolgreich = True oder nicht = False

    ### Methoden
    ### #########################################################################

    def loginCheck(self, p_anzVersuche, p_cl):
        ### Inline Documentation (Muss in """ Bla """ oder  ''' Bla ''' stehen):
        '''
            Return: True  bei Login erfolgreich
                    False bei Login nicht erfolgreich
        '''
        anzVersucheText = ''  # Anzahl der Versuche Text (1. Aufruf kein Text)
        i = 0  # Anzahl der Versuche Zähler

        while i < p_anzVersuche and not self.__loginOK:
            os.system(p_cl)
            print(anzVersucheText)

            u_lo = input('Login	: ')
            u_pw = input('Pass	: ')

            if u_lo in self.__loPwDict and self.__loPwDict[u_lo] == u_pw:
                self.__loginOK = True
                break

            i += 1
            anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(p_anzVersuche) + ' Versuche'

        return self.__loginOK

    def loginListeSortiert(self, p_spaltenUeberschriftenRef, p_spaltenBreiteRef=30):
        '''
            Gibt eine formatierte Liste aller Logins mit Passwort nach Login sortiert zurück.
        '''
        if not self.__loginOK:
            return 'Sie sind nicht angemeldet'

        ### Kopie von der Liste spaltenUeberschriften aus dem Hauptprogramm erstellen
        p_spaltenUeberschriften = copy.deepcopy(p_spaltenUeberschriftenRef)

        ausgabe = ''
        trennzeile = '+' + ('-' * (p_spaltenBreiteRef + 2) + '+') * 2 + '\n'
        ausgabe += trennzeile
        ausgabe += f'| {p_spaltenUeberschriften[0]:{p_spaltenBreiteRef}} | {p_spaltenUeberschriften[1]:{p_spaltenBreiteRef}} |\n'
        ausgabe += trennzeile
        for aktKey in sorted(self.__loPwDict, key=lambda a: a[0].lower()):
            ausgabe += f'| {aktKey:{p_spaltenBreiteRef}} | {self.__loPwDict[aktKey]:{p_spaltenBreiteRef}} |\n'
        ausgabe += trennzeile
        return ausgabe

    def setLo_Pw(self, p_loPwDict):
        '''loPwDict
            Erwartet ein Login-Passwort Dictionary mit folgender Struktur:

            p_loPwDict ={
                'login':'pass'
                [,...]
            }
        '''
        if not self.__loginOK:
            print('Sie sind nicht angemeldet')
            exit()

        if type(p_loPwDict).__name__ == 'dict' and p_loPwDict:
            self.__loPwDict = p_loPwDict
            self.__loginOK = False
        else:
            print('Bitte ein Dictionary als Parameter �bergeben.')
            exit()


### Hauptprogramm
### #########################################################################


loPwDict = {
    'Admin': '123',
    'User': '456',
    'paul': 'abc'
}

objLo = loKlasse()

# help(objLo)

# (loPwDict)

anzVersuche = 3  # Maximale Anzahl der Versuche
spaltenUeberschriften = ['Login', 'Password']

if os.name == 'nt':
    cl = 'cls'
else:
    cl = 'clear'

print(objLo.loginListeSortiert(spaltenUeberschriften, 10))

### Mit Initial - User und Pass anmelden
if objLo.loginCheck(anzVersuche, cl) == True:
    ### Neue Login - Daten �bergeben
    objLo.setLo_Pw(loPwDict)
    os.system(cl)
    print('Sie wurden abgemeldet. Bitte mit den neuen Daten Anmelden.')
    if objLo.loginCheck(anzVersuche, cl) == True:
        print('Herzlich willkommen!', end='\n\n')
        print('User-Liste:', '-----------', '', sep='\n')
        print(objLo.loginListeSortiert(spaltenUeberschriften, 10))
    else:
        print('Ungültige Login/Passwort Kombination!')
else:
    print('Ungültige Login/Passwort Kombination!')

input('\nSchließen mit Return')
