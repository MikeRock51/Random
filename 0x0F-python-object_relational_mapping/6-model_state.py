#!/usr/bin/python3
"""Links class to table in database"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State


if __name__ == '__main__':
    username = argv[1]
    pwd = argv[2]
    database = argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(username, pwd, database))
    Base.metadata.create_all(engine)
