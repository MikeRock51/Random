#!/usr/bin/python3
"""The city model"""


from models.base_model import BaseModel


class City(BaseModel, Base):
    """The city class"""
    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
    name = Column(String(128), nullable=False)
