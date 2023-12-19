#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities, states FROM cities;")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
