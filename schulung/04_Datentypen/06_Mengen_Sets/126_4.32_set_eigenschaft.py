#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ein Set unterscheidet sich von Listen und Tupel dadurch, 
# dass jedes Element nur einmal existiert.

# Liste
li = [8, 2, 5, 5, 5]
print("Liste:", li)

# Set
s1 = set([8, 2, 5, 5, 5])
print("Set:", s1)
print("Anzahl:", len(s1))

# Elemente
for x in s1:
    print("Element:", x)
if 5 in s1:
    print("5 ist enthalten")