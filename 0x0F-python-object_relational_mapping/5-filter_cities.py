#!/usr/bin/python3
"""Lists all cities of a given state"""

import MySQLdb
from sys import argv


if __name__ == '__main__':

    username = argv[1]
    pwd = argv[2]
    database = argv[3]
    queryState = argv[4]

    conn = MySQLdb.connect(user=username, passwd=pwd, db=database,
                                host='localhost', charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON state_id\
                                            = states.id WHERE states.name = %s\
                                            ORDER BY cities.id", (queryState,))
    query = cur.fetchall()
    cityList = []
    for row in query:
        cityList.append(row[0])

    print(", ".join(cityList))
