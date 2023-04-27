#!/usr/bin/python3
"""Defines the database storage engine for the program"""

from sqlalchemy import create_engine

class DBStorage:
    """DB storage engine class"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(

