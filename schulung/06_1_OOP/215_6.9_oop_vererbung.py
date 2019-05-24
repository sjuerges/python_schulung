#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition der Klasse Fahrzeug - Buch S.214
class Fahrzeug:
    def __init__(self, bez, ge):
        self.bezeichnung = bez
        self.geschwindigkeit = ge

    def beschleunigen(self, wert):
        self.geschwindigkeit += wert

    def __str__(self):
        return self.bezeichnung + " " \
               + str(self.geschwindigkeit) + " km/h"


# Definition der Klasse PKW  - Buch S.215 (oben)
class PKW(Fahrzeug):  # Angabe der Basisklasse in Klammern!
    def __init__(self, bez, ge, ins):
        Fahrzeug.__init__(self, bez, ge)
        self.insassen = ins

    def __str__(self):
        return Fahrzeug.__str__(self) + " " \
               + str(self.insassen) + " Insassen"

    def einsteigen(self, anzahl):
        self.insassen += anzahl

    def aussteigen(self, anzahl):
        self.insassen -= anzahl


# Objekt der abgeleiteten Klasse PKW erzeugen   - Buch S.215 (unten)
fiat = PKW("Fiat Marea", 50, 0)

# eigene Methode anwenden
fiat.einsteigen(3)
fiat.aussteigen(1)

# geerbte Methode anwenden
fiat.beschleunigen(10)

# ueberschriebene Methode anwenden
print(fiat)
