#!/usr/bin/python3
"""Lists all states starting with N from a database"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    username = argv[1]
    pwd = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(user=username, passwd=pwd, db=database,
                                    charset='utf8', host='localhost')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE SUBSTRING(name, 1, 1)\
                                            = 'N' ORDER BY states.id")
    query = cur.fetchall()

    for row in query:
        print(row)
