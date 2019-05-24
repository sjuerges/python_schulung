#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import xml.etree.ElementTree as ET

pfad = re.sub(r'^(.*)[\/\\].*$', r'\1', __file__)

tree = ET.parse(pfad + '/seminar.xml')
root = tree.getroot()

# XPath: https://docs.python.org/3.6/library/xml.etree.elementtree.html#example
for treffer in root.findall('*/*/NACHNAME'):
    print(treffer.text)

for treffer in root.findall('SEMINAR/*/[@anrede]'):
    print(treffer.attrib['anrede'])

for treffer in root.findall('SEMINAR/*/[@anrede]'):
    print(treffer.attrib['anrede'], treffer.findall('VORNAME')[0].text, treffer.findall('NACHNAME')[0].text)
