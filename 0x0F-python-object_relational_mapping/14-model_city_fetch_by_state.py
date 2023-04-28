#!/usr/bin/python3
"""Prints all city objects from the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == '__main__':

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                        argv[2], argv[3]), pool_pre_ping=True)

    session = Session(engine)
    cities = session.query(City, State).filter(
                            State.id == City.state_id).order_by(City.id).all()
    for city in cities:
        print("{}: ({}) {}".format(city[1].name, city[0].id, city[0].name))

    session.close()
