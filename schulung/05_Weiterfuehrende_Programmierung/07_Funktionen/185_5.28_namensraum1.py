#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Testfunktion
def func():
    try:
        print(x)
    except:
        print("Fehler")


# Hauptprogramm
func()
x = 42
func()


# Testfunktion 2
def func2(x):
    try:
        print(x)
    except:
        print("Fehler")


# Hauptprogramm
func2(5)
print(x)
func2(10)
print(x)
