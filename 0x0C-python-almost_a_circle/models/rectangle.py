#!/usr/bin/python3

''' module: rectangle
'''

from models.base import Base


class Rectangle(Base):
    '''class: Rectangle
    '''
    KV_dict = {'id': 'id', 'width': '_Rectangle__width',
               'height': '_Rectangle__height',
               'x': '_Rectangle__x', 'y': '_Rectangle__y'}

    def __init__(self, width, height, x=0, y=0, id=None):
        '''method: __init__
        rectangle instantiator
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def update(self, *args, **kwargs):
        '''method: update
        accepts variable length list of class attributes, updates attributes
        no return value
        '''
        key_list = ['id', '_Rectangle__width', '_Rectangle__height',
                    '_Rectangle__x', '_Rectangle__y']
        KV_dict = {'id': 'id', 'width': '_Rectangle__width',
                   'height': '_Rectangle__height',
                   'x': '_Rectangle__x', 'y': '_Rectangle__y'}
        for idx, el in enumerate(args):
            self.__dict__[key_list[idx]] = el
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__dict__[KV_dict[key]] = val

    def __str__(self):
        '''method: __str__
        returns pretty representation of Rectangle object
        '''

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def area(self):
        '''public_method: area
        returns area of rectangle
        '''
        return self.__width * self.__height

    def display(self):
        '''public method: display
        prints ascii respresentation of a rectangle to stdout
        '''
        print("\n" * (self.__y), end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def integer_GT_zero(self, name, value):
        '''public_method: integer_GT_zero
        validates value is int > zero
        name: always a string
        value: positive integer
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def integer_GTE_zero(self, name, value):
        '''public_method: integer_GTE_zero
        validates value is int >= zero
        name: always a string
        value: positive integer, or ZERO
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        ''' method: width getter
        '''
        return self.__width

    @width.setter
    def width(self, width):
        '''method: width setter
        '''
        self.integer_GT_zero("width", width)
        self.__width = width

    @property
    def height(self):
        ''' method: height getter
        '''
        return self.__height

    @height.setter
    def height(self, height):
        ''' method: height getter
        '''
        self.integer_GT_zero("height", height)
        self.__height = height

    @property
    def x(self):
        ''' method: x getter
        '''
        return self.__x

    @x.setter
    def x(self, x):
        ''' method: x setter
        '''
        self.integer_GTE_zero("x", x)
        self.__x = x

    @property
    def y(self):
        ''' method y getter
        '''
        return self.__y

    @y.setter
    def y(self, y):
        ''' method y setter
        '''
        self.integer_GTE_zero("y", y)
        self.__y = y

    def to_dictionary(self):
        ''' method: to_dictionary
        accepts: instance of Rectangle class (an object)
        return dict representation of Rectangle object
        '''
        new_dict = {}
        for key, val in Rectangle.KV_dict.items():
            new_dict[key] = self.__dict__[val]
        return new_dict
