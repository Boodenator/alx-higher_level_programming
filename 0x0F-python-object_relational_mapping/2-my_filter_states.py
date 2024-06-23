#!/usr/bin/python3
"""
script for inputting an argument and show all values for names 
matching args the states table of hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == '__main__':

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    state_name = sys.argv[4]

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '%{}%'\
    ORDER BY states.id ASC".format(state_name))
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    db.close()
