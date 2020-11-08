import pandas as pd
from matplotlib import pyplot   #det gör att man kan se de in en diagram eller grafiskt
from dataclasses import make_dataclass

#class Person
Person = make_dataclass("Person", [
    ('age', int),
    ('height', float),
    ('weight', float),
    ('chest', float),
    ('size', str),
    ('color', str)
], namespace={

    '__str__': lambda self: f'{self.age}, {self.height}, {self.weight}, {self.chest},{self.size}, {self.color} \n'
})

def prepare_data():
    pass

def main():
    p1 = Person(233, 167, 64, 123, "Small", "red")
    print(p1)


if __name__ == '__main__':
    main()
