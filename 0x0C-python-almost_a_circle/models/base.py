#!/usr/bin/python3
"""Define Base class"""
import json
import os
import csv


class Base:
    """Definition of Base class

    class attributes:
        nb_objects: nbr of instances
    instance atrributes:
        id: Base identifier

    static methods:
        to_json_string :
            * args : list_dictionaries
            * returns the JSON string representation
                of list_dictionaries
        from_json_string :
            * args : json_string
            * returns the list of the JSON string
                representation json_string

    class methods:
        save_to_file :
            * args : cls, list_objs
            * writes the JSON string representation of
                list_objs to a file
        create :
            * args : cls, **dictionary
            * returns an instance with all attributes
                already set
        load_from_file :
            * args : cls
            *  returns a list of instances
        save_to_file_csv :
            * args : cls, list_objs
            * serializes in CSV
        load_from_file_csv :
            * args : cls
            * deserializes in CSV
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base attributes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        print_str = ""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            print_str = "[]"
        else:
            list_dict = []
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
            print_str = cls.to_json_string(list_dict)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(print_str)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 2)
        else:
            new = cls(3)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r", encoding="utf-8") as file:
            str_file = file.read()

        list_dict = cls.from_json_string(str_file)
        return [cls.create(**dic) for dic in list_dict]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            attrs = ["id", "width", "height", "x", "y"]
            attrs_vals = [0, 0, 0, 0, 0]
        else:
            attrs = ["id", "size", "x", "y"]
            attrs_vals = [0, 0, 0, 0]

        rows = []

        if list_objs is None:
            pass
        else:
            for obj in list_objs:
                for key in range(len(attrs)):
                    attrs_vals[key] = obj.to_dictionary()[attrs[key]]
                rows.append(attrs_vals[:])

        with open(filename, "w") as csv_file:
            csvwriter = csv.writer(csv_file)
            csvwriter.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize in CSV"""
        filename = cls.__name__ + ".csv"

        if os.path.exists(filename) is False:
            return []

        with open(filename, "r") as csv_file:
            read = csv.reader(csv_file)
            list_csv = list(read)

        if cls.__name__ == "Rectangle":
            attrs = ["id", "width", "height", "x", "y"]
        else:
            attrs = ["id", "size", "x", "y"]

        rows = []

        for elemt in list_csv:
            csv_dict = {}
            for key in enumerate(elemt):
                csv_dict[attrs[key[0]]] = int(key[1])
            rows.append(csv_dict)

        list_output = []

        for i in range(len(rows)):
            list_output.append(cls.create(**rows[i]))

        return list_output
