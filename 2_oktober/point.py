class Point:
    def __init__(self, x, y, name, x_step, y_step):
        self.x = x
        self.y = y
        self.name = name
        self.x_step = x_step
        self.y_step = y_step

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"name = {self.name}, x = {self.x}, y = {self.y}, x_step = {self.x_step}, y_step = {self.y_step}"

    def __add__(self, other):
        print(repr(self), "+", repr(other))
        return Point(self.x + other.x, self.y + other.y, "Noname", 0, 0)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y



def main():
    p1 = Point(10, 15, "Point 1", -5, 6)
    p2 = Point(10, 15, "Point 2", 10, -3)

    p3 = p1 + p2
    print(p3)



if __name__ == '__main__':
    main()