import read_only as ro
import integers_only as io
import time_prop as tp

if __name__ == "__main__":

    # Task 1

    print(f"{'Task #1':-^60}")

    try:
        car_1 = ro.CarAudi("A4", 2015)
        print(car_1)
        print(car_1.make)
        # del car_1.make
        # print(car_1.make)
        car_1.make = "test"
        print(car_1.make)

    except AttributeError as error:
        print(error)

    # Or
    print()

    try:
        car_2 = ro.CarBMW("BMW", "3", 2017)
        print(car_2)
        print(car_2.make)
        # del car_2.make
        # print(car_2.make)
        car_2.make = "test"
        # print(car_2.make)
        # print()

    except AttributeError as error:
        print(error)

    # Task 2

    print(f"{'Task #2':-^60}")

    try:

        num_1 = io.Numbers(1, 5)
        # num_2 = io.Numbers(5, "2")
        print(num_1.number_1, num_1.number_2, sep=", ")
        print()

    except ValueError as error:
        print(error)

    # Task 3

    print(f"{'Task #3':-^60}")
    print("See \"Property_init.txt\"")

    test_3 = tp.A("Testing property")
    test_3.prop = "New property"

    help(ro)
