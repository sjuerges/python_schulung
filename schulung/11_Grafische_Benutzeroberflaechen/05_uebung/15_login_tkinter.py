#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Module einbinden
### #########################################################################
from login_mod import loginCheck

### Hauptprogramm
### #########################################################################
anzVersuche = 3  # Maximale Anzahl der Versuche

### DB -Konfiguration
config = {
    'user': 'root',
    'password': 'root',
    'host': '127.0.0.1',
    'database': 'logindb',
    'raise_on_warnings': True,
    'charset': 'utf8',
    'sql_mode': 'strict_trans_tables,strict_all_tables'
}

import tkinter


def ende():
    main.destroy()


def anmelden():
    ### NICHT FERTIG
    if loginCheck(loFeld.get(), pwFeld.get(), config, anzVersuche) == True:
        ergebnissText["text"] = 'richtig'
    else:
        ergebnissText["text"] = 'falsch'


main = tkinter.Tk()

# Row 0
ergebnissText = tkinter.Label(main, text="", width=8, anchor="w")
ergebnissText.grid(row=0, column=2, columnspan=2, sticky="we")

loText = tkinter.Label(main, text="Login:", width=8, anchor="w")
loText.grid(row=1, column=1, sticky="we")

loFeld = tkinter.Entry(
    main,
    bg="#FFFFFF",
    bd=1,
    width=8
)
loFeld.grid(row=1, column=2, columnspan=2, sticky="we")

pwText = tkinter.Label(main, text="Pass:", width=8, anchor="w")
pwText.grid(row=2, column=1, sticky="we")

pwFeld = tkinter.Entry(
    main,
    bg="#FFFFFF",
    bd=1,
    width=8
)
pwFeld.grid(row=2, column=2, columnspan=2, sticky="we")

tkinter.Label(
    main,
    text="",
    width=8
).grid(row=4, column=1, sticky="we")

tkinter.Button(
    main,
    text="Anmelden",
    width=8,
    command=lambda: anmelden()
).grid(row=3, column=2, columnspan=2, sticky="we")

main.mainloop()
