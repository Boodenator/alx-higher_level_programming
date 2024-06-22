#!/usr/bin/python3
"""
a script with aruments as input and values of states tables
hbtn_0e_0_usa as a database.
"""


import sys
import MYSQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    state_name = sys.argv[4]

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = (%s)\
    ORDER BY states.id ASC", (state_name,))
    table = cur.fetchall()

    for row in table:
        print(row)

    cur.close()
    db.close()
