#!/usr/bin/python3
"""Lists all states from hbtn_0e_0_usa database using MySQLdb"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    pwd = argv[2]
    database = argv[3]

    conn = MySQLdb.connect(user=username, passwd=pwd, db=database,
                                 host='localhost', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    query = cur.fetchall()
    for row in query:
        print(row)
