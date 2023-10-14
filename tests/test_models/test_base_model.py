#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def test_id_is_string(self):
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict_returns_dict(self):
        result = self.model.to_dict()
        self.assertIsInstance(result, dict)

    def test_to_dict_includes_class_name(self):
        result = self.model.to_dict()
        self.assertIn('__class__', result)
        self.assertEqual(result['__class__'], 'BaseModel')

    def test_to_dict_includes_created_at(self):
        result = self.model.to_dict()
        self.assertIn('created_at', result)

    def test_to_dict_includes_updated_at(self):
        result = self.model.to_dict()
        self.assertIn('updated_at', result)

    def test_str_format(self):
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)


if __name__ == '__main__':
    unittest.main()
