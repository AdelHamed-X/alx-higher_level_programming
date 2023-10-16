#!/usr/bin/python3
"""
This module has a student class
"""


class Student:
    """class Student"""
    def __init__(self, first_name, last_name, age):
        """
        instantiation with attr
        :param first_name: frst name
        :param last_name: last name
        :param age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """
        retrieves dict representation of an instance
        :return: dict
        """

        if isinstance(attr, list) and \
                all(isinstance(ele, str) for ele in attr):
            return {k: getattr(self, k) for k in attr if hasattr(self, k)}

        return self.__dict__
