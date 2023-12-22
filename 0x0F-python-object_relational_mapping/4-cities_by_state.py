#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id;")
    states = cur.fetchall()

    for state in states:
        print(state)
