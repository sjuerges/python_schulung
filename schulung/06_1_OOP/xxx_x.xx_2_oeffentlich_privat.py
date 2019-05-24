#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# property()
# Python bietet eine Möglichkeit, Attribute so zu definieren,
# dass man auf sie von außen scheinbar direkt zugreifen kann,
# der Zugriff aber von Methoden kontrolliert wird.

class test:
    def __init__(self):
        self._varInt = 0

    def getVarInt(self):
        return self._varInt

    def setVarInt(self, wert):
        try:
            self._varInt = int(wert)
        except:
            print('Datentypfehler');

    def delVarInt(self):
        del self._varInt

    varInt = property(getVarInt, setVarInt, delVarInt)


t = test();
print(t.varInt)
t.varInt = 'abc'
t.varInt = 10.5
# t.varInt=10
print(t.varInt)
