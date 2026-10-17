# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def info(self):
#         return f"Rectangle(width={self.width}, height={self.height})"
#
#
# Rectangle1 = Rectangle(5,3)
# Rectangle2 = Rectangle(10,4)
#
# print(Rectangle1.info(), "Area:", Rectangle1.area(), "Perimeter:", Rectangle1.perimeter())
# print(Rectangle2.info(), "Area:", Rectangle2.area(), "Perimeter:", Rectangle2.perimeter())

#2
#
# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
#     def add_grade(self, grade):
#         if grade < 0 or grade > 12:
#             raise ValueError("Grade must be between 0 and 12.")
#         self.grades.append(grade)
#
#     def average_grade(self):
#         if not self.grades:
#             return 0
#         return sum(self.grades) / len(self.grades)
#
#     def __str__(self):
#         return f"Student(name={self.name}, grades={self.grades})"
#
# student = Student("Ivan", [])
#
#
# student.add_grade(10)
# student.add_grade(12)
#
#
# try:
#     student.add_grade(15)
# except ValueError as e:
#     print(f"Error: {e}")
#
# student.add_grade(9)
#
# print(f"Average: {student.average_grade():.2f}")
# print(student)
#
#
# #3
#
# Students = [
#     Student("Ivan", [12, 12, 9]),
#     Student("Anna", [11, 10, 12]),
#     Student("Artem", [2, 2, 1]),
#     Student("Ilya", [8, 9, 10]),
#     Student("Matviy", [5, 6, 7])]
#
# for student in Students:
#     print(f"{student.name} — {student.average_grade():.2f}")
#
# max_avg = max(s.average_grade() for s in Students)
# best_students = [s for s in Students if s.average_grade() == max_avg]
#
# for s in best_students:
#     print(f"Best result: {s.name} — {s.average_grade():.2f}")

#4

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             print(f"Error: Deposit amount must be positive.")
#             return
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print(f"Error: Withdrawal amount must be positive.")
#             return
#         if amount > self.balance:
#             print(f"Error: Insufficient funds for withdrawal -{amount}")
#             return
#         self.balance -= amount
#
#     def info(self):
#         print(f"{self.owner}: Balance {self.balance}")
#
# ivan = BankAccount("Ivan", 1000)
# ivan.deposit(500)
# ivan.withdraw(300)
# ivan.withdraw(2000)
#
# olha = BankAccount("Olha", 700)
# olha.withdraw(200)
# olha.deposit(100)
#
# ivan.info()
# olha.info()
