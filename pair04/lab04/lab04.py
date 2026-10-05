# # #1
# # user_input = input("Enter numbers: ").split()
# # numbers = []
# # for i in user_input:
# #     numbers.append(int(i))
# # multiple = []
# # positive = []
# # negative = []
# # even = []
# # for number in numbers:
# #     if number % 3 == 0:
# #         multiple.append(number)
# #     if number % 2 == 0:
# #         even.append(number)
# #     if number > 0:
# #         positive.append(number)
# #     if number < 0:
# #         negative.append(number)
# # print(positive)
# # print(negative)
# # print(even)
# # print(multiple)
# # print(f"Мінімальне: {min(numbers)} Максимальне: {max(numbers)} Сумма: {sum(numbers)} Середнє: {sum(numbers) / len(numbers)}")
# #
#
# #2
#
# # group1 = {'Anna', 'Ivan', 'Olha'}
# # group2 = {'Ivan', 'Maksym', 'Olha'}
# # spilni =  group1 & group2
# # only_group1 =  group1 - group2
# # only_group2 =  group2 - group1
# # razom =  group1 | group2
# # print(spilni)
# # print(only_group1)
# # print(only_group2)
# # print(razom)
#
# #3
# # product = [{"name": "Milk", "price": 48.0}, {"name": "Tea", "price": 75.0}, {"name": "Eggs", "price": 25.0}, {"name": "Cheese", "price": 120.0}]
# # print("Add new product: 1\n Search product: 2\n Search product by price range: 3")
# #
# # choice = input("Enter your choice: ")
# #
# # if choice == "1":
# #     name = input("Enter product name: ")
# #     price = float(input("Enter product price: "))
# #     product.append({"name": name, "price": price})
# # if choice == "2":
# #     name = input("Enter product name: ")
# #     for item in product:
# #         if item["name"] == name:
# #             print(f"Product: {item['name']}, Price: {item['price']}")
# #             break
# #     else:
# #         print("Product not found.")
# # if choice == "3":
# #     min_price = float(input("Enter minimum price: "))
# #     max_price = float(input("Enter maximum price: "))
# #     found = False
# #     for item in product:
# #         if min_price <= item["price"] <= max_price:
# #             print(f"{item['name']} -- {item['price']}")
# #             found = True
# #     if not found:
# #         print("No products found in the given price range.")
#
# #4
#
# group_info = ('10-IT', '2026/2027')
# students = {}
#
# while True:
#     print(
#         "\nAdd new student: 1\nPrint all students list: 2\n"
#         "Search student average grade by name: 3\nStudents rating by average grade: 4\nSearch students with highest average grade: 5")
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         full_name = input("Enter student full name: ")
#         grades = list(map(int, input("Enter student grades(1-12) separated by space: ").split()))
#         if len(grades) == 5 and all(1 <= grade <= 12 for grade in grades):
#             students[full_name] = grades
#         else:
#             print("Error")
#
#     elif choice == "2":
#         print(f"{group_info[0]} -- {group_info[1]}")
#         for name, grades in students.items():
#             print(f"{name} -- {grades}")
#
#     elif choice == "3":
#         full_name = input("Enter student full name: ")
#         if full_name in students:
#             average_grade = sum(students[full_name]) / len(students[full_name])
#             print(f"{full_name} -- {average_grade:.1f}")
#
#
#     elif choice == "4":
#         if students:
#             rating = []
#             for name, grades in students.items():
#                 average_grade = sum(grades) / len(grades)
#                 rating.append((name, average_grade))
#             rating.sort(key=lambda x: x[1], reverse=True)
#             for name, avg in rating:
#                 print(f"{name} -- {avg:.1f}")
#
#
#     elif choice == "5":
#         if students:
#             best_student = None
#             max_avg = -1
#             for name, grades in students.items():
#                 average_grade = sum(grades) / len(grades)
#                 if average_grade > max_avg:
#                     max_avg = average_grade
#                     best_student = name
#             print(f"{best_student} -- {max_avg:.1f}")
#
