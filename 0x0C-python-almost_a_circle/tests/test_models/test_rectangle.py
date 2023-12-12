#!/usr/bin/python3
"""Test Cases for Rectangle class"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
import os


class TestRectangle(unittest.TestCase):
    """Test Class for Rectangle"""

    def setUp(self):
        """method that will be executed before each Test case"""
        Base._Base__nb_objects = 0

    def test_rectangle_without_position(self):
        """Create a Rectangle without setting the position and the id"""
        rec1 = Rectangle(5, 7)
        self.assertEqual(rec1.width, 5)
        self.assertEqual(rec1.height, 7)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec1.id, 1)

    def test_rectangle_instance(self):
        """Create an instance of Rectangle by setting a value to
        all attributes
        """
        rec1 = Rectangle(2, 4, 0, 0, 1991)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 4)
        self.assertEqual(rec1.x, 0)
        self.assertEqual(rec1.y, 0)
        self.assertEqual(rec1.id, 1991)

    def test_multiple_instance(self):
        """Create multiple Rectangles"""
        rec1 = Rectangle(2, 8, 1, 2)
        rec2 = Rectangle(3, 6, 0, 2, 31)
        rec3 = Rectangle(4, 7, 1, 0)
        self.assertEqual(rec1.width, 2)
        self.assertEqual(rec1.height, 8)
        self.assertEqual(rec1.x, 1)
        self.assertEqual(rec1.y, 2)
        self.assertEqual(rec1.id, 1)
        self.assertEqual(rec2.id, 31)
        self.assertEqual(rec3.id, 2)

    def test_access_width(self):
        """Check the access to the private attribute width"""
        with self.assertRaises(AttributeError):
            self.__width

    def test_access_height(self):
        """Check the access to the private attribute height"""
        with self.assertRaises(AttributeError):
            self.__height

    def test_access_x(self):
        """Check the access to the private attribute x"""
        with self.assertRaises(AttributeError):
            self.__x

    def test_access_y(self):
        """Check the access to the private attribute y"""
        with self.assertRaises(AttributeError):
            self.__y

    def test_typeError_raise_width(self):
        """Test raises of TypeError when width value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(False, 8, 2, 6)

        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_typeError_raise_height(self):
        """Test raises of TypeError when height value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, {"height": 5}, 0, 3)
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_typeError_raise_x(self):
        """Test raises of TypeError when x value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 3, (1, 1), 1)
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_typeError_raise_y(self):
        """Test raises of TypeError when y value is not integer"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(1, 6, 0, [3, 0])
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_typeError_raise_width_float(self):
        """Test raises of TypeError when width value is a float"""
        with self.assertRaises(TypeError) as ctx:
            Rectangle(2.5, 1, 9, 7)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_valueError_raise_width(self):
        """Test raises of ValueError when width value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(-1, 2, 6, 7, 33)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_valueError_zero_width(self):
        """Test raises of ValueError when width value is 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(0, 2, 6, 7, 33)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_valueError_raise_height(self):
        """Test raises of ValueError when height value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(3, -4, 9, 4, 66)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_valueError_zero_height(self):
        """Test raises of ValueError when height value is 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(3, 0, 9, 4, 66)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_valueError_raise_x(self):
        """Test raises of ValueError when x value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 4, -7, 2, 91)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_valueError_raise_y(self):
        """Test raises of ValueError when y value is less than 0"""
        with self.assertRaises(ValueError) as ctx:
            Rectangle(1, 4, 2, -1, 12)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_typeError_more_args(self):
        """Test instanciate Rectangle with the wrong number of arguments"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 91, 7)

    def test_rectangle_with_no_args(self):
        """Test instanciate Rectangle without args"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rectangle_with_1_arg(self):
        """Test instanciate Rectangle with one arg"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_area(self):
        """Test the calcul of the rectangle area"""
        rec = Rectangle(10, 5, 0, 1, 91)
        self.assertEqual(rec.area(), 50)

    def test_area_without_set_position(self):
        """Instanciate Rectangle without setting x and y than
        call area method"""
        rec = Rectangle(5, 3)
        self.assertEqual(rec.area(), 15)

    def test_area_with_change_args(self):
        """Test area with changing width and height"""
        rec = Rectangle(4, 6)
        self.assertEqual(rec.area(), 24)
        rec.width = 5
        self.assertEqual(rec.area(), 30)
        rec.height = 2
        self.assertEqual(rec.area(), 10)
        rec.width = 7
        rec.height = 3
        self.assertEqual(rec.area(), 21)

    def test_area_with_args(self):
        """Call area method with arguments"""
        rec = Rectangle(2, 4, 2, 1)
        with self.assertRaises(TypeError):
            rec.area(2, 5)

    def test_display(self):
        """Test display rectangle method"""
        rec = Rectangle(2, 4, 0, 3, 12)
        expectedOutput = "\n\n\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), expectedOutput)

    def test_display_with_changing(self):
        """Test display rectangle method with changing args"""
        rec = Rectangle(2, 3)
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "##\n##\n##\n")
        rec.width = 4
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "####\n####\n####\n")
        rec.height = 2
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "####\n####\n")
        rec.height = 1
        rec.width = 5
        with patch('sys.stdout', new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "#####\n")

    def test_display_with_args(self):
        """Test calling display method with arguments"""
        rec = Rectangle(2, 4)
        with self.assertRaises(TypeError):
            rec.display(55)

    def test_str(self):
        """Test calling str method"""
        rec = Rectangle(4, 6, 2, 1, 12)
        expectedResult = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(rec.__str__(), expectedResult)

    def test_str_without_setting_id(self):
        """Test calling str method without setting the id"""
        rec = Rectangle(2, 3, 1, 2)
        expectedResult = "[Rectangle] (1) 1/2 - 2/3"
        self.assertEqual(rec.__str__(), expectedResult)

    def test_str_without_setting_position(self):
        """Test calling str method without setting x, y and id"""
        rec = Rectangle(5, 2)
        expectedResult = "[Rectangle] (1) 0/0 - 5/2"
        self.assertEqual(rec.__str__(), expectedResult)

    def test_str_with_changes(self):
        """Test calling str method with changing attributes value"""
        rec = Rectangle(3, 4, 1, 7, 91)
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 1/7 - 3/4")
        rec.x = 3
        rec.y = 5
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 3/5 - 3/4")
        rec.width = 6
        rec.height = 5
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 3/5 - 6/5")
        rec.x = 0
        rec.height = 9
        self.assertEqual(rec.__str__(), "[Rectangle] (91) 0/5 - 6/9")

    def test_str_with_args(self):
        """Test calling str method with arguments"""
        rec = Rectangle(3, 4, 1, 0, 91)
        with self.assertRaises(TypeError):
            rec.__str__(2, 7)

    def test_str_multiple_rectangle(self):
        """Test calling str method with multiple
        Rectangles instances
        """
        rec1 = Rectangle(3, 5)
        rec2 = Rectangle(2, 7, 1, 3)
        rec3 = Rectangle(10, 2, 1, 4, 91)
        self.assertEqual(rec1.__str__(), "[Rectangle] (1) 0/0 - 3/5")
        self.assertEqual(rec2.__str__(), "[Rectangle] (2) 1/3 - 2/7")
        self.assertEqual(rec3.__str__(), "[Rectangle] (91) 1/4 - 10/2")

    def test_display_with_handle_position(self):
        """Test display method with handling x and y"""
        rec = Rectangle(5, 2, 4, 2, 3)
        rec1 = Rectangle(7, 3, 2, 0)
        rec2 = Rectangle(10, 2, 0, 4, 91)
        with patch("sys.stdout", new=StringIO()) as out:
            rec.display()
            self.assertEqual(out.getvalue(), "\n\n    #####\n    #####\n")
        with patch("sys.stdout", new=StringIO()) as out:
            rec1.display()
            self.assertEqual(out.getvalue(),
                             "  #######\n  #######\n  #######\n")
        with patch("sys.stdout", new=StringIO()) as out:
            rec2.display()
            self.assertEqual(out.getvalue(),
                             "\n\n\n\n##########\n##########\n")

    def test_update_id(self):
        """Test update method by changing the id attribute"""
        rec = Rectangle(5, 4, 6, 1, 91)
        rec.update(99)
        self.assertEqual(rec.id, 99)
        self.assertEqual(rec.__str__(), "[Rectangle] (99) 6/1 - 5/4")

    def test_update_2_attrs(self):
        """Test update method by changing id and width attributes"""
        rec = Rectangle(5, 4, 6, 1, 91)
        rec.update(99, 10)
        self.assertEqual(rec.id, 99)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.__str__(), "[Rectangle] (99) 6/1 - 10/4")

    def test_update_3_attrs(self):
        """Test update method by changing id, width and
            height attributes
        """
        rec = Rectangle(5, 4, 6, 1, 91)
        rec.update(99, 10, 2)
        self.assertEqual(rec.id, 99)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.__str__(), "[Rectangle] (99) 6/1 - 10/2")

    def test_update_4_attrs(self):
        """Test update method by changing id, width,
            height and x attributes
        """
        rec = Rectangle(5, 4, 6, 1, 91)
        rec.update(99, 10, 2, 2)
        self.assertEqual(rec.id, 99)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.__str__(), "[Rectangle] (99) 2/1 - 10/2")

    def test_update_5_attrs(self):
        """Test update method by changing id, width,
            height, x and y attributes
        """
        rec = Rectangle(5, 4, 6, 1, 91)
        rec.update(99, 10, 2, 2, 0)
        self.assertEqual(rec.id, 99)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.__str__(), "[Rectangle] (99) 2/0 - 10/2")

    def test_update_more_args(self):
        """Test update method with more arguments"""
        rec = Rectangle(5, 4, 6, 1, 91)
        with self.assertRaises(IndexError):
            rec.update(99, 10, 2, 2, 0, 14)

    def test_update_wrong_type_width(self):
        """Test update 2 args with wrong type for the width"""
        rec = Rectangle(10, 2, 3, 4)
        with self.assertRaises(TypeError) as ctx:
            rec.update(32, 3.5)

        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_update_wrong_type_height(self):
        """Test update 3 args with wrong type for the height"""
        rec = Rectangle(5, 4, 1, 0)
        with self.assertRaises(TypeError) as ctx:
            rec.update(10, 7, (1, 'h'))

        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_update_wrong_type_x(self):
        """Test update 4 args with wrong type for x"""
        rec = Rectangle(2, 5)
        with self.assertRaises(TypeError) as ctx:
            rec.update(3, 5, 2, ['H', 'I'])

        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_update_wrong_type_y(self):
        """Test update 5 args with wrong type for y"""
        rec = Rectangle(4, 5)
        with self.assertRaises(TypeError) as ctx:
            rec.update(55, 7, 3, 2, True)

        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_update_width_zero(self):
        """Test update the value of width with 0"""
        rec = Rectangle(5, 3, 1, 7, 66)
        with self.assertRaises(ValueError) as ctx:
            rec.update(10, 0)

        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_update_width_negative(self):
        """Test update the value of width with a negative value"""
        rec = Rectangle(10, 1)
        with self.assertRaises(ValueError) as ctx:
            rec.update(3, -9)

        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_update_height_zero(self):
        """Test update the value of height with 0"""
        rec = Rectangle(4, 7, 0, 3)
        with self.assertRaises(ValueError) as ctx:
            rec.update(87, 6, 0)

        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_update_height_negative(self):
        """Test update the value of height with a negative value"""
        rec = Rectangle(8, 1, 3, 9)
        with self.assertRaises(ValueError) as ctx:
            rec.update(96, 4, -7)

        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_update_x_negative(self):
        """Test update the value of x with a negative value"""
        rec = Rectangle(7, 2, 1, 3, 102)
        with self.assertRaises(ValueError) as ctx:
            rec.update(1991, 2, 3, -5)

        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_update_y_negative(self):
        """Test update the value of y with a negative value"""
        rec = Rectangle(10, 5)
        with self.assertRaises(ValueError) as ctx:
            rec.update(2, 6, 4, 7, -2)

        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_update_without_args(self):
        """Test update without arguments"""
        rec = Rectangle(5, 9)
        rec.update()
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 9)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 1)

    def test_update_multiple(self):
        """Test calling update for the same instance multiple times"""
        rec = Rectangle(3, 7, 9, 1, 1991)
        self.assertEqual(rec.__str__(), "[Rectangle] (1991) 9/1 - 3/7")

        rec.update(85)
        self.assertEqual(rec.__str__(), "[Rectangle] (85) 9/1 - 3/7")

        rec.update(85, 2)
        self.assertEqual(rec.__str__(), "[Rectangle] (85) 9/1 - 2/7")

        rec.update(85, 2, 10)
        self.assertEqual(rec.__str__(), "[Rectangle] (85) 9/1 - 2/10")

        rec.update(85, 2, 10, 3)
        self.assertEqual(rec.__str__(), "[Rectangle] (85) 3/1 - 2/10")

        rec.update(85, 2, 10, 3, 4)
        self.assertEqual(rec.__str__(), "[Rectangle] (85) 3/4 - 2/10")

    def test_update_kwargs_with_args(self):
        """Test passing args and kwargs to update method"""
        rec = Rectangle(1, 2, 0, 0, 5)
        self.assertEqual(rec.__str__(), "[Rectangle] (5) 0/0 - 1/2")
        rec.update(6, 3, 5, 1, 1, height=8, id=32)
        self.assertEqual(rec.__str__(), "[Rectangle] (6) 1/1 - 3/5")

    def test_update_kwargs_width(self):
        """Test updating width value by passing key,value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        rec.update(width=10)
        self.assertEqual(rec.__str__(), "[Rectangle] (96) 3/4 - 10/2")

    def test_update_kwargs_height(self):
        """Test updating height value by passing key, value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        rec.update(height=20)
        self.assertEqual(rec.__str__(), "[Rectangle] (96) 3/4 - 1/20")

    def test_update_kwargd_x(self):
        """Test updating x value by passing key,value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        rec.update(x=7)
        self.assertEqual(rec.__str__(), "[Rectangle] (96) 7/4 - 1/2")

    def test_update_kwargs_y(self):
        """Test updating y value by passing key, value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        rec.update(y=12)
        self.assertEqual(rec.__str__(), "[Rectangle] (96) 3/12 - 1/2")

    def test_update_kwargs_id(self):
        """Test updating id value by passing key, value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        rec.update(id=1991)
        self.assertEqual(rec.__str__(), "[Rectangle] (1991) 3/4 - 1/2")

    def test_update_multi_order_kwargs(self):
        """Test updating multiple attributes in order by passing
        key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        rec.update(id=25, width=6, height=14, x=9, y=10)
        self.assertEqual(rec.__str__(), "[Rectangle] (25) 9/10 - 6/14")

    def test_update_multi_disord_kwargs(self):
        """Test updating multiple attributes not in the order by passing
        key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        rec.update(x=11, id=98, height=8, y=10, width=6)
        self.assertEqual(rec.__str__(), "[Rectangle] (98) 11/10 - 6/8")

    def test_update_kwargs_width_zero(self):
        """Test updating width value to 0 by passing key, value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(ValueError) as ctx:
            rec.update(width=0)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_update_kwargs_width_negative(self):
        """Test updating width value with a negative value
        by passing key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(ValueError) as ctx:
            rec.update(width=-5)
        self.assertEqual(str(ctx.exception), "width must be > 0")

    def test_update_kwargs_wrong_type_width(self):
        """Test updating width value with the wrong type by
        passing key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(TypeError) as ctx:
            rec.update(width=False)
        self.assertEqual(str(ctx.exception), "width must be an integer")

    def test_update_kwargs_height_zero(self):
        """Test updating height value to 0 by passing key, value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(ValueError) as ctx:
            rec.update(height=0)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_update_kwargs_height_negative(self):
        """Test updating height value with a negative value by
        passing key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(ValueError) as ctx:
            rec.update(height=-3)
        self.assertEqual(str(ctx.exception), "height must be > 0")

    def test_update_kwargs_height_wrong_type(self):
        """Test updating height value with a wrong type by passing
        key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(TypeError) as ctx:
            rec.update(height=['Hello', 'HAJAR'])
        self.assertEqual(str(ctx.exception), "height must be an integer")

    def test_update_kwargs_wrong_type_x(self):
        """Test updating x value with a wrong type by passing key, value"""
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(TypeError) as ctx:
            rec.update(x=9.25)
        self.assertEqual(str(ctx.exception), "x must be an integer")

    def test_update_kwargs_negative_x(self):
        """Test updating x value with a negative value by passing
        key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(ValueError) as ctx:
            rec.update(x=-8)
        self.assertEqual(str(ctx.exception), "x must be >= 0")

    def test_update_kwargs_wrong_type_y(self):
        """Test updating y value with a wrong type by passing
        key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(TypeError) as ctx:
            rec.update(y=(2, True))
        self.assertEqual(str(ctx.exception), "y must be an integer")

    def test_update_kwargs_negative_y(self):
        """Test updating y value with a negative value by passing
        key, value
        """
        rec = Rectangle(1, 2, 3, 4, 96)
        with self.assertRaises(ValueError) as ctx:
            rec.update(y=-5)
        self.assertEqual(str(ctx.exception), "y must be >= 0")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        rec = Rectangle(1, 2, 3, 4, 96)
        dic = {'x': 3, 'y': 4, 'id': 96, 'height': 2, 'width': 1}
        self.assertDictEqual(rec.to_dictionary(), dic)

    def test_to_dictionary_minim(self):
        """Test to_dictionary method with a minimum instance"""
        rec = Rectangle(1, 2)
        dic = {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 1}
        self.assertDictEqual(rec.to_dictionary(), dic)

    def test_type_returned_value_dict(self):
        """Test that check the type of the returned value by
        to_dictionary method
        """
        r1 = Rectangle(10, 2, 1, 9)
        self.assertIs(type(r1.to_dictionary()), dict)

    def test_to_dictionary_2(self):
        """Test to_dictionary method by adding some manipulations"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        dic = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dictionary, dic)
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertDictEqual(r2.to_dictionary(), dic)
        self.assertFalse(r1 == r2)

    def test_save_to_file(self):
        """Test save_to_file method for list of rectangles"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        dic1 = r1.to_dictionary()
        dic2 = r2.to_dictionary()
        Rectangle.save_to_file([r1, r2])
        expected = "[{}, {}]\n".format(dic1, dic2)
        with patch("sys.stdout", new=StringIO()) as out:
            with open("Rectangle.json", "r") as file:
                print(file.read())
            self.assertEqual(out.getvalue(), expected.replace("'", "\""))

    def test_save_to_file_None(self):
        """Test save_to_file method with None arg"""
        Rectangle.save_to_file(None)
        with patch("sys.stdout", new=StringIO()) as out:
            with open("Rectangle.json", "r") as file:
                print(file.read())
            self.assertEqual(out.getvalue(), "[]\n")

    def test_from_json_string(self):
        """returns the list of the JSON string representation json_string"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        dic1 = r1.to_dictionary()
        dic2 = r2.to_dictionary()
        list_input = [dic1, dic2]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_save_to_file_empty(self):
        """Test save_to_file method for Rectangle with empty list"""
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        Rectangle.save_to_file([])
        with patch("sys.stdout", new=StringIO()) as out:
            with open("Rectangle.json", "r") as file:
                print(file.read())
            self.assertEqual(out.getvalue(), "[]\n")

    def test_rectangle_to_json_string_empty(self):
        """Test to_json_string for Rectangle with empty list arg"""
        json_str = Rectangle.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_rectangle_to_json_string_None(self):
        """Test to_json_string for Rectangle with None arg"""
        json_str = Rectangle.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_rectangle_from_json_string_None(self):
        """Test from_json_string for Rectangle with None arg"""
        json_list = Rectangle.from_json_string(None)
        self.assertListEqual(json_list, [])

    def test_rectangle_from_json_string_empty(self):
        """Test from_json_string for Rectangle with empty list arg"""
        json_list = Rectangle.from_json_string("")
        self.assertListEqual(json_list, [])

    def test_rectangle_create(self):
        """Test create class method"""
        rec = Rectangle(10, 2)
        dic1 = rec.to_dictionary()
        rec2 = Rectangle.create(**dic1)
        self.assertEqual(rec2.__str__(), "[Rectangle] (1) 0/0 - 10/2")
        self.assertFalse(rec2 == rec)
        self.assertFalse(rec2 is rec)

    def test_rectangle_create_id(self):
        """Test create class method"""
        dictionary = {"id": 1991}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 1991)

    def test_rectangle_create_2_args(self):
        """Test create class method by passing 2 attrs value"""
        dictionary = {"width": 10, "height": 5}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 5)

    def test_rectangle_create_5_args(self):
        """Test create class method by passing 5 attrs values"""
        dictionary = {"width": 5, "x": 9, "y": 3, "height": 2, "id": 91}
        rec = Rectangle.create(**dictionary)
        self.assertEqual(rec.id, 91)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 9)
        self.assertEqual(rec.y, 3)

    def test_rectangle_load_from_file(self):
        """Test load_from_file for Rectangle"""
        r1 = Rectangle(10, 2, 1, 3, 91)
        r2 = Rectangle(4, 5)
        l_input = [r1, r2]
        Rectangle.save_to_file(l_input)
        l_output = Rectangle.load_from_file()
        for i in range(len(l_output)):
            self.assertEqual(l_output[i].__str__(), l_input[i].__str__())

    def test_rectangle_load_from_file_not_exist(self):
        """Test load_from_file method with file doesn't exist"""
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        self.assertListEqual(Rectangle.load_from_file(), [])

    def test_rectangle_load_from_file_with_args(self):
        """Test calling load_from_file with argument"""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file("file")
