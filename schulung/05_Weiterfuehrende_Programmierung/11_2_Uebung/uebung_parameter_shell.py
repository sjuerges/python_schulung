#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Aufruf:
# python3.6 uebung_parameter_shell.py --anzahlVers=3 --user=Admin --pass=123

import sys

sys.argv = ['uebung_parameter_shell.py', '--user=Adin', '--pass=12"=3', '--list=["a",2]', '--fl=3.0']

defaultDict = {
    'anzahlVers': 1,
    'user': '',
    'pass': '',
    'fl': 0.0,
    'list': [0, 3]
}

confDict = {}

for aktParam in sys.argv[1:]:

    paraName, *paraWert = aktParam.split('=', 1)
    paraName = paraName[2:]

    paraWert = '='.join(paraWert)

    if paraName in defaultDict:

        aktType = type(defaultDict[paraName]).__name__
        try:
            if aktType in ('str', 'int', 'float'):
                paraWert = eval(aktType + '("' + paraWert.replace('"', r'\"') + '")')
            else:
                paraWert = eval(aktType + '(' + paraWert + ')')
        except:
            print('Fehler:',
                  paraName,
                  '- ungültiger Datentyp, der Wert muss vom Typ',
                  aktType,
                  'sein. Default Wert wird verwendet.'
                  )
        confDict[paraName] = paraWert

defaultDict.update(confDict)

confDict = defaultDict

print('Ergebnis:', confDict)
