#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import hashlib


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
    anzVersucheText = ''
    formValue = {'lo': '', 'pw': '', 'anzVers': 0}

    ### Methoden
    ### #########################################################################
    def __init__(self, p_loPwDatei, p_formData):
        self.__lopwDatei = p_loPwDatei
        for aktFormName in p_formData:
            self.formValue[aktFormName] = p_formData[aktFormName].value
        self.formValue['anzVers'] = int(self.formValue['anzVers']) + 1
        self.formValue['anzVers'] = str(self.formValue['anzVers'])
        # print(self.formValue);

    def loginCheck(self, p_anzVersuche):
        ### Inline Documentation (Muss in """ Bla """ oder  ''' Bla ''' stehen):
        '''
            Return: True  bei Login erfolgreich
                    False bei Login nicht erfolgreich
        '''
        ### Aktuelle Daten einlesen
        self.__loPwDict = self.__leseDaten()

        loginOK = False  # Login erfolgreich = True oder nicht = False

        u_lo = self.formValue['lo']
        u_pw = self.formValue['pw']
        u_vers = int(self.formValue['anzVers'])
        if u_vers > 1:
            self.anzVersucheText = 'Versuch ' + str(u_vers) + ' von ' + str(p_anzVersuche) + ' Versuche'

        u_pw = hashlib.sha512(bytes(u_pw, encoding='utf-8')).hexdigest()

        if u_lo in self.__loPwDict and self.__loPwDict[u_lo] == u_pw and u_vers <= p_anzVersuche + 1:
            loginOK = True

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
        lopwDict = {};
        try:
            dh = open(self.__lopwDatei, 'r')
        except:
            print('Datei ' + (self.__lopwDatei) + ' kann nicht geöffnet werden!')
            sys.exit(0)
        ### ENTWEDER
        zeLoPw = dh.readline().rstrip()
        while zeLoPw:
            (*zeLo, zePw) = zeLoPw.split(':')
            if zeLo and zePw != '':
                lopwDict[':'.join(zeLo)] = zePw
            zeLoPw = dh.readline().rstrip()

        dh.close()
        return lopwDict
