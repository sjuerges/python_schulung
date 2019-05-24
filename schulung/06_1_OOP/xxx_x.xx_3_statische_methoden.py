#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Statische Methode können über den Klassennamen aufgerufen
# werden.

class statischeM:
    def __init__(self):
        self.merke = 'Test';

    def meine():
        print('Alles Gut!')

    def deine(self):
        print(self.merke)


statischeM.meine()
try:
    statischeM.deine()
except:
    print('deine() ist keine statische Methode!')

t = statischeM()
t.deine();
