#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Siehe auch: http://docs.python.org/3.6/tutorial/classes.html#private-variables

# In Python wird zwischen 
# "Stark privaten Attributen und Methoden" und 
# "Schwach privaten Attributen und Methoden" unterschieden
# 1) "Stark private Attributen und Methoden" beginnen mit #    "__" im Namen und enden nicht mit einen Unterstrich.
#    Sie sind nur innerhalb der Klasse in welcher Sie 
#    definiert wurden verwendbar.
# 2) "Schwach private Attributen und Methoden" beginnen mit #    "_" im Namen und enden nicht mit einen Unterstrich.
#    Sie werden durch "from ... import *" ignoriert.
#    Man kann aber Problemlos auf Sie zugreifen wenn der Name
#    bekannt ist.

# Definition der Klasse o_p
class o_p:
    oe = 'oeffentlich'
    __pr = 'privat'

    def get_pr(self):
        return self.__pr

    def set_pr(self, neu):
        self.__pr = neu

    def oe_methode(self):
        return self.__pr_methode()

    def __pr_methode(self):
        return self.__pr


test = o_p()

# �ffentliche Eigenschaft ausgeben und manipulieren
print(test.oe)
test.oe = 'test.oe ueberschrieben'
print(test.oe)
print()

# Private Eigenschaft ausgeben und manipulieren
try:
    print(test.__pr)
except:
    print('Zugriff auf test.__pr nicht möglich!')
print(test.get_pr())
test.set_pr('test.__pr ueberschrieben')
print(test.get_pr())
print()

# Private Methode aufrufen
try:
    print(test.__pr_methode)
except:
    print('Zugriff auf test.__pr_methode() nicht möglich!')
print()

# Private Methode über öffentliche Methode aufrufen
print('Private Methode über öffentliche Methode aufrufen:', test.oe_methode())
