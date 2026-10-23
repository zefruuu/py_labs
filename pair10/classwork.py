class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

person = Person("Alice", 30)
print(person.name)


class student(Person):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group

class teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Subject: {self.subject}"

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def info(self):
        return f"Course: {self.name}, Teacher: {self.teacher.name}, Students: {[s.name for s in self.students]}"

teacher = teacher("Charlie", 40, "Math")
print(teacher.name)
print(teacher.subject)
print(teacher.info())

student = student("Bob", 20, "A")
print(student.name)
print(student.group)
print(student.info())

person = [Person("Alice", 30), student("Bob", 20, "A"), teacher("Charlie", 40, "Math"), student("Ivan", 25, "B")]
for p in person:
    print(p.info())

print(isinstance(person, list))
