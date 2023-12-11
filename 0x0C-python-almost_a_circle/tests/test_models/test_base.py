#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):
    """Definition of test class of Base"""

    def setUp(self):
        """Method that execute before each Test"""
        Base._Base__nb_objects = 0

    def test_id_None(self):
        """Test id Base attribute with None initialization"""
        baseTest = Base()
        self.assertEqual(baseTest.id, 1)

    def test_base_list_id(self):
        """Test Base with list id"""
        self.assertEqual(Base([1, 5]).id, [1, 5])

    def test_base_boolean_id(self):
        """Test Base with Boolean id"""
        self.assertEqual(Base(False).id, False)

    def test_id_with_value(self):
        """Test id Base attribute with value"""
        baseTest = Base(5)
        self.assertEqual(baseTest.id, 5)

    def test_access_nb_objects(self):
        """Test access to the private class attribute __nb_objects"""
        baseTest = Base()
        with self.assertRaises(AttributeError):
            print(baseTest.__nb_objects)

    def test_multiple_instance(self):
        """Test multiple instances without setting id value"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
        base3.id = 5
        self.assertEqual(base3.id, 5)

    def test_mix_instances(self):
        """Test with multiple mix Base instances"""
        base1 = Base()
        base2 = Base(91)
        base3 = Base()
        base4 = Base(99)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 91)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, 99)

    def test_multiple_args(self):
        """Test instanciate Base with multiple args"""
        with self.assertRaises(TypeError):
            baseTest = Base(5, 8)

    def test_with_string_val(self):
        """Test instanciate Base with a String value"""
        baseTest = Base("1991")
        self.assertEqual(baseTest.id, "1991")

    def test_to_json_string(self):
        """Test to_json_string method of Base"""
        r1 = Rectangle(10, 7, 2, 8)
        dic = r1.to_dictionary()
        json_dic = Base.to_json_string([dic])
        expected = "[{}]\n".format(dic.__str__())
        with patch("sys.stdout", new=StringIO()) as out:
            print(json_dic)
            self.assertEqual(out.getvalue(), expected.replace("'", "\""))
        self.assertIs(type(json_dic), str)
        self.assertIs(type(dic), dict)

    def test_to_json_string_without_args(self):
        """Test to_json_string method without args"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_None(self):
        """Test to_json_string method with None arg"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string method with empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")
