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

### Doku für die Methoden und Eigenschaften:
# https://docs.python.org/3.6/library/xml.dom.html

### The following interfaces have no implementation in xml.dom.minidom:

# DOMTimeStamp
# DocumentType
# DOMImplementation
# CharacterData
# CDATASection
# Notation
# Entity
# EntityReference
# DocumentFragment

from xml.dom import minidom

doc = minidom.parse('config.xml')

name = doc.getElementsByTagName('host')[0]

print(name.firstChild.data);

dbListe = doc.getElementsByTagName('db')

for db in dbListe:
    print(db.firstChild.data);

standby = doc.getElementsByTagName('standby')[0]
dbListe = standby.getElementsByTagName('db')

for db in dbListe:
    print(db.firstChild.data);

print('mysql db demo ohne standby')
mysql = doc.getElementsByTagName('mysql')[0]
kindListe = mysql.childNodes

for kind in kindListe:
    ### Nuer Elementknoten
    if kind.nodeType == 1:
        if kind.tagName == 'db':
            print(kind.firstChild.data)
