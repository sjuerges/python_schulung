#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# print() erzeugt am Ende einen Zeilenumbruch
# print() fügt zwischen den Parametern ein " " ein

print('Hallo', 'Leute');
print('Hallo', 'Leute');

# Dieses Verhalten kann durch die Parameter end='' und sep=''
# geändert werden (siehe Auch S. 150 im Buch)

print('\nHallo', 'Leute', end=' ');
print('Hallo', 'Leute', sep='***');
print('Hallo', 'Leute', sep='', end='');
print('Test');

# Dies ist auch eine Verkettung allerdings werden 
# zuerst die Strings verkettet und danach print() 
# ausgeführt
print('\n\n' 'Hallo' ' Leute');

# ## Achtung dies geht nur mit echten String-Objekten!
# print('\n\n' 'Hallo' 5);
# print('\n\n' 'Hallo' str(5));
# print('\n\n' 'Hallo' + str(5));
