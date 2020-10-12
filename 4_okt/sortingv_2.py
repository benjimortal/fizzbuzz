class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"


def comp(person):
    return person.age


def main():
    p1 = Person("Pia", 45)
    p2 = Person("Lars", 34)
    p3 = Person("Ove", 67)
    p4 = Person("Stina", 27)
    p5 = Person("Anna", 39)

    people = [p1, p2, p3, p4, p5]
    new_people = sorted(people, key=lambda p: p.age)
    for person in new_people:
        print(person)
        print("________")

    people.sort(key=comp, reverse=True)
    for person in people:
        print(person)
        print("________")



if __name__ == '__main__':
    main()

