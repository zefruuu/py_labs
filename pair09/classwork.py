# book = {
#     'title': "The Great Gatsby",
#     'author': "F. Scott Fitzgerald",
#     'copies_sold': 25000000,
#     'year': 1925
# }

# class Book:
#     def __init__(self, title, author, copies_sold, year):
#         self.title = title
#         self.author = author
#         self.copies_sold = copies_sold
#         self.year = year
#     def available(self):
#         return self.copies_sold > 0
# book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 25000000, 1925)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 30000000, 1960)
#
# print(book1.title, book1.author, book1.copies_sold, book1.year)
# print(book2.title, book2.author, book2.copies_sold, book2.year)
# print(book1.available())
# print(book2.available())

# class rectangle:
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
# rectangle1 = rectangle(5, 10)
# print("Area:", rectangle1.area())
# print("Perimeter:", rectangle1.perimeter())
# print("Area > 1000:", rectangle1.area() > 1000)

# class counter:
#     def __init__(self, value=0):
#         self.value = value
#
#     def increment(self):
#         self.value += 1
#
#     def decrement(self):
#         self.value -= 1
#
#     def reset(self):
#         self.value = 0
#
# counter1 = counter()
# counter2 = counter()
# print("Counter 1 value:", counter1.value)
# counter1.increment()
# print("Counter 1 value after increment:", counter1.value)
# counter2.increment()
# print("Counter 2 value after increment:", counter2.value)
#
# class Book:
#     def __init__(self, title, author, copies_sold, year):
#         self.title = title
#         self.author = author
#         self.copies_sold = copies_sold
#         self.year = year
#
#     def give_one(self):
#         if self.copies_sold > 0:
#             self.copies_sold -= 1
#             return True
#         else:
#             return False
#
# book = Book("The Great Gatsby", "F. Scott Fitzgerald", 20, 1925)
# print("Copies sold before giving one:", book.copies_sold)
# if book.give_one():
#     print("Successfully gave one copy.")
# else:
#     print("No copies left to give.")
# print("Copies sold after giving one:", book.copies_sold)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grades = []

student1 = Student("Ivan")
student2 = Student("Anna")

student1.grades.append(12)
student2.grades.append(1)

print(f'{student1.name} has grades: {student1.grades}')
print(f'{student2.name} has grades: {student2.grades}')