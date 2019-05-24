#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### DB mit utf-8 als Zeichensatz

'''
create user müller identified by '123';
grant all on *.* to müller;
'''

import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'mysql'
}

try:
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT host, user FROM user "
             "WHERE user like %(user)s")

    # cursor.execute(query,{'user':'müller'})
    cursor.execute(query, {'user': '%'})
    datensatz = cursor.fetchone()
    while datensatz:
        ### bytes(datensatz[b'host']).decode('utf-8') -> UTF-8 in der DB
        ### MySQL 5.7.x
        # print(bytes(datensatz['host']).decode('utf-8'),bytes(datensatz['user']).decode('utf-8'))
        ### MySQL 8.0.11
        print(bytes(datensatz[b'host']).decode('utf-8'), bytes(datensatz[b'user']).decode('utf-8'))
        datensatz = cursor.fetchone()

    cursor.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
