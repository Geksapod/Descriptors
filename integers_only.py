"""This module provide access to Numbers class"""


class Numbers:
    """This class used to store only integer numbers."""

    def __init__(self, number_1: int, number_2: int):
        """Initialisation of the attributes the class Numbers."""

        self.number_1 = number_1
        self.number_2 = number_2

    def __setattr__(self, key: str, value: int):

        if isinstance(value, int):
            self.__dict__[key] = value
        else:
            raise ValueError("The value must be an integer")
