#!/usr/bin/python3
"""Defines a state model"""

from sqlalchemy.orm.declarative import declarative_base
frim sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Interger, create_engine


Base = declarative_base()


class State(Base):
    """A state class"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)

engine
