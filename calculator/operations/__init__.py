
""" These are the Operation Classes"""


class Addition: # pylint: disable=too-few-public-methods
    """ This is the addition class"""

    # this defines a static method that you can use without instantiating the calculator class
    # If you can go to the store and buy it, it is an object.
    # If you can't buy it then its a static method
    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return value_1 + value_2


class Subtraction: # pylint: disable=too-few-public-methods
    """ This is the subtraction class"""

    @staticmethod
    def subtract(value_1, value_2):
        """ This is the add method"""
        return value_1 - value_2


class Multiplication: # pylint: disable=too-few-public-methods
    """ This is the subtraction class"""

    @staticmethod
    def multiply(value_1, value_2):
        """ This is the add method"""
        return value_1 * value_2
