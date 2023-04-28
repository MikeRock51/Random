#!/usr/bin/python3
"""Creates the state of California with the city San Francisco"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from sys import argv
from relationship_city import City


if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                            argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)
    sf = City(name="San Francisco")
    cali = State(name='California', cities=[sf])
    session.add(cali)
    session.commit()
    session.close()
