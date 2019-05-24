#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy
import os

import mysql.connector


class loKlasse:
    '''
        Eine Klasse für eine Login Funktionalität
    '''

    ### Eigenschaften
    ### #########################################################################
    __loginOK = False
    __dbConnectData = {}
    __dbVerb = ''

    ### Methoden
    ### #########################################################################
    def __init__(self, p_dbConnectData):
        self.__dbConnectData = p_dbConnectData

    def __del__(self):
        if self.__dbVerb:
            self.__dbVerb.close()

    def __dbConnect(self):
        self.__dbVerb = mysql.connector.connect(**self.__dbConnectData)

    def __dbClose(self):
        self.__dbVerb.close()

    def loginCheck(self, p_anzVersuche, p_cl):
        ### Inline Documentation (Muss in """ Bla """ oder  ''' Bla ''' stehen):
        '''
            Return: True  bei Login erfolgreich
                    False bei Login nicht erfolgreich
        '''

        loginOK = False  # Login erfolgreich = True oder nicht = False
        anzVersucheText = ''  # Anzahl der Versuche Text (1. Aufruf kein Text)
        i = 0  # Anzahl der Versuche Zähler
        select = '''SELECT count(*) anz
                             FROM usertab 
                             WHERE login = %(login)s
                               and pass = md5(%(pass)s)'''
        self.__dbConnect()
        erg = self.__dbVerb.cursor(dictionary=True)

        while i < p_anzVersuche and not loginOK:
            os.system(p_cl)
            print(anzVersucheText)

            u_lo = input('Login    : ')
            # u_pw = getpass('Pass     : ')
            u_pw = input('Pass     : ')

            erg.execute(select, {'login': u_lo, 'pass': u_pw})

            datensatz = erg.fetchone()

            try:
                if datensatz[b'anz'] == 1:
                    loginOK = True
                    break
            except:
                if datensatz['anz'] == 1:
                    loginOK = True
                    break

            i += 1
            anzVersucheText = 'Versuch ' + str(i + 1) + ' von ' + str(p_anzVersuche) + ' Versuche'

        self.__loginOK = loginOK
        self.__dbClose()
        return loginOK

    def zeigeLogins(self, p_spaltenUeberschriftenRef):
        '''
            Alle Logins mit Passworten nach Login sortiert ausgeben.
        '''
        if not self.__loginOK:
            return 'Sie sind nicht angemeldet'

        ### Kopie von der Liste spaltenUeberschriften aus dem Hauptprogramm erstellen
        p_spaltenUeberschriften = copy.deepcopy(p_spaltenUeberschriftenRef)

        self.__dbConnect()

        select = '''SELECT max(length(login)) loginLen,
                                    max(length(pass)) passLen
                             FROM usertab'''
        erg = self.__dbVerb.cursor(dictionary=True)
        erg.execute(select)
        datensatz = erg.fetchone()

        maxLoginLen = datensatz['loginLen']
        maxPassLen = datensatz['passLen']

        select = '''SELECT login, pass
                             FROM usertab
                             ORDER BY login ASC'''

        ausgabe = ''
        fmDaten = '| {0:' + str(maxLoginLen) + 's} | {1:' + str(maxPassLen) + 's} |\n'
        trennzeile = '+' + ('-' * (maxLoginLen + 2) + '+') + ('-' * (maxPassLen + 2) + '+') + '\n'
        ausgabe += trennzeile
        ausgabe += fmDaten.format(p_spaltenUeberschriften[0], p_spaltenUeberschriften[1])
        ausgabe += trennzeile

        erg.execute(select)

        datensatz = erg.fetchone()
        while datensatz:
            try:
                ausgabe += fmDaten.format(datensatz[b'login'].decode('cp1252'), datensatz['pass'])
            except:
                # ausgabe += fmDaten.format(datensatz['login'], datensatz['pass'])
                ### ODER ab Python 3.6
                ausgabe += f'| {datensatz["login"]:{maxLoginLen}} | {datensatz["pass"]:{maxPassLen}} |\n'
            datensatz = erg.fetchone()
        ausgabe += trennzeile
        self.__dbClose()
        return ausgabe
