# if 5 > 2  # синтаксина помилка
#     print("yes")

# n = int("Hello")  # ValueError

# try:
#     age = int(input("Enter your age: "))
#     print(f"You are {age} years old.")
# except ValueError:
#     print("Invalid input. Please enter a valid integer for age.")

# try:
#     a = float(input("Enter a number: "))
#     b = float(input("Enter another number: "))
#     result = a / b
#     print(f"The result of {a} divided by {b} is {result}.")
# except ValueError:
#     print("Invalid input. Please enter valid numbers.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
# else:
#     print(f"square of {number} is {number ** 2}.")

# try:
#     number = int(input("Enter a number: "))
#     print(100 / number)
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# finally:
#     print("Goodbye!")

# try:
#     grade = int(input("Enter your grade (0-12): "))
#     if grade < 0 or grade > 12:
#         raise ValueError("Grade must be between 0 and 12.")
#     print("Your grade is {}".format(grade))
#     break
#  except ValueError as e:
#             print(f"Invalid input: {e}")

# def int_input(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Invalid input. Please enter a valid integer.")
# count = int_input("Enter a number: ")
# print(count)

# def input_grade():
#     while True:
#         try:
#             grade = int(input("Enter your grade (0-12): "))
#             if grade < 0 or grade > 12:
#                 raise ValueError("Grade must be between 0 and 12.")
#             return grade
#         except ValueError as e:
#             print(f"Invalid input: {e}")

# students = ["Anna", "Ivan", "Sophie"]
# try:
#     index = input("Enter the index of the student you want to find: ")
#     index = int(index)
#     print(students[index])
# except ValueError:
#     print("Student not found.")
# except IndexError:
#     print("Index out of range.")

# price = {
#     "apple": 1.5,
#     "banana": 0.8,
#     "orange": 1.2
# }
# product = input("Enter the product name: ")
# try:
#     print(f"The price of {product} is ${price[product]}.")
# except KeyError:
#     print(f"Product '{product}' not found in the price list.")
# print(price.get(product, "Product not found in the price list."))
# print(f"The price of {product} is ${price[product]}.")

# try:
#     with open("data.txt", "r", encoding="utf-8") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print("File not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# line = 'Anna;444'
#
# # line = 'Anna;444'
# #
# # parts = line.split(';')
# if len(parts) != 2:
#     print('error')
# else:
#     name = parts[0]
#     grade = parts[1]
#
#     try:
#         score = int(grade)
#         if score < 0 or score > 100:
#             raise ValueError("Score must be between 0 and 100.")
#         print(f"{name} has a score of {score}.")
#     except ValueError as e:
#         print(f"Invalid score for {name}: {e}")

lines = [
    'Anna;90',
    'Ivan;hello',
    'Sophie;95',]

for line_number, line in enumerate(lines, start=1):
    parts = line.split(';')
    if len(parts) != 2:
        print(f"Line {line_number}: Error - Incorrect format.")
        continue

    name, grade_str = parts
    try:
        score = int(grade_str)
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        print(f"Line {line_number}: {name} has a score of {score}.")
    except ValueError as e:
        print(f"Line {line_number}: Invalid score for {name}: {e}")