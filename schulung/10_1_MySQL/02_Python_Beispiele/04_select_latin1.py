#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### DB mit latin1 als Zeichensatz

import mysql.connector
from mysql.connector import errorcode

'''
CREATE DATABASE test;
CREATE TABLE test.lopw (
  `login` varchar(60) NOT NULL,
  `pass` varchar(69) DEFAULT NULL,
  PRIMARY KEY (`login`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
insert into test.lopw values('admin','123');
'''

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'test'
}

try:
    cnx = mysql.connector.connect(**config)

    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT count(*) anz FROM lopw "
             "WHERE login = %(login)s and pass = %(pass)s")

    cursor.execute(query, {'login': 'admin', 'pass': '123'})

    datensatz = cursor.fetchone()

    # if datensatz['anz']==1:
    ### ODER
    if datensatz[b'anz'] == 1:
        print('vorhanden')
    else:
        print('NICHT vorhanden')

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
