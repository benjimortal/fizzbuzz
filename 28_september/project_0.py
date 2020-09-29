marks = {}

for i in range(10):
    student_name = input("Enter student's name: ")
    student_mark = input("Enter student's mark: ")


marks = {student_name.title():student_mark}

print(marks)