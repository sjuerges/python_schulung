#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
import hashlib
import os


### Klasse erstellen
### #########################################################################
class loKlasse:
    '''
        Eine Klasse f�r eine Login Funktionalit�t
    '''

    ### Eigenschaften
    ### #########################################################################
    __anzVersuche = 3
    __loPwDict = {}
    __loginOK = False  # Login erfolgreich = True oder nicht = False
    __lopwDatei = ''

    if os.name == 'nt':
        __cl = 'cls'
    else:
        __cl = 'clear'

    ### Methoden
    ### #########################################################################
    def __init__(self, p_loPwDatei):
        self.__lopwDatei = p_loPwDatei
        self.__loPwDict = self.__leseDaten()

    def __leseDaten(self):
        lopwDict = {};
        try:
            dh = open(self.__lopwDatei, 'r')
        except:
            print('Datei ' + (self.__lopwDatei) + ' kann nicht ge�ffnet werden!')
            sys.exit(0)

        zeLoPw = dh.readline().rstrip()
        while zeLoPw:
            (*zeLo, zePw) = zeLoPw.split(':')
            if zeLo and zePw != '':
                lopwDict[':'.join(zeLo)] = zePw
            zeLoPw = dh.readline().rstrip()

        dh.close()
        return lopwDict

    def loginCheck(self):
        ### Inline Documentation (Muss in """ Bla """ oder  ''' Bla ''' stehen):
        '''
            Return: True  bei Login erfolgreich
                    False bei Login nicht erfolgreich
        '''
        anzVersucheText = ''  # Anzahl der Versuche Text (1. Aufruf kein Text)
        i = 0  # Anzahl der Versuche Z�hler

        while i < self.__anzVersuche and not self.__loginOK:
            os.system(self.__cl)
            print(anzVersucheText)

            u_lo = input('Login	: ')
            u_pw = input('Pass	: ')

            u_pw = hashlib.sha512(bytes(u_pw, encoding='utf-8')).hexdigest()

            if u_lo in self.__loPwDict and self.__loPwDict[u_lo] == u_pw:
                self.__loginOK = True
                break

            i += 1
            anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(self.__anzVersuche) + ' Versuche'

        return self.__loginOK

    def loginListeSortiert(self, p_spaltenUeberschriftenRef):
        '''
            Gibt eine formatierte Liste aller Logins mit Passwort nach Login sortiert zur�ck.
        '''
        if not self.__loginOK:
            return 'Sie sind nicht angemeldet'

        ### Kopie von der Liste spaltenUeberschriften aus dem Hauptprogramm erstellen
        p_spaltenUeberschriften = copy.deepcopy(p_spaltenUeberschriftenRef)

        breiteSpalte1 = self.__maxLaenge(self.__loPwDict.keys(), p_spaltenUeberschriften[0])
        breiteSpalte2 = self.__maxLaenge(self.__loPwDict.values(), p_spaltenUeberschriften[1])

        ausgabe = ''
        trennzeile = '+' + ('-' * (breiteSpalte1 + 2) + '+') + ('-' * (breiteSpalte2 + 2) + '+') + '\n'
        ausgabe += trennzeile
        ausgabe += f'| {p_spaltenUeberschriften[0]:{breiteSpalte1}} | {p_spaltenUeberschriften[1]:{breiteSpalte2}} |\n'
        ausgabe += trennzeile
        for aktKey in sorted(self.__loPwDict, key=lambda a: a[0].lower()):
            ausgabe += f'| {aktKey:{breiteSpalte1}} | {self.__loPwDict[aktKey]:{breiteSpalte2}} |\n'
        ausgabe += trennzeile
        return ausgabe

    def __maxLaenge(self, werteListe, ueberschrift):
        laengenListe = list(map(lambda a: len(a), werteListe))
        laengenListe.append(len(ueberschrift))
        return max(laengenListe)
