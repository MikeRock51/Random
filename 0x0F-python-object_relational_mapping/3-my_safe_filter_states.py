#!/usr/bin/python3
"""Lists all states from a database that matches a given name"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    username = argv[1]
    pwd = argv[2]
    database = argv[3]
    searchedState = argv[4]

    conn = MySQLdb.connect(user=username, passwd=pwd, db=database,
                                    host='localhost', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name =\
                %s ORDER BY states.id", (searchedState,))
    query = cur.fetchall()

    for row in query:
        print(row)
