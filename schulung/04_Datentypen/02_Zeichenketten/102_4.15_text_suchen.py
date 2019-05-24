#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Beispiel
test = "Das ist ein Beispielsatz"
print("Text:", test)

# Anzahl Suchtexte
such = "ei"
anz = test.count(such)
print("count: Der String", such, "kommt", anz, "mal vor")

# Erste Position des Suchtextes
anfpos = test.find(such)
print("find 1: Zum ersten Mal an Position", anfpos)

# Weitere Position des Suchtextes
nextpos = test.find(such, anfpos + 1)
print("find 2: Ein weiteres Mal an Position", nextpos)

# Letzte Position des Suchtextes
endpos = test.rfind(such)
print("rfind: Zum letzten Mal an Position", endpos)

# Suchtext nicht gefunden
such = "am"
pos = test.find(such)
if pos == -1:
    print("find 3:", such, "wurde nicht gefunden")
else:
    print("find 3:", such, "an Position", pos, "gefunden")

# Ersetzen von Text
test = test.replace("ist", "war")
print("replace:", test)

test = "Das ist ein Beispielsatz. Das noch ein Beispielsatz"
such = "ei"
pos = -1
while True:
    pos = test.find(such, pos + 1)
    if pos <= -1:
        break
    print(pos)

anzahl = test.count(such)
pos = -1
for i in range(anzahl):
    pos = test.find(such, pos + 1)
    print(pos)
