from typing import List

class Person:
    def __init__(self, other):
        return Person()


def add(a:float, b:float) ->float:
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError("arguments a and b must be of type int or float")

    """" Function that adds tow numbers
    :param a: float or int, first number to add
    :param b: float or int, second number to add
    :return: float or int"""
    return a + b
def hepp(values: list[int]):
    """return :None"""
    pass
def main():
    print(hepp())
    print(add(2, 3))
    print(add(2.6, 3.4))
    """"
    print(add("2", "3"))
    print(add([1, 2, 3], [4, 5, 6]))
    print(add(True, False))
    """


    """p1 = Person
    p2 = Person
    print(add(p1, p2))"""


if __name__ == '__main__':
    main()
