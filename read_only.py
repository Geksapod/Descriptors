

class ReadOnly:

    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        raise AttributeError("Field is read-only")

    def __delete__(self, instance):
        raise AttributeError("Field is read-only")


class CarA:

    vin = ReadOnly("wVWZZZ3CZEE140287")

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Car {self.make} {self.model} {self.year}"


class CarB:

    def __init__(self, make, model, year, vin):
        self.make = make
        self.model = model
        self.year = year
        self.__vin = vin

    @property
    def vin(self):
        return self.__vin

    @vin.setter
    def vin(self, item):
        pass

    @vin.deleter
    def vin(self):
        pass

    def __str__(self):
        return f"Car {self.make} {self.model} {self.year}"
