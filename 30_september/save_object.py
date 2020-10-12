import pickle
from person import Person


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    p1 = Person("Anna", 34)
    p2 = Person("Pelle", 56)

    print(p1.name, p1.age)
    print(p2.name, p2.age)

    with open("persons.dat", "wb") as person_file:
        pickle.dump(p1, person_file)
        pickle.dump(p2, person_file)


if __name__ == '__main__':
    main()
