#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user, pwd, database, state = argv[1:]

    db = MySQLdb.connect(host='localhost', user=user,
                         passwd=pwd, db=database, port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "JOIN states ON cities.state_id = cities.id "
                "WHERE states.name = %s;", (state, ))

    cities = cur.fetchall()
    if cities:
        print(", ".join(city[0] for city in cities))
