# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")
# try:
#     if operation == "+":
#         result = number1 + number2
#     elif operation == "-":
#         result = number1 - number2
#     elif operation == "*":
#         result = number1 * number2
#     elif operation == "/":
#         result = number1 / number2
#     else:
#         raise ValueError("Invalid operation. Please enter one of +, -, *, /.")
#     print(f"The result of {number1} {operation} {number2} is {result}.")
# except ValueError as e:
#     print(f"Error: {e}")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

#2

# def input_grade():
#     while True:
#        try:
#              grade = int(input("Enter your grade (0-12): "))
#              if grade < 0 or grade > 12:
#                  raise ValueError("Grade must be between 0 and 12.")
#              return print(f'Grade is: {grade}')
#        except ValueError as e:
#              print(f"Invalid input: {e}")
#
# input_grade()

#3

# student = ["Artem", "Anna", "Illya", "Matvii", "Ivan"]
#
# subject_statistics =  {
#     "Math": 1,
#     "English": 11,
#     "IT": 5,
#     "History": 7,
#     "Physics": 9
# }
#
# print("1 - Search student by index")
# print("2 - Search grade by subject grade")
#
# user_search = input("Enter the type of search: ")
#
# def search_student_by_index():
#     try:
#         index = int(input("Enter the index of the student you want to find: "))
#         print(f"The student at index {index} is {student[index]}.")
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")
#     except IndexError:
#         print("Error: Index out of range. Please enter a valid index.")
#
# def search_grade_by_subject():
#     try:
#         subject = input("Enter the subject you want to find the grade for: ")
#         print(f"The grade for {subject} is {subject_statistics[subject]}.")
#     except KeyError:
#         print("Error: Subject not found. Please enter a valid subject.")
#
# if user_search == "1":
#     search_student_by_index()
# elif user_search == "2":
#     search_grade_by_subject()

#4

# with open("students.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()
#     for line in lines:
#         try:
#             name, grade = line.strip().split(";")
#             grade = int(grade)
#             if not (0 <= grade <= 100):
#                 print(
#                     f"Error: Invalid grade in line number {lines.index(line) + 1}: '{line.strip()}'. Grade must be between 0 and 100.")
#             else:
#                 print(f"Name: {name}, Grade: {grade}")
#         except ValueError:
#             print(f"Error: Invalid data format in line number {lines.index(line) + 1}: '{line.strip()}'. Expected 'name;grade'.")
#         except FileNotFoundError:
#             print("Error: The file 'students.txt' was not found.")

