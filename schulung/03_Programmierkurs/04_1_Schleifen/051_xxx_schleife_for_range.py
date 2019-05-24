#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# range(INTEGER start,INTEGER stop,INTEGER increment)

for i in range(1, 10, 2):
    print("Zahl:", i)

for i in range(-1, -10, -2):
    print("Zahl:", i)

# Fehler:
# for i in range(-1, -10, -2.5):
#	print("Zahl:", i)
