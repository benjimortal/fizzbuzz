class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}:"

    def say_hi(self):
        print(f"Hello I am {self.first_name}!")


class User(Person):
    def __init__(self, first_name, last_name, user_name, password):
        super().__init__(first_name, last_name)
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return f"{super().__str__()} has the username {self.user_name} and has the password: {self.password}"


class Employee(Person):  # den arrvar bara från class Person.
    amount = 1.02

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()} earns {self.salary}"

    def pay_raise(self):
        self.salary *= self.amount   #öka lönen med 2 procent


class Developer(Employee):
    amount = 1.04

    def say_hi(self):
        print(f"Yo, I'm a developer and my name is {self.first_name}")


def main():
    u1 = User("Jawid", "Mortazawi", "jawidskim", "lle1234")
    print(u1.first_name)

    e1 = Employee("Marielle", "Grosvernier", 38000)
    e2 = Employee("Irene", "Grosvernier", 32000)
    e3 = Employee("Jawid", "Mortazawi", 45000)
    u2 = User("Reyhaneh", "Sadeghi", "anishtain", "sja1234")
    d1 = Developer("Mohammad", "Mortazawi", 39000)

    people = [e1, e2, e3, u2, d1]
    for person in people:
        person.say_hi()
    """print(e1)
    print(e2)
    print(e3)
    #print(u2)
    print(d1)
    e1.pay_raise()
    e2.pay_raise()
    e3.pay_raise()
    d1.pay_raise()
    print(e1)
    print(e2)
    print(e3)
    print(d1)"""



    """if isinstance(e1, User):
        print("Is a user!")
    else:
        print("Is not a user!")

    if isinstance(e1, Person):
        print("Is a Person!")
    else:
        print("Is not!")

    if isinstance(u1, User):
        print("User!")
    else:
        print("Is not a user!")

    if isinstance(u1, Person):
        print("Is a Person!")
    else:
        print("Is not!")"""


if __name__ == '__main__':
    main()
