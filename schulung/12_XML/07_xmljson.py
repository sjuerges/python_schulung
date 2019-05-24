#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://pypi.org/project/xmljson/
# pip3.6 install xmltodict

import re

pfad = re.sub(r'^(.*)[\/\\].*$', r'\1', __file__)

import json
import xmltodict


def convert(xml_file, xml_attribs=True):
    with open(xml_file, 'rb') as f:  # Achtung 'rb' Modus
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
        return json.dumps(d, indent=4)


jsonString = convert(pfad + '/seminar.xml')
print(jsonString)

jsonObj = json.loads(jsonString)
print('SEMINARORT:', jsonObj['SEMINARPLAN']['SEMINAR']['SEMINARORT'])

print('SEMINARLEITER:', jsonObj['SEMINARPLAN']['SEMINAR']['SEMINARLEITER'])

print('TEILNEHMER:', jsonObj['SEMINARPLAN']['SEMINAR']['TEILNEHMER'])
