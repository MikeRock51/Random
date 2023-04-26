#!/usr/bin/python3
"""The state model"""


from models.base_model import BaseModel


class State(BaseModel, Base):
    """The state class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if HBNB_TYPE_STORAGE == 'db':
        cities = relationship('City')
