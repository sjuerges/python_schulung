#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Module
import _thread
import time

### 2 Hilfsvariablen damit das Hauptprogramm nicht
#   die Threads Abbricht bevor diese bendet wurden:
num_threads = 0  # Anzahl der aktiven Threads
thread_started = False  # Thread überhaupt jemals gestartet?


# thread_started wird benötigt damit das Hauptprogramm nicht
# abbricht bevor jemals ein Thread gestartet wurde

# Thread-Funktion
def show(tmp):
    global counter
    global num_threads, thread_started
    num_threads += 1
    thread_started = True

    # Fehlerhandling wird benötigt, damit der num_threads Counter
    # auch wenn ein Fehler auftritt reduziert wird
    try:
        id = _thread.get_ident()
        for i in range(5):
            counter += 1
            print(i, id, counter, tmp)

            # Division durch 0
            if counter == 5:
                erg = 1 / 0
            time.sleep(1.5)
        num_threads -= 1
    except:
        # Auch bei Fehler num_threads wieder reduzieren.
        num_threads -= 1
    return


# Hauptprogramm
id = _thread.get_ident()
counter = 0
print(id, counter)

_thread.start_new_thread(show, tuple('a'))
time.sleep(0.5)
_thread.start_new_thread(show, tuple('b'))

# Erst im Hauptprogramm weiter wenn alle Threads beendet sind!
while num_threads > 0 or thread_started == False:
    pass

counter += 1
print(id, counter)
