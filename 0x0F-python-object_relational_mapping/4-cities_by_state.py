#!/usr/bin/python3
"""Lists all cities along with their corresponding
states from a given database"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    username = argv[1]
    pwd = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(user=username, passwd=pwd, host='localhost',
            db=database, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON state_id = states.id ORDER BY cities.id")
    query = cur.fetchall()

    for row in query:
        print(row)
