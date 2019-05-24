#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='',
                              host='localhost',
                              database='mysql')
cnx.close()
