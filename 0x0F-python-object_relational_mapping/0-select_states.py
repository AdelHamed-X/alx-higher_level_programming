#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv

mysql_username, mysql_password, database_name = argv[1], argv[2], argv[3]

db = MySQLdb.connect(host='localhost',
                     user=f'{mysql_username}',
                     passwd=f'{mysql_password}',
                     db=f'{database_name}',
                     port=3306)

db_cursor = db.cursor()

db_cursor.execute("SELECT * FROM states")

rows = db_cursor.fetchall()

for row in rows:
  print(row)
