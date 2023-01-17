
class Numbers:

    def __init__(self, number_1, number_2):

        self.number_1 = number_1
        self.number_2 = number_2

    def __setattr__(self, key, value):

        if isinstance(value, int):
            self.__dict__[key] = value
        else:
            raise ValueError("The value must be an integer")
