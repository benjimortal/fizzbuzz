class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    def __str__(self):
        return f"A Point object with x = {self.x} and y = {self.y}"
def main():
    p1 = Point(10, 15)
    p2 = Point(20, 25)
    print(p1)


if __name__ == '__main__':
    main()
