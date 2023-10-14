#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel: A unittest class for BaseModel.

    This class contains a set of unit tests for
    the BaseModel class
    in the 'models.base_model' module.
    """

    def setUp(self):
        """
        setUp: Method called before each test case.
        Initializes a new instance of BaseModel for testing.
        """
        self.model = BaseModel()

    def test_id_is_string(self):
        """
        test_id_is_string: Test case to check if 'id' is a string.
        Asserts whether the 'id' attribute of the BaseModel
        instance is a string.
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """
        test_created_at_is_datetime: Test case to check if
        'created_at' is a datetime.
        Asserts whether the 'created_at' attribute of the
        BaseModel instance is of type 'datetime'.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        test_updated_at_is_datetime: Test case to check
        if 'updated_at' is a datetime.
        Asserts whether the 'updated_at' attribute of the
        BaseModel instance is of type 'datetime'.
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        test_save_updates_updated_at: Test case to check
        if 'save' method updates 'updated_at'.
        Tests if the 'save' method correctly updates
        the 'updated_at' attribute.
        """
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        """
        test_to_dict_returns_dict: Test case to check
        if 'to_dict' returns a dictionary.
        Tests if the 'to_dict' method returns a dictionary.
        """
        result = self.model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_includes_class_name(self):
        """
        test_to_dict_includes_class_name: Test case to check
        if 'to_dict' includes '__class__'.
        Checks if the dictionary returned by 'to_dict'
        contains the key '__class__' with value 'BaseModel'.
        """
        result = self.model.to_dict()
        self.assertIn('__class__', result)
        self.assertEqual(result['__class__'], 'BaseModel')

    def test_to_dict_includes_created_at(self):
        """
        test_to_dict_includes_created_at: Test case to
        check if 'to_dict' includes 'created_at'.
        Checks if the dictionary returned by 'to_dict'
        contains the key 'created_at'.
        """
        result = self.model.to_dict()
        self.assertIn('created_at', result)

    def test_to_dict_includes_updated_at(self):
        """
        test_to_dict_includes_updated_at: Test case
        to check if 'to_dict' includes 'updated_at'.
        Checks if the dictionary returned by 'to_dict'
        contains the key 'updated_at'.
        """
        result = self.model.to_dict()
        self.assertIn('updated_at', result)

    def test_str_format(self):
        """
        test_str_format: Test case to check if '__str__'
        method returns expected string format.
        Tests if the '__str__' method returns the
        expected formatted string.
        """
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)


if __name__ == '__main__':
    unittest.main()
