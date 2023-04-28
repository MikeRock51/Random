#!/usr/bin/python3
"""Defines the database storage engine for the program"""

from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base

class DBStorage:
    """DB storage engine class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        host = getenv('HBNB_MYSQL_HOST')
        pwd = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb//{}:{}@{}/{}".format(user, pwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        objects = {}
        if cls is not None:
            queryResults = self.__session.query(cls).all()

            for result in queryResult:
                key = "{}.{}".format(result.__class__.__name__, result.id)
                objects[key] = result
        else:
            for className in [User, State, City, Amenity, Place, Review]:
                queryResult = self.__session.query(className).all()
                for result in queryResult:
                    key = "{}.{}".format(result.__class__.__name__, result.id)
                    objects[key] = result
        return objects

