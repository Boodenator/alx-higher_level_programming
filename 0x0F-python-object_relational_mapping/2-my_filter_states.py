#!/usr/bin/python3
"""
script with arguments as input and values arranged in 
a table as output of hbtn_0e_usa.
"""

import sys
import MYSQLdb


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
