#!/usr/bin/python3
"""Prints the first state object from a database"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv


if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    state = session.query(State).order_by(State.id).first()

    print("{}: {}".format(state.id, state.name))

    session.close()
