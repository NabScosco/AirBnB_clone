#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class serves as the base for other classes.
    It defines common attributes and methods.
    """

    def __init__(self):
        """
        Initialize a new instance of BaseModel.

        Attributes:
            id (str): Unique identifier generated using uuid4.
            created_at (datetime): Timestamp of when the instance is created.
            updated_at (datetime): Timestamp of when the instance is
            last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Update the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the object's attributes to a dictionary representation.

        Returns:
            dict: A dictionary containing the object's attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Return a string representation of the object.

        Returns:
            str: A formatted string with class name, id, and attributes.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
