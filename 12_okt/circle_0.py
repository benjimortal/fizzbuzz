from math import pi


def circle_area(r: float):
    if r < 0:
        raise ValueError("The radius can not be negative")
    if type(r) not in (int, float):
        raise TypeError("The radius must be of type int or float")
    return pi * (r**2)


def main():
    print(circle_area(1))
    print(circle_area(0))
    print(circle_area(10))
    print(circle_area(-10))
    print(circle_area(True))
    print(circle_area(2 + 5j))
    print(circle_area('radius'))


if __name__ == '__main__':
    main()
