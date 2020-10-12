class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_it(self):
        print(self.a, self.b, self.c, self.d)

    def as_str(self):
        return f"a = {self.a} b = {self.b}"


class B(A):     #CLASSEN B ARVAR ALLTING SOM CLASSEN A HAR. PLUS ATT CLASSEN B KAN LÖGGA TILL SIN EGNA SAKER OCKSÅ
    def __init__(self, a, b, c, d):
        super().__init__(a, b)      # SUPER betyder att den anropar nånthing i den klassen den arvar ifrån
        self.c = c
        self.d = d

    def as_str(self):
        return f"{super().as_str()} c = {self.c} d = {self.d}"


def main():
    b_obj = B(1, 2, 3, 4)
    b_obj.print_it()
    result = b_obj.as_str()
    print(result)


if __name__ == '__main__':
    main()
