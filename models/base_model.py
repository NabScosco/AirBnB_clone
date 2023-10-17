#!/usr/bin/python3
"""
Module for BaseModel class.
"""

from datetime import datetime
import uuid
from models import storage

class BaseModel:
    """
    Defines a BaseModel class that serves as the foundation for other classes.

    Attributes:
        id (str): A unique identifier generated using uuid.uuid4().
        created_at (datetime): The date and time when the instance is created.
        updated_at (datetime): The date and time when the instance is last updated.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes a new instance of BaseModel.
        save(self):
            Updates the `updated_at` attribute with the current date and time.
        to_dict(self):
            Returns a dictionary representation of the instance's attributes.

    Usage Example:
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable-length argument list (not used).
            **kwargs: Arbitrary keyword arguments to initialize instance attributes.

        Note:
            If kwargs is not empty, each key is an attribute name and each value is
            the corresponding value for that attribute. If empty, id and created_at
            are generated.

        Usage Example:
            my_model = BaseModel(name="Example", my_number=42)
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A formatted string containing class name, id, and attributes.

        Usage Example:
            print(my_model)
        """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute with the current date and time.

        Usage Example:
            my_model.save()
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance's attributes.

        Returns:
            dict: A dictionary containing the attributes and their values.

        Usage Example:
            my_dict = my_model.to_dict()
        """

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
