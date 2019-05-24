#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# HTML-Dokument mit Variablen
print("Content-type: text/html")
print()

import sys
import os
sys.path.insert(0,'./modul/')
import cgi

from loKlasse import loKlasse;

# Ausgabe bei Fehler im Browser
import cgitb
cgitb.enable()
# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

formObj=loKlasse('./daten/lo_pw.txt',form);
maxAnzVersuche=3
spaltenUeberschriften = ['Login','Password'];

print('''<!DOCTYPE html>
<html>
    <head>
        <meta charset='utf-8'>
        <title>Login</title>
        <style>
            body{
                font-family: Verdana, sans-serif;
            }
            form, p{
                margin: 10px auto;
            }
            h1, pre{
                width: 1000px;
                margin: 10px auto;
            }
            .lo{
                 width:250px;
            }
            label{
                display:block;
                width:250px;
                margin-top: 10px;
            }
            input{
                width: 100%;
            }
            input[type="submit"]{
                 margin-top: 10px;
            }
        </style>
    </head>
    <body>''')

loginOK=formObj.loginCheck(maxAnzVersuche)

if loginOK:
    print('<h1>Herzlich willkommen</h1>')
    print('<pre>',formObj.zeigeLogins(spaltenUeberschriften),'</pre>',sep='')
elif not loginOK and int(formObj.formValue['anzVers'])>maxAnzVersuche:
    print('<h1>Falsche Login/Passwort Kombination</h1>')
else:
    print('''
        <h1 class="lo">Login</h1>
        <p class="lo">'''+formObj.anzVersucheText+'''</p>
        <form class="lo" action="'''+os.environ['SCRIPT_NAME']+'''" method="post">
            <label for="lo">Login:</label><input id="lo" name="lo" value="'''+formObj.formValue['lo']+'''"><br>
            <label for="pw">Pass:</label><input id="pw" name="pw" type="password"><br>
            <input name="anzVers" type="hidden" value="'''+formObj.formValue['anzVers']+'''">
            <input type="submit" value="Anmelden">
        </form>''')
    
print('''</body>
</html>''')
