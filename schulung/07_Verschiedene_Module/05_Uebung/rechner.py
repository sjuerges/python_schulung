#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rechner für die Grundrechenarten, welcher wie folgt funktioniert:
#
# Zahl1     : 2,2
# Das war keine Zahl!!!
# Zahl1     : 2.2
# Rechenart : plus
# "plus" ist keine gültige Rechenart. Zulässig sind: +, -, *, /
# Rechenart : +
# Zahl2     : 3
# ---------------
# Ergebnis  : 5.2

import re


def zahlEinlesen(p_text, p_fehlertext, p_rechenart='', p_0FehlerText=''):
    while True:
        try:
            z = float(input(p_text))
            if p_rechenart == '/' and z == 0:
                raise RuntimeError(p_0FehlerText);
            break
        except RuntimeError as e:
            print(e)
        except:
            print(p_fehlertext)
    return z


def raPruefen(p_text, p_rechenArten, p_fehlertext):
    tmpRAList = p_rechenArten.split(',')
    tmpRAList = list(map(lambda a: re.escape(a), tmpRAList))
    # print(r'^('+(r'|'.join(tmpRAList))+r')$')
    regExp = re.compile(r'^(' + (r'|'.join(tmpRAList)) + r')$')
    while True:
        try:
            text = input(p_text)
            if not regExp.search(text):
                raise
            break
        except:
            print(p_fehlertext % (text, p_rechenArten))
    return text


fehlertextZahl = 'Das war keine Zahl!!!'
divisionDurch0Fehlertext = 'Die Division durch 0 ist nicht möglich!'
fehlertextRechenart = f'"%s" ist keine gültige Rechenart. Zulässig sind: %s'
rechenArten = '+,-,*,/,**';

### Usereingaben
zahl1 = zahlEinlesen('Zahl1     : ', fehlertextZahl)

# Rechenart prüfen: siehe Beispiele/07_Verschiedene_Module/05_Uebung
ra = raPruefen('Rechenart : ', rechenArten, fehlertextRechenart)

zahl2 = zahlEinlesen('Zahl2     : ', fehlertextZahl, ra, divisionDurch0Fehlertext)

### Rechnen
erg = str((eval(str(zahl1) + ra + str(zahl2))))

### Ausgeben
print('------------' + '-' * len(erg))
print('Ergebnis  : ' + erg)
