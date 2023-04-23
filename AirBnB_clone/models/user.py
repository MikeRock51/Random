#!/usr/bin/python3
"""Contains the user class"""


from models.base_model import BaseModel


class User(BaseModel):
    """The user class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
