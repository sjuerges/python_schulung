#!/usr/bin/env python3

# Modul cgi
import  cgi, cgitb

# Ausgabe bei Fehler
cgitb.enable()

# Objekt der Klasse FieldStorage
form = cgi.FieldStorage()

# Einzelne Elemente des Objekts
if "nn" in form:
    nn = form["nn"].value
else:
    nn=''

if "vn" in form:
    vn = form["vn"].value




# HTML-Dokument mit Variablen
print("Content-type: text/html")
print()

print("<!DOCTYPE html><html>")
print("<head><meta charset='utf-8'></head>");
print("<body>")

if nn=='' or vn=='':
    print('''
          <b>Bitte senden Sie Ihre Daten:</b><p>
   <form action="/cgi-bin/315_9.12_server_antworten.cgi">
      <input name="nn"> Nachname<p>
      <input name="vn"> Vorname<p>
      <input type="submit">
   </form>''')
else:
    print("<p><b>Registrierte Daten:</b></p>")
    print("<p>Nachname:", nn, "</p>")
    print("<p>Vorname:", vn, "</p>")

print("</body>")
print("</html>")
