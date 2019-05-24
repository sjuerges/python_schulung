#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modul
import re

# re.match()  - Sucht immer am Anfang der Zeichenkette
# re.search() - Sucht irgendwo im Text

# siehe auch: http://docs.python.org/3.6/library/re.html

testListe = ['Madlaine', 'Madleine', 'Madline']

reString = r'Madlaine';
# reString=r'Madl(a|e)ine';
# reString=r'Madl(a|e|)ine';
# reString=r'Madl(ai|ei|i)ne';
# reString=r'Madl[ae]ine';
# reString=r'Madl[ae]?ine';

regExpr = re.compile(reString);

print('Suche : ' + reString);

for i in testListe:
    if regExpr.search(i):
        print('%-10s : %s' % (i, 'wahr'))
    else:
        print('%-10s : %s' % (i, 'falsch'))
