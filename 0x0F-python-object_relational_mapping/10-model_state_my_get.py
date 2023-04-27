#!/usr/bin/python3
"""Prints the state id of a requested state from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                            argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    stateId = session.query(State.id).filter(State.name == argv[4]).first()

    if stateId:
        print(stateId[0])
    else:
        print("Not found")
