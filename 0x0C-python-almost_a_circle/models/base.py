#!/usr/bin/python3

''' file/module base
'''
import json


class Base:
    '''class: Base
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' method: __init__
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        '''method: save_to_file
        accepts: list of objects that inherit from  base class
        writes JSON representation to file in following format:
        '''
        # from objects, build dict representations and put them in a new list
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                tmp_dict = cls.to_dictionary(obj)
                list_dicts.append(tmp_dict)
            json_L_of_D = cls.to_json_string(list_dicts)
        else:
            json_L_of_D = "[]"

        filename = cls.__name__ + ".json"

        with open(filename, "w") as file:
            num_char = file.write(json_L_of_D)

    @classmethod
    def load_from_file(cls):
        '''method: load_from_file
        accepts: class type - based on class name, create filename and loads
             JSON representation of a list of objects
        returns: list of objects/instances
        '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_str = f.read()
            dict_list = cls.from_json_string(json_str)
        except:
            dict_list = []

        # create list of objects
        list_of_objs = []
        for a_dict in dict_list:
            list_of_objs.append(cls.create(**a_dict))
        return list_of_objs

    @classmethod
    def create(cls, **dictionary):
        ''' method: create
        accepts: dictionary as kwargs
        returns: instance with all attributes set
        '''
        if cls.__name__ == 'Rectangle':
            obj = cls(111, 222)
        elif cls.__name__ == 'Square':
            obj = cls(666)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def from_json_string(json_string):
        '''method: from_json_string
        accepts: json_string (string representing a list of dictionaries)
        returns: Python Object representation of JSON string
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' method: to_json_string
        accepts: list_dictionaries  (list of dictionaries)
        returns: JSON string representation list_dictionaries
        '''
        ret_list = []
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if type(list_dictionaries) != list:
            ret_list.append(list_dictionaries)
        else:
            ret_list = list_dictionaries
        return json.dumps(ret_list)
