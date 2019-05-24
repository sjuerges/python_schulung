#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

from lxml import etree

pfad = re.sub(r'^(.*)[\/\\].*$', r'\1', __file__)


def validate(xmlDatei: str, xsdDatei: str) -> bool:
    xmlSchemaDoc = etree.parse(xsdDatei)
    xmlSchema = etree.XMLSchema(xmlSchemaDoc)

    xmlDoc = etree.parse(xmlDatei)

    return xmlSchema.validate(xmlDoc)


# XML-Datei validieren
if validate(pfad + '/seminar.xml', pfad + '/seminar.xsd'):
    print('Die XML-Datei entspricht dem Schema')
else:
    print('Ung�ltige XML-Datei')

# XML-Datei validieren mit Error
from lxml.etree import XMLParser, XMLSchema, parse, XMLSyntaxError

parser = XMLParser(schema=XMLSchema(file=pfad + '/seminar.xsd'))
try:
    xml = parse(open(pfad + '/seminar_fehler.xml', mode='rb'), parser)
except XMLSyntaxError as e:
    for error in parser.error_log:
        print(error.message, error.line, error.column)
