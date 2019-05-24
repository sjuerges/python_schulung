#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ## Ausgabe
# #######################################################################
print('# Ausgabe')
print('Hallo', 'Leute')
print('Hallo' + 'Leute')
print('Hallo' 'Leute')
print('Hallo', 'Leute', sep='')
print('Hallo', 'Leute', sep='***', end='$$$')
print('Test')

# ## Daten Einlesen
# #######################################################################
print('\n# Daten Einlesen')
userEingabe = 'paul'
# userEingabe = input('Name: ')

print(userEingabe)

# Fallunterscheidungen
# #######################################################################
print('\n# Fallunterscheidungen')

if userEingabe == 'paula':
    print('sehr gut')
elif userEingabe == 'paul':
    print('gut')
else:
    print('mangelhaft')

# ## Schleifen
# #######################################################################
print('\n# Schleifen')

# FOR mit Liste
for aktWert in 1, 7, 2:
    print('# FOR mit Liste:', aktWert)

# FOR mit range()
for i in range(10, 15, 1):
    print('FOR mit range():', i)

# WHILE
while i < 20:
    print('WHILE:', i)
    i += 1

# DO WHILE
while True:
    print('"DO"-WHILE:', i)
    i += 1
    if i > 20:
        break

# ## Listen
# #######################################################################
print('\n# Listen')

# Liste erstellen
liste = [50, 51, 52]
# del liste[1]
print('liste: ', liste)

# Liste durchlaufen
for listenWert in liste:
    print('Liste nur Werte:', listenWert)

print()
for aktIndex in range(len(liste)):
    print('Liste Index und Werte:', aktIndex, ':', liste[aktIndex])

# Liste Mehrdimensional
print('\n# Liste Mehrdimensional')


def noneTest():
    pass


liste = [
    ['hallo', userEingabe],
    ['Guten Morgen'],
    10,
    1.5,
    noneTest(),
    True
]

for listenWert in liste:
    '''
    if (
        type(listenWert).__name__=='str'
        or
        type(listenWert).__name__=='int'
        or
        type(listenWert).__name__=='float'
        or
        type(listenWert).__name__=='NoneType'
        or
        type(listenWert).__name__=='bool'
    ):
    '''
    if type(listenWert).__name__ in ['str', 'int', 'float', 'NoneType', 'bool']:
        print('', listenWert)
    else:
        for wert in listenWert:
            print('', wert)

# Liste entpacken
print('# Liste entpacken')
erstes, *rest, letztes = liste
print(erstes, rest, letztes, sep='\n')

# ACHTUNG listenRef enthält eine Referenz auf 			
listenRef = liste
listenRef[0] = 'Über Referenz var liste geändert'
# Original wurde geändert:
print(liste)

# Formatierte Ausgabe von mehrdimensionalen Strukturen
import json

print(bytes(json.dumps(liste, indent=4), 'utf-8').decode('unicode_escape'))

# ## Dictionary
# #######################################################################
print('\n# Dictionary')

woerterbuch = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value3',
}

# del woerterbuch['key1']
print('woerterbuch: ', woerterbuch, end='\n\n')
# Eintrag hinzufügen
woerterbuch['Key1'] = 'Value1'
print('woerterbuch: ', woerterbuch, end='\n\n')

# Dictionary durchlaufen
for aktKey in woerterbuch:
    print(' Dictionary Key + Values:', aktKey, woerterbuch[aktKey])

# Dictionary Views
keyView = woerterbuch.keys()
valueView = woerterbuch.values()
itemView = woerterbuch.items()

print('', keyView, valueView, itemView, sep='\n ')

# Suche nach Key
if 'key1' in keyView:
    print('\nkey1 gefunden')
if 'key1' in woerterbuch:
    print('\nkey1 gefunden')

# Suche nach Value
if 'value1' in valueView:
    print('\nvalue1 gefunden')

# Suche nach Item	
if ('key1', 'value1') in itemView:
    print('\nkey1 mit value1 gefunden')

print()
for aktWert in keyView:
    print(' keyView in FOR: ', aktWert)

print()
for aktWert in itemView:
    print(' itemView in FOR: ', aktWert)

# ## SET - Liste mit eindeutigen Werten
# #########################################################################
print('\n# SET')

setName1 = set([1, 2, 2, 2, 3])
setName2 = set([1, 5, 2])

print('\nSets: ', setName1, setName2, '\n')

print('Vereinigungsmenge: ', setName1 | setName2)
print('Schnittmenge     : ', setName1 & setName2)
print('Diffmenge        : ', setName1 - setName2)
print('Diffmenge        : ', setName2 - setName1)
print('Sym. Diffmenge   : ', setName2 ^ setName1)

