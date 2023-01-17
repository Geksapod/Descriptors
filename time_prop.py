import time


class A:

    def __init__(self, prop):
        self.prop = prop

    @staticmethod
    def time_dec(method):

        def time_dec_inner(*args, **kwargs):
            return time.ctime(time.time()), method(*args, **kwargs)

        return time_dec_inner

    @staticmethod
    def write_prop(method):

        def write_prop_inner(*args, **kwargs):
            a, b = method(*args, **kwargs)
            with open("Property_init.txt", "a") as f:
                f.write(f"{b} {a}\n")
                return method(*args, **kwargs)

        return write_prop_inner

    @write_prop
    @time_dec
    def __setattr__(self, key, value):

        self.__dict__[key] = value
        return value
