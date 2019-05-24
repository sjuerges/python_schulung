#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import hashlib
import os
import xml.etree.ElementTree as ET


class loKlasse:
    '''
        Eine Klasse für eine Login Funktionalität
    '''

    ### Eigenschaften
    ### #########################################################################
    __loPwDict = {
        'admin': 'pass'
    }
    __loginOK = False
    __lopwDatei = ''

    ### Methoden
    ### #########################################################################
    def __init__(self, p_loPwDatei):
        self.__lopwDatei = p_loPwDatei

    def loginCheck(self, p_anzVersuche, p_cl):
        ### Inline Documentation (Muss in """ Bla """ oder  ''' Bla ''' stehen):
        '''
            Return: True  bei Login erfolgreich
                    False bei Login nicht erfolgreich
        '''
        ### Aktuelle Daten einlesen
        self.__loPwDict = self.__leseDaten()

        loginOK = False  # Login erfolgreich = True oder nicht = False
        anzVersucheText = ''  # Anzahl der Versuche Text (1. Aufruf kein Text)
        i = 0  # Anzahl der Versuche Zähler

        while i < p_anzVersuche and not loginOK:
            os.system(p_cl)
            print(anzVersucheText)

            u_lo = input('Login    : ')
            u_pw = input('Pass     : ')

            u_pw = hashlib.sha512(bytes(u_pw, encoding='utf-8')).hexdigest()

            if u_lo in self.__loPwDict and self.__loPwDict[u_lo] == u_pw:
                loginOK = True
                break

            i += 1
            anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(p_anzVersuche) + ' Versuche'

        self.__loginOK = loginOK
        return loginOK

    def zeigeLogins(self, p_spaltenUeberschriftenRef):
        '''
            Alle Logins mit Passworten nach Login sortiert ausgeben.
        '''
        if not self.__loginOK:
            return 'Sie sind nicht angemeldet'

        ### Kopie von der Liste spaltenUeberschriften aus dem Hauptprogramm erstellen
        p_spaltenUeberschriften = copy.deepcopy(p_spaltenUeberschriftenRef)

        ### Aktuelle Daten einlesen
        self.__loPwDict = self.__leseDaten()

        ### Spaltenbreiten aus Dictionary Daten ermitteln
        # Keys
        keyLenListe = map(lambda x: len(x), self.__loPwDict.keys());
        maxKeyLen = max(keyLenListe)
        if maxKeyLen < len(p_spaltenUeberschriften[0]):
            maxKeyLen = len(p_spaltenUeberschriften[0])
        # Values
        valLenListe = map(lambda x: len(x), self.__loPwDict.values());
        maxValLen = max(valLenListe)
        if maxValLen < len(p_spaltenUeberschriften[1]):
            maxValLen = len(p_spaltenUeberschriften[1])

        ausgabe = ''
        fmDaten = '| {0:' + str(maxKeyLen) + 's} | {1:' + str(maxValLen) + 's} |\n'
        trennzeile = '+' + ('-' * (maxKeyLen + 2) + '+') + ('-' * (maxValLen + 2) + '+') + '\n'
        ausgabe += trennzeile
        ausgabe += fmDaten.format(p_spaltenUeberschriften[0], p_spaltenUeberschriften[1])
        ausgabe += trennzeile

        for aktKey in sorted(self.__loPwDict):
            ausgabe += fmDaten.format(aktKey, self.__loPwDict[aktKey])
        ausgabe += trennzeile

        return ausgabe

    def __leseDaten(self):
        lopwDict = {}
        tree = ET.parse(self.__lopwDatei)
        ### Ref auf root Element (<users>) holen
        root = tree.getroot()
        ### Alle Kinder des root Elements (<users>) durchlaufen
        for child in root:
            if (  # Kind Element Name wirklich <user>
                    child.tag == 'user'
                    and
                    # Attribut login vorhanden und nicht Leer
                    'login' in child.attrib and child.attrib['login'] != ''
                    and
                    # Attribut pass vorhanden und nicht Leer
                    'pass' in child.attrib and child.attrib['pass'] != ''
            ):
                # Eintrag in lopwDict hinzufügen
                lopwDict[child.attrib['login']] = child.attrib['pass']
        ### tree löschen nicht vergessen!
        del tree
        return lopwDict
