#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modul
import re

testListe = ['a@a.de', 'a@a.a.de', 'a@@a.de', 'a@a..de', 'a b@a.de', 'meine@тесто.москва', 'a@?.a.de']

reString = r'''
	^                                                      # nichts davor
	\S+                                                    # Kein Whitespace mindestens 1-mal
	@                                                      # ein @ vor dem Domainnamen
	([^^°!"§$%&/()=?`´²³{}\[\]\\*+~'#;:,\.<>|\s]+\.)+      # Domain + Subleveldomainname - mindestens 1 Zeichen und keine der genannten Zeichen
	[^^°!"§$%&/()=?`´²³{}\[\]\\*+~'#;:,\.<>|\s\-]{2,}      # Top-Level-Domain-Name - Lateinische Buchstaben - mindestens 2
	$                                                      # nichts dahinter
'''

regExpr = re.compile(reString, re.X)

print('Suche : ' + reString)

for i in testListe:
    if regExpr.search(i):
        print('%-10s : %s' % (i, 'wahr'))
    else:
        print('%-10s : %s' % (i, 'falsch'))
