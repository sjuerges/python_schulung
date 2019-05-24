#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Erstellen Sie ein Login Script welches wie folgt funktioniert:
# ... Uebung>01_login.py
# Login    : Admin
# Pass     : 123
# Herzlich willkommen!

# ... Uebung>01_login.py
# Login    : aaa
# Pass     : bbb
# Ungültige Login/Passwort Kombination!

lo = 'Admin'
pw = '123'

u_lo = input('Login    : ')
u_pw = input('Pass     : ')

if lo == u_lo and pw == u_pw:
    print('Herzlich willkommen!')
else:
    print('Ungültige Login/Passwort Kombination!')

print()
input('Schließen mit Return')
