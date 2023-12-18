#!/usr/bin/python3
"""
Lists all states that starts with N from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3], port=3306)

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%'
            COLLATE utf8mb4_bin;")
    states = c.fetchall()

    for state in states:
        print(state)

    c.close()
    db.close()
