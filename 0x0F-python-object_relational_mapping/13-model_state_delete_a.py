#!/usr/bin/python3
"""
Deletes all state objects with name containing
letter a from the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                            argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    stateChange = session.query(State).filter(State.name.like('%a%')).delete()
    session.commit()
    session.close()
