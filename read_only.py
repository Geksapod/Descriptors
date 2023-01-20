"""This module provide access to ReadOnly, CarA and CarB classes"""


class ReadOnly:
    """This class used to set properties read only."""

    def __init__(self, value):
        """Initialisation of the attributes the class ReadOnly."""

        self.value = value

    def __get__(self, instance, owner):

        return self.value

    def __set__(self, instance, value):

        raise AttributeError("Field is read-only")

    def __delete__(self, instance):
        raise AttributeError("Field is read-only")


class CarAudi:
    """
    This class used to represent Audi car.

    Attributes:
        make: Brand of a car.
        model: Model of a car.
        year: Year of manufacture.
    """

    make = ReadOnly("Audi")

    def __init__(self, model, year):
        """
        Initialisation of the attributes the class CarAudi.

        :param model: Model of a car.
        :param year: Year of manufacture.
        """

        self.model = model
        self.year = year

    def __str__(self):
        return f"Car {self.make} {self.model} {self.year}"


class CarBMW:
    """
    This class used to represent BMW car.

    Attributes:
        model = Model of a car.
        year: Year of manufacture.
    Properties:
        make: Brand of a car.
    """

    def __init__(self, make, model, year):
        """
        Initialisation of the attributes the class CarBMW.

        :param make: Brand of a car.
        :param model: Model of a car.
        :param year: Year of manufacture.
        """

        self.__make = make
        self.model = model
        self.year = year

    @property
    def make(self):
        """Setup make as read only property."""
        return self.__make

    @make.setter
    def make(self, item):
        print("Field is read-only")

    @make.deleter
    def make(self):
        print("Field is read-only")

    def __str__(self):
        return f"Car {self.make} {self.model} {self.year}"