setName1 = set([1, 2, 3])
setName2 = set([1, 2])

print('\nSets: ', setName1, setName2, '\n')

print('echte Teilmenge  : ', setName2 < setName1)
print('Teilmenge        : ', setName2 <= setName1)

# ## Funktionen
# #########################################################################
print('\n# Funktionen')


# Funktion erstellen
def funktName(a, b=3, e=5, *liste):
    print(' In der Funktion:', a, b, e, liste)
    c = a + b + e
    for i in liste:
        c += i
    return c, c


# Funktion aufrufen (ausführen)
print(' funktName(1)             :', funktName(1), '\n')
print(' funktName(1, 2)          :', funktName(1, 2), '\n')
print(' funktName(1, 2, 3)       :', funktName(1, 2, 3), '\n')
print(' funktName(1, 2, 3, 4, 5) :', funktName(1, 2, 3, 4, 5), '\n')
print(' funktName(1, e=10)       :', funktName(1, e=10), '\n')


# Funktion mit Type Hints
def funktName(a: int, b: float) -> float:
    '''
        Das ist keine besonders gute Hilfe
    '''
    return a * b


print(funktName(2, 3))
# Gibt beim call der Funktion keinen Error:
# print(funktName('a','b'))

# Hilfe zur Funktion anzeigen
help(funktName)

# ## Lambda-Funktion - anonyme Funktion
# #########################################################################
print('\n# Lambda-Funktion')
funkVariable = lambda a: a * 2

print(funkVariable(2))

lopwDict = {
    'User': 'efg',
    'Admin': '123',
    'paul': 'abc'
}

for (login, passw) in sorted(lopwDict.items(), key=lambda a: a[1]):
    print('Lambda-Funktion:', login, ':', passw)

# ## Formatierte Ausgaben
# #########################################################################
print('\n# Formatierte Ausgaben')
datenListe = ['Guten Tag', 'Kay Stromberg']

# ab Python 3.6
xml = f'''
	<root>
		<gruss>{datenListe[0]}</gruss>
		<autor>{datenListe[1]}</autor>
	</root>
'''
print(xml)

# ab Python 3.1
xml = '''
	<root>
		<gruss>{0}</gruss>
		<autor>{1}</autor>
	</root>
'''.format(datenListe[0], datenListe[1])
print(xml)

# ab Python 2
xml = '''
	<root>
		<gruss>%s</gruss>
		<autor>%s</autor>
	</root>
''' % (datenListe[0], datenListe[1])
print(xml)

# ## Fehlerbehandlung
# #########################################################################
print('\n# Fehlerbehandlung')

try:
    10 / 0
except:
    print('Alle Fehler behandeln')

# Liste der Built-In-Exceptions
# http://docs.python.org/3.6/library/exceptions.html#concrete-exceptions


try:
    # 10+'20'
    10 / 0
except ZeroDivisionError:
    print('ZeroDivisionError')
except TypeError:
    print('TypeError')
except:
    print('Alle Fehler behandeln')
finally:
    print('Das passiert immer')

# Benutzerdefinierte Errors
try:
    raise RuntimeError('Mein Fehler')
except RuntimeError as fehlertext:
    print(fehlertext)
except:
    print('Alle Fehler behandeln')

# ## Module sind normale Python Dateien (mod_name_1.py)
# #######################################################################
print('\n# Module')

import sys
import os

sys.path.insert(0, os.path.dirname(__file__) + '/module')

import mod_name_1

mod_name_1.funkt_name_1()

import mod_name_2 as m2

m2.funkt_name_2()

var_name_1 = 'main'
from mod_name_1 import *

print(var_name_1)

from mod_name_1 import funkt_name_1 as f1

f1()

# ## OOP - Klasse erstellen
# #########################################################################
print('\n# OOP')


class klassenName:
    ## Eigenschfaten
    # oeffentliche Eigenschaft
    confDict = {}
    # private Eigenschaft (__ am Anfang des Namens)
    __privateEigenschaft = 1

    ## Methoden
    # Konstruktor-Methode
    # Alles was beim Instanzieren sofort ausgeführt werden soll
    def __init__(self):
        self.__privateEigenschaft = 2
        self.__privateMethode()

    # Destruktor-Methode
    # Alles was beim Löschen bzw. Programmende ausgeführt werden soll
    def __del__(self):
        pass

    ## Istanzmethoden
    # oeffentliche Methode
    def oeffentlicheMethode(self):
        return self.__privateEigenschaft

    # private Methode
    def __privateMethode(self):
        print('__privateMethode')


## Objekt erzeugen
objName = klassenName()

print('objName.oeffentlicheMethode():', objName.oeffentlicheMethode())
