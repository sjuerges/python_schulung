#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# siehe auch 04 Datentypen Buch Seite 97

# Zeichenketten können in ', " oder in ''' stehen
print('"Hallo" sagte er.',
      "'Hallo' sagte er.",
      '''Er sagte "Hallo" oder war es doch 'Hallo'.''', sep='\n')

# Das Escape Zeichen ist \
print('\n\nEr sagte \'Hallo\'.')

# Nun ist \ kein Escape Zeichen mehr (r=raw(roh) String)
print(r'\n\nEr sagte \'Hallo\'.')
# HINWEIS: Verwenden Sie raw Strings für reguläre Ausdrücke!

# Unicode String
print(u'\n\nEr sagte \'Hallo\'.')

# Mehrzeilige Strings müssen in ''' stehen
print('''
Hallo
	Leute
''')
