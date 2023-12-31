#!/usr/bin/python3
"""
Lists all values that matches user's input from the database hbtn_0e_0_usa,
safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name "
                "LIKE %s;", (sys.argv[4], ))
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
