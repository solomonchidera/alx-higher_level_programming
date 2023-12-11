#!/usr/bin/python3
"""Define the rectangle class that inherits from Base class"""


from models.base import Base


class Rectangle(Base):
    """Definition of Rectangle class

    instance attributes:
        width: the Rectangle width (Required)
        height: the Rectangle height (Required)
        x, y: define the position of the Rectangle (Optional)
            by default (0, 0)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialise Rectangle Attributes"""
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter of width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter of the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter of the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter of the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter of the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter of the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " ", end="")
            print(self.__width * '#')

    def __str__(self):
        """returns the Rectangle string representation"""
        return "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" \
            + str(self.y) + " - " + str(self.width) + "/" + str(self.height)

    def update(self, *args, **kwargs):
        """update Rectangle attributes with:
            - 1st argument should be the id attribute
            - 2nd argument should be the width attribute
            - 3rd argument should be the height attribute
            - 4th argument should be the x attribute
            - 5th argument should be the y attribute
        """
        if args is not None and len(args) != 0:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        attrs = ["id", "width", "height", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}
