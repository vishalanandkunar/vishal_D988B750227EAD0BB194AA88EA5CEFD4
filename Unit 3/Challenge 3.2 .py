def sort_students(students):
    students.sort(key=lambda x: x.cgpa, reverse=True)

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

students_list = [
    Student("John", "A001", 3.9),
    Student("Jane", "A002", 3.5),
    Student("Mike", "A003", 3.7),
    Student("Sarah", "A004", 3.8)
]

print("Unsorted List:")
for student in students_list:
    print(student.name, student.roll_number, student.cgpa)

sort_students(students_list)

print("\nSorted List:")
for student in students_list:
    print(student.name, student.roll_number, student.cgpa)
