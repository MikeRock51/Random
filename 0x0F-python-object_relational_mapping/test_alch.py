#!/usr/bin/python3
"""Lists all state from a database"""

from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from relationship_city import City


if __name__ == '__main__':

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2],
                                                    argv[3], pool_pre_ping=True
                                                    ))
    session = Session(engine)

    for className in [State, City]:
        print(className)
        queryResult = session.query(className).all()
        #for result in queryResult:
         #   print(f"{result.__class__.__name__}.{result.id}: {result}")
