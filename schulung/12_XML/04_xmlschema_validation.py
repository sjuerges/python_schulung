#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install xmlschema

import re

import xmlschema

pfad = re.sub(r'^(.*)[\/\\].*$', r'\1', __file__)

schemaObj = xmlschema.XMLSchema(pfad + '/seminar.xsd')

# XML-Datei validieren
if schemaObj.is_valid(pfad + '/seminar.xml'):
    print('Die XML-Datei entspricht dem Schema')
else:
    print('Ung�ltige XML-Datei')

# XML-Datei validieren mit Error
try:
    schemaObj.validate(pfad + '/seminar_fehler.xml')
    print('Die XML-Datei entspricht dem Schema')
except xmlschema.validators.exceptions.XMLSchemaValidationError as msg:
    print(msg)
