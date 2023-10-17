#!/usr/bin/python3
"""
documentation for file storage
"""
import json

class FileStorage:
    """
    Manages the serialization and deserialization of instances to and from a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary to store serialized instances.

    Methods:
        all(self):
            Returns the dictionary of serialized objects.
        new(self, obj):
            Adds a new object to the dictionary of serialized objects.
        save(self):
            Serializes objects to the JSON file.
        reload(self):
            Deserializes the JSON file to objects.

    Usage Example:
        storage = FileStorage()
        storage.reload()
        all_objects = storage.all()
        my_model = BaseModel()
        storage.new(my_model)
        storage.save()
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of serialized objects.

        Returns:
            dict: A dictionary containing serialized objects.

        Usage Example:
            all_objects = storage.all()
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of serialized objects.

        Args:
            obj (BaseModel): An instance of a BaseModel or a subclass.

        Usage Example:
            my_model = BaseModel()
            storage.new(my_model)
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects to the JSON file.

        Usage Example:
            storage.save()
        """

        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        Deserializes the JSON file to objects.

        Usage Example:
            storage.reload()
        """

        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError:
            pass
