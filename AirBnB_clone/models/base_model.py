#!/usr/bin/python3
"""A module containing the base model of my console"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes and methods for other classes"""

    def __init__(self):
        """Object contructor"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the updated_at attribute to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        instance = self.__dict__
        instance['__class__'] = type(self).__name__
        instance['created_at'] = instance['created_at'].isoformat()
        instance['updated_at'] = instance['updated_at'].isoformat()

        return instance
