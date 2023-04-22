#!/usr/bin/python3
"""File Storage module for persisting instances"""


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}


    def all(self):
        """Returns all stored instances"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Saves obj into __objects with the key <obj class name>.id
        """
        setattr(__objects, type(obj).__name__, obj)

    def save(self):
        """Serilizes __objects to file.json"""

