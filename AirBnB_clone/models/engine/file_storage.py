#!/usr/bin/python3
"""File Storage module for persisting instances"""

import json
import os


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
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes __objects to file.json"""
        objs = {}
        with open(self.__file_path, 'w') as file:
            # print(f"WWWWIIII:-> {self.__objects}")
            for key, value in self.__objects.items():
                objs[key] = value.to_dict()
            json.dump(objs, file)

    def reload(self):
        """Deserializes the Json file to __objects"""
        from models.base_model import BaseModel

        json_load = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_load = json.load(file)
            for key, value in json_load.items():
                self.__objects[key] = BaseModel(**value)
        else:
            return