#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Module
import _thread
import time


# Thread-Funktion
def show():
    global counter
    id = _thread.get_ident()
    for i in range(5):
        counter += 1
        print(i, id, counter)
        time.sleep(1.5)
    return


# Hauptprogramm
id = _thread.get_ident()
counter = 0
print(id, counter)

_thread.start_new_thread(show, ())
time.sleep(0.5)
_thread.start_new_thread(show, ())
time.sleep(10)

counter += 1
print(id, counter)
