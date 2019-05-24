#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode


### Funktionen
### #########################################################################
def loginCheck(u_lo, u_pw, p_config, p_anzVersuche):
    loginOK = False  # Login erfolgreich = True oder nicht = False
    anzVersucheText = ''  # Anzahl der Versuche Text (1. Aufruf kein Text)
    i = 0  # Anzahl der Versuche Zähler

    if pruefeUser(u_lo, u_pw, p_config):
        loginOK = True

    return loginOK


def loginListeSortiert(p_config, p_spaltenBreiteRef=30):
    ausgabe = ''
    try:
        verb = mysql.connector.connect(
            **p_config
        )

        ### Abfrage
        sql = ('''SELECT login ,pass
                    FROM usertab
                    ORDER BY login ASC''')

        erg = verb.cursor()
        erg.execute(sql)
        fmDaten = '| {0:' + str(p_spaltenBreiteRef) + 's} | {1:' + str(p_spaltenBreiteRef) + 's} |\n'
        trennzeile = '+' + ('-' * (p_spaltenBreiteRef + 2) + '+') * 2 + '\n'
        ausgabe += trennzeile
        ausgabe += fmDaten.format('Login', 'Password')
        ausgabe += trennzeile
        for (lo, pw) in erg:
            ausgabe += fmDaten.format(lo.decode("utf-8"), pw)
        ausgabe += trennzeile
        return ausgabe

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ungültige Login/Passwort Kombination!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Datenbank nicht vorhanden")
        elif err.errno == 1146:
            print("Tabelle nicht vorhanden")
        else:
            print(err)
    verb.close()
    return ausgabe


def pruefeUser(p_u_lo, p_u_pw, p_config):
    userOK = False
    try:
        verb = mysql.connector.connect(
            **p_config
        )

        ### Abfrage
        sql = ('''SELECT count(*) anz
                    FROM usertab
                    WHERE binary login = %(login)s and pass = md5(%(pass)s)''')

        erg = verb.cursor()
        erg.execute(sql, {'login': p_u_lo, 'pass': p_u_pw})

        (userOK,) = erg.fetchone();
        print(userOK)

        erg.close()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Ungültige Login/Passwort Kombination!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Datenbank nicht vorhanden")
        elif err.errno == 1146:
            print("Tabelle nicht vorhanden")
        else:
            print(err)

    verb.close()
    return userOK
