#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Installation
# Voraussetzung Python 3.3 und 3.4 unter Windows:
# https://www.microsoft.com/en-us/download/confirmation.aspx?id=8279

# cd c:\Python34\Scripts
# pip install lxml

# CentOS 7 Python 3.6 XML - Module schon vorhanden!

### ACHTUNG
# https://docs.python.org/3.6/library/xml.html#xml-vulnerabilities

import re
from xml.dom import minidom

doc = minidom.parse('config.xml')

kindListe = doc.getElementsByTagName('config')[0].childNodes


def allesAusgeben(kindListe, level=0):
    for kind in kindListe:
        ### Elementknoten
        if kind.nodeType == kind.ELEMENT_NODE:
            print(' ' * level * 4, 'Element-Anfang:', kind.tagName)
            newKindListe = kind.childNodes
            allesAusgeben(newKindListe, level + 1)
            print(' ' * level * 4, 'Element-Ende  :', kind.tagName)
        ### Textknoten wenn Sie etwas anderes als nur Whitespace beinhalten
        elif kind.nodeType == kind.TEXT_NODE and not re.compile(r'^\s*$').search(kind.nodeValue):
            print(' ' * (level + 1) * 4, 'TEXT.nodeValue:', kind.nodeValue)


allesAusgeben(kindListe)
