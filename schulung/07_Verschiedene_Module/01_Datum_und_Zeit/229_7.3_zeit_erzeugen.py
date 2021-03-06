#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import locale
# Modul time
import time

# locale.setlocale(locale.LC_TIME, 'deu_deu')  # WIN
locale.setlocale(locale.LC_TIME,'de_DE') # Linux

# Aktuelle Zeit
lt = time.localtime()

print(time.strftime("Tag.Monat.Jahr: %d.%m.%Y", lt))
print(time.strftime("Stunde:Minute:Sekunde: %H:%M:%S", lt))
print(time.strftime("im 12-Stunden-Format:"
                    " %I:%M:%S Uhr %p", lt))
print(time.strftime("Datum und Zeit: %c", lt))
print(time.strftime("nur Datum: %x, nur Zeit: %X", lt))
print(time.strftime("Jahr in zwei Ziffern: %y", lt))
print(time.strftime("Tag des Jahres: %j", lt))
print()

# Woche, Monat
print(time.strftime("Wochentag kurz:%a, ganz:%A,"
                    " Nr.(Sonntag=0):%w", lt))
print(time.strftime("Monat kurz:%b, ganz:%B", lt))
print()

# Kalenderwoche
print(time.strftime("Woche des Jahres,"
                    " Beginn Sonntag: %U", lt))
print(time.strftime("Woche des Jahres,"
                    " Beginn Montag: %W", lt))
print()

# Zeitzone
print(time.strftime("Zeitzone: %Z", lt))
