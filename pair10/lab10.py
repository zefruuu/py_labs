import os
#1

class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Name: {self.name}."

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        return f"Name: {self.name}, Group: {self.group}."

    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
        else:
            print("Invalid grade. Please enter a grade between 1 and 12.")

    def average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

# student1 = Student("Anna", "10-IT")
# student2 = Student("Ivan", "10-IT")
# print(student1.info())
# print(student2.info())

#2

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"Teacher: {self.name}, Subject: {self.subject}."

# list = [Person("Anna"), Student("Ivan", "10-IT"), Teacher("Ivan Komarov", "IT")]
# for p in list:
#     print(p.info())


class Course:
    def __init__(self, title, teacher, students):
        self.title = title
        self.teacher = teacher
        self.students = students

    def add_student(self, new_student):
        for student in self.students:
            if student.name == new_student.name:
                print(f"Student {new_student.name} is already in the course.")
                return
        self.students.append(new_student)
    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break
    def show_students(self):
        return [student.name for student in self.students]

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None
    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)
        if student:
            student.add_grade(grade)
        else:
            print(f"Student {name} not found in the course.")

    def show_rating(self):
        students_list = list(self.students)
        n = len(students_list)

        for i in range(n):
         for j in range(0, n - i - 1):
            if students_list[j].average() < students_list[j + 1].average():
                 students_list[j], students_list[j + 1] = students_list[j + 1], students_list[j]

        result = []
        for student in students_list:
            result.append((student.name, student.average()))

        return result

Math = Course("Math", Teacher("Mykhailo Tadlia", "Math"), [Student("Anna", "10-IT"), Student("Ivan", "10-IT")])


Math.add_student(Student("Artem", "10-IT"))
Math.add_student(Student("Iliya", "10-IT"))
Math.add_student(Student("Matvii", "10-IT"))
Math.add_student(Student("Olexander", "10-IT"))
Math.add_student(Student("Dmytro", "10-IT"))
Math.add_student(Student("Anna", "10-IT"))
Math.remove_student("Anna")

print(Math.show_students())


user_choice = input("Menu:\n1 - Show course\n2 - Add student\n3 - Remove student\n4 - Find student\n5 - Add grade to student\n6 - Show rating\n7 - Save data\n0 - Exit\nChoose an option: ")

if int(user_choice) == 1:
    print(f"Course: {Math.title}, Teacher: {Math.teacher.name}, Subject: {Math.teacher.subject}")
    print("Students:", Math.show_students())
if int(user_choice) == 2:
    name = input("Enter student name: ")
    group = input("Enter student group: ")
    Math.add_student(Student(name, group))
    print(f"Student {name} added.")
if int(user_choice) == 3:
    name = input("Enter student name to remove: ")
    Math.remove_student(name)
    print(f"Student {name} removed.")
if int(user_choice) == 4:
    name = input("Enter student name to find: ")
    student = Math.find_student(name)
    if student:
        print(f"Found student: {student.info()}")
    else:
        print(f"Student {name} not found.")
if int(user_choice) == 5:
    name = input("Enter student name to add grade: ")
    grade = int(input("Enter grade (1-12): "))
    Math.add_grade_to_student(name, grade)
    print(f"Grade {grade} added to student {name}.")
if int(user_choice) == 6:
    rating = Math.show_rating()
    print("Rating:")
    for student_name, avg in rating:
        print(f"{student_name}: {avg:.2f}")
if int(user_choice) == 7:

    data = {
        "title": Math.title,
        "teacher": {
            "name": Math.teacher.name,
            "subject": Math.teacher.subject
        },
        "students": [
            {
                "name": student.name,
                "group": student.group,
                "grades": student.grades
            } for student in Math.students
        ]
    }
    if not os.path.exists("data"):
        with open("data.txt", "w", encoding="utf-8") as f:
            f.write(str(data))

    print("Data saved to course_data.txt.")