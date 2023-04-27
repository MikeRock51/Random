#!/usr/bin/python3
"""Adds a state object to the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                            argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    newState = State(name="Louisiana");
    session.add(newState)
    session.commit()
    print(newState.id)
    session.close()
