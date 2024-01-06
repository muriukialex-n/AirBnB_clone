#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up an instance of BaseModel for testing"""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        """Clean up after each test case"""
        del self.my_model

    def test_str_method(self):
        """Test the __str__ method of BaseModel"""
        expected_str = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save_method(self):
        """Test the save method of BaseModel"""
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel"""
        my_model_json = self.my_model.to_dict()
        self.assertTrue(isinstance(my_model_json, dict))
        self.assertIn("__class__", my_model_json)
        self.assertEqual(my_model_json["__class__"], "BaseModel")
        self.assertIn("created_at", my_model_json)
        self.assertIn("updated_at", my_model_json)
        self.assertIn("id", my_model_json)
        self.assertIn("name", my_model_json)
        self.assertIn("my_number", my_model_json)

    def test_to_dict_datetime_format(self):
        """Test the format of datetime in to_dict method"""
        my_model_json = self.my_model.to_dict()
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(my_model_json["created_at"], self.my_model.created_at.strftime(datetime_format))
        self.assertEqual(my_model_json["updated_at"], self.my_model.updated_at.strftime(datetime_format))

    def test_to_dict_attributes_types(self):
        """Test the types of attributes in to_dict method"""
        my_model_json = self.my_model.to_dict()
        self.assertEqual(type(my_model_json["name"]), str)
        self.assertEqual(type(my_model_json["my_number"]), int)


if __name__ == '__main__':
    unittest.main()
