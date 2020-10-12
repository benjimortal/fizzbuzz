class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.firstname} {self.lastname} is {self.age} years old,\n" \
               f"and get {self.salary} in salary evry singel month!"


def comp(employee):
    return employee.age or employee.salary

def main():

    e1 = Employee("Jawid", "Mortazawi", 24, 40000)
    e2 = Employee("Mohammad", "Mortazawi", 20, 30000)
    e3 = Employee("Hassan", "Sadeghi", 28, 50000)
    e4 = Employee("Hossein", "Sadeghi", 26, 40000)
    e5 = Employee("Mustafa", "Rezaei", 23, 40000)

    employee = [e1, e2, e3, e4, e5]

    employee.sort(key=comp)
    for person in employee:
        print(person)
        print("___________________________________________")


if __name__ == '__main__':
    main()
