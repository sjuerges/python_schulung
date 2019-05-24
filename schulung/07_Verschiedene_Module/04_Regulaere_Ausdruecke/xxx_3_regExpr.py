#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Modul
import re

# siehe auch: http://docs.python.org/3.6/library/re.html

testListe = ['Das Haus ist schön', 'Ich komme aus Berlin', 'Ich möchte ausschlafen']

# \b = Wortgrenze
# \B = NICHT Wortgrenze

reString = r'aus'
# reString=r'aus\b'
# reString=r'aus\B'
# reString=r'\baus'
# reString=r'\Baus'
# reString=r'\baus\b'

regExpr = re.compile(reString)

print('Suche : ' + reString)

for i in testListe:
    # print(regExpr.match(i))
    if regExpr.search(i):
        print('%-17s : %s' % (i, 'wahr'))
    else:
        print('%-17s : %s' % (i, 'falsch'))
