#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Originallste - Zeichenketten
zk = ['Klaus', 'Heinrich', 'Adam']
print("Original:")
print(zk)

# Sortieren der Elemente
zk.sort()
print("Nach Sortieren:")
print(zk)

# Originallste - Zahlen
za = [10, 1010, 5, 20]
print("Original:")
print(za)

# Sortieren der Elemente
za.sort()
print("Nach Sortieren:")
print(za)

# Originallste - Zahlen und Zeichenketten
za = ['10', '1010', 5, 20]
print("Original:")
print(za)

# Sortieren der Elemente
try:
    za.sort()
    print("Nach Sortieren:")
    print(za)
except:
    print('Unterschiedliche Datentypen!')

# Mit Lambda - Funktion (Kann immer nur eine Anweisung enthalten!)
za.sort(key=lambda a: int(a))
print(za);


# Oder mit externer Funktion
def sortFunkt(z):
    return int(z)


za.sort(key=lambda a: sortFunkt(a))
print(za);

# Sortierrichtung mit sort(reverse={True|False})
za.sort(key=lambda a: int(a), reverse=True)
print(za);
