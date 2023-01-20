"""This module provide access to A class"""

import time
from typing import Callable, Any, Hashable


class A:
    """
    This class used to write names of properties and times when the properties were set up.

    Attributes:
        time_set_attr: Time when property was set up.
        prop: Property of the class.
    """

    time_set_attr = ""

    def __init__(self, prop):
        """
        Initialisation of the attributes the class Numbers.

        :param prop: Property of the class.
        """

        self.prop = prop

    @staticmethod
    def time_dec(method: Callable[[object, Hashable, Any], Any]):
        """
        Calculate time when method was executed.
        This static method used to decorate method.
        """

        def time_dec_inner(*args, **kwargs):

            A.time_set_attr = time.ctime(time.time())

            return method(*args, **kwargs)

        return time_dec_inner

    @staticmethod
    def write_prop(method: Callable[[object, Hashable, Any], Any]):
        """
        Write in txt file name of the method and time when the method was executed.
        This static method used to decorate method.
        """

        def write_prop_inner(*args, **kwargs):
            res = method(*args, **kwargs)
            with open("Property_init.txt", "a") as f:
                f.write(f"{res} {A.time_set_attr}\n")
                return res

        return write_prop_inner

    @write_prop
    @time_dec
    def __setattr__(self, key, value):

        self.__dict__[key] = value
        return value
