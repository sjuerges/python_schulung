#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modul
import re

# siehe auch: http://docs.python.org/3.6/library/re.html

testListe = ['Madlaine Müller', 'Schulze Madleine', 'Madline']

reString = r'Madl[ae]?ine'  # Irgendwo in der Zeichenkette
# reString=r'^Madl[ae]?ine' # Am Anfang der Zeichenkette
# reString=r'Madl[ae]?ine$' # Am Ende der Zeichenkette
# reString=r'^Madl[ae]?ine$'# Alleine in der Zeichenkette

regExpr = re.compile(reString)

print('Suche : ' + reString)

for i in testListe:
    # print(regExpr.match(i))
    if regExpr.search(i):
        print('%-17s : %s' % (i, 'wahr'))
    else:
        print('%-17s : %s' % (i, 'falsch'))
