#!/usr/bin/python3
"""Defines the database storage engine for the program"""

from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DB storage engine class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        host = getenv('HBNB_MYSQL_HOST')
        pwd = getenv('HBNB_MYSQL_PWD')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(engine)

    def all(self, cls=None):
        """Returns a dictionary of all objects from the database"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        objects = {}
        if cls is not None:
            print(cls)
            queryResults = self.__session.query(cls.__class__.__name__).all()

            for result in queryResult:
                key = "{}.{}".format(result.__class__.__name__, result.id)
                objects[key] = result
        else:
            for className in [City, State, User]:
                queryResult = self.__session.query(className).all()
                for result in queryResult:
                    key = "{}.{}".format(result.__class__.__name__, result.id)
                    print(type(result))
                    objects[key] = result
        return objects

    def new(self, obj):
        """Adds obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session"""
        if obj is not None:
            self.__session.query(obj.__class__.__name__).delete()

    def reload(self):
        """Creates all tables in the database"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
