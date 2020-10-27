class Student:
    def __init__(self, name, age, grade):
        self.name =name
        self.age = age
        self.grade = grade


    def get_grade(self):
        return self.grade


class Curse:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.studenst = []
        self.is_active = False


    def add_student(self, student):
        if len(self.studenst) < self.max_students:
            self.studensts.append(student)
            return True
        return False

    def get_average_grade(self):
        pass

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 64)


def main():
    s = Student



if __name__ == '__main__':
    main()
