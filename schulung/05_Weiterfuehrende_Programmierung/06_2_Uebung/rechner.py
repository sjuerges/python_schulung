#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Rechner für die Grundrechenarten, welcher wie folgt funktioniert:
#
# Zahl1	 : 2,2
# Das war keine Zahl!!!
# Zahl1	 : 2.2
# Rechenart : plus
# "plus" ist keine gültige Rechenart. Zulässig sind: +, -, *, /
# Rechenart : +
# Zahl2	 : 3
# ---------------
# Ergebnis  : 5.2

def zahlEinlesen(p_text, p_fehlertext, p_ra='', p_fehlertextDivision=''):
    while True:
        try:
            z = float(input(p_text))
            if z == 0 and p_ra == '/':
                raise RuntimeError(p_fehlertextDivision)
            break
        except RuntimeError as e:
            print(e)
        except:
            print(p_fehlertext)
    return z


def raPruefen(p_text, p_rechenArtListe, p_fehlertext):
    while True:
        text = input(p_text)
        if text in p_rechenArtListe:
            break
        else:
            print(p_fehlertext % (text, ', '.join(p_rechenArtListe)))

    return text


fehlertextZahl = 'Das war keine Zahl!!!'
fehlertextRechenart = '"%s" ist keine gültige Rechenart. Zulässig sind: %s'
rechenArtListe = ('+', '-', '*', '/', '**');
fehlertextDivision = 'Division durch 0 auch in Python nicht möglich.\nBitte eine andere Zahl eingeben.'

### Usereingaben
zahl1 = zahlEinlesen('Zahl1	  : ', fehlertextZahl)

ra = raPruefen('Rechenart : ', rechenArtListe, fehlertextRechenart)

zahl2 = zahlEinlesen('Zahl2	  : ', fehlertextZahl, ra, fehlertextDivision)

### Rechnen
erg = str((eval(str(zahl1) + ra + str(zahl2))))

### Ausgeben
print('------------' + '-' * len(erg))
print('Ergebnis  : ' + erg)
