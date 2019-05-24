#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### siehe auch: http://blog.lerner.co.il/python-attributes/

# Definition der Klasse o_p
class testClass:
    __privat = 'private variable in der klasse o_p'

    def get__pr(self):
        return self.__privat


testObj = testClass()

try:
    print(testObj.__privat)
except:
    print('Zugriff auf test.__pr nicht möglich!')

### Dies funktioniert aber
print('\n# Neue Eigenschaft hinzufügen:')
testObj.__privat = 'Neue Eigenschaft'
### testObj.__pr und __pr im objekt sind nicht wirklich das gleiche!!! 
print(testObj.__privat, testObj.get__pr(), sep='\n')

# Es gibt einmal: __privat            -> testObj.__privat
# und einmal    : _testClass__privat  -> testObj._testClass__privat
print('\n# Prüfen mit dir():')
varListe = dir(testObj)
# print(*varListe,sep='\n')
for aktVar in varListe:
    if 'privat' in aktVar:
        aktWert = eval('testObj.' + aktVar)
        print(f'testObj.{aktVar:<20} = {aktWert}')

# Bedeutet man kann die angeblich private Eigenschaft
# doch manipulieren!
# ###################################################################
print('\n# Private Eigenschaft wirklich überschrieben:')
testObj._testClass__privat = 'neu'
print(testObj.__privat, testObj.get__pr(), sep='\n')
