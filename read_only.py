"""This module provide access to ReadOnly, CarA and CarB classes"""


class ReadOnly:
    """This class used to set properties read only."""

    def __init__(self, attribute_name):
        """Initialisation of the attributes the class ReadOnly."""

        self.attribute_name = attribute_name

    def __get__(self, instance, owner):

        return instance.__dict__[self.attribute_name]

    def __set__(self, instance, value):

        if self.attribute_name not in instance.__dict__:
            instance.__dict__[self.attribute_name] = value
        else:
            raise AttributeError("Field is read-only")

    def __delete__(self, instance):
        raise AttributeError("Field is read-only")


class Car:
    """
    This class used to represent Audi car.

    Attributes:
        make: Brand of a car.
        model: Model of a car.
        year: Year of manufacture.
    """

    make = ReadOnly("make")

    def __init__(self, make, model, year):
        """
        Initialisation of the attributes the class CarAudi.

        :param model: Model of a car.
        :param year: Year of manufacture.
        """
        self.make = make
        self.model = model
        self.year = year


    def __str__(self):
        return f"Car {self.make} {self.model} {self.year}"
