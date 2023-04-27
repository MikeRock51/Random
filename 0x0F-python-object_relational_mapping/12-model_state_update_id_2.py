#!/usr/bin/python3
"""Changes the name of a state object from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State


if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                            argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    stateChange = session.query(State).filter(State.id == 2).first()
    stateChange.name ='New Mexico'
    session.add(stateChange)
    session.commit()
    session.close()
