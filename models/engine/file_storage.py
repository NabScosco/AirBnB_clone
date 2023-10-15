#!/usr/bin/python3
"""
Mnodule: file_storage.py

This defines a a `FileStorage` class.
"""

import json


class FileStorage:
    """
    This class handles the serialization and deserialization
    of objects to and from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file where
        objects will be stored.
        __objects (dict): A dictionary that will hold all
        objects by their class name and ID.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary containing all objects.

        Returns:
            dict: A dictionary containing all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to a JSON file.
        """
        obj_dict = {
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes objects from the JSON file.
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            pass
