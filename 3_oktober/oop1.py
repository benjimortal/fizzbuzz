class Point(object):
    def __init__(self, x, y, name, x_step, y_step):
        self.x = x
        self.y = y
        self.name = name
        self.x_step = x_step
        self.y_step = y_step


    def __repr__(self):
        return f"Point({self.x}, {self.y})" #den h'r metoden är för programmerare som kan se output som den koden : Point(10, 15)

    def __str__(self):
        return f"A Point object with x = {self.x} and y= {self.y}"  #den här metoden är för användaren

    def __add__(self, other):  # en method som heter magicmethod
        print(repr(self), "=>", repr(other))
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return Point(self.x // other.x, self.y // other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def main():
    p1 = Point(10, 15)
    p2 = Point(10, 17)
    p3 = Point(10, 17)

    print(repr(p1))
    print(str(p1))

    p4 = p1 + p2 * p3
    print(p4)

    if p1 == p2:
        print("Lika")
    else:
        print("Inte lika")

    if p2 == p3:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
