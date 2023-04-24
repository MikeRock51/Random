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
            for key, value in self.__objects.items():
                objs[key] = value.to_dict()
            json.dump(objs, file)

    def class_list(self):
            from models.base_model import BaseModel
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review

            return {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
            }

    def reload(self):
        """Deserializes the Json file to __objects"""
        from models.base_model import BaseModel

        json_load = {}
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                json_load = json.load(file)
            for key, value in json_load.items():
                # print(value['__class__'])
                calling_class = self.class_list()[value['__class__']]
                # print(calling_class)
                self.__objects[key] = calling_class(**value) 
        else:
            return
