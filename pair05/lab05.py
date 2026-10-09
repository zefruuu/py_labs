# def get_circle_area(radius):
#     return 3.14159 * (radius ** 2)
#
# def get_rectangle_area(width, height):
#     return width * height
#
# def get_triangle_area(base, height):
#     return 0.5 * base * height
#
# def main():
#     figure = input("Фігура: ").strip().lower()
#
#     if figure == "круг":
#         radius = float(input("Радіус: "))
#         print(f"Площа круга: {get_circle_area(radius)}")
#     elif figure == "прямокутник":
#         width = float(input("Ширина: "))
#         height = float(input("Висота: "))
#         print(f"Площа прямокутника: {get_rectangle_area(width, height)}")
#     elif figure == "трикутник":
#         base = float(input("Основа: "))
#         height = float(input("Висота: "))
#         print(f"Площа трикутника: {get_triangle_area(base, height)}")
#     else:
#         print("Невідома фігура")
#
# if __name__ == "__main__":
#     main()

# user_num = int(input("Enter a number: "))
# def is_prime():
#     if user_num < 2:
#         return "Ні"
#     if user_num == 2:
#         return "Так"
#     for i in range(2, int(user_num ** 0.5) + 1):
#         if user_num % i == 0:
#             return "Ні"
#     return "Так"
# def divivors():
#     divisors = []
#     for i in range(1, int(user_num ** 0.5) + 1):
#         if user_num % i == 0:
#             divisors.append(i)
#             if i != user_num // i:
#                 divisors.append(user_num // i)
#     return sorted(divisors)
# def digit_sum():
#     str_num = str(user_num)
#     return sum(int(digit) for digit in str_num)
# print(f"Чи є число простим? {is_prime()}")
# print(f"Дільники числа: {divivors()}")
# print(f"Сума цифр числа: {digit_sum()}")

# grades = tuple(map(int, input("Enter grades: ").split()))
#
# def average(grades):
#     return sum(grades) / len(grades)
# def maximum(grades):
#     return max(grades)
# def minimum(grades):
#     return min(grades)
# def moreThan(grades, value):
#     count = 0
#     for grade in grades:
#         if grade > value:
#             count += 1
#     return count
# value = int(input("Enter a value: "))
# count = moreThan(grades, value)
# print(average(grades))
# print(minimum(grades))
# print(maximum(grades))
# print(f'Grades more than {value}: {count}')

# password = input("Enter your password: ")
# def min_password_length():
#     if len(password) < 8:
#         print("Password must be at least 8 characters long.")
#         return False
#     return True
# def number_in_password():
#     if not any(char.isdigit() for char in password):
#         print("Password must contain at least one number.")
#         return False
#     elif any(char.isdigit() for char in password):
#         return True
# def upper_password_length():
#     if not any(char.isupper() for char in password):
#         print("Password must contain at least one uppercase letter.")
#         return False
#     elif any(char.isupper() for char in password):
#         return True
# def lower_password_length():
#     if not any(char.islower() for char in password):
#         print("Password must contain at least one lowercase letter.")
#         return False
#     elif any(char.islower() for char in password):
#         return True
# def special_password_length():
#     special_characters = "!@#$%^&*()-+"
#     if not any(char in special_characters for char in password):
#         print("Password must contain at least one special character.")
#         return False
#     elif any(char in special_characters for char in password):
#         return True
# def validate_password():
#     if (min_password_length() and number_in_password() and upper_password_length() and
#         lower_password_length() and special_password_length()):
#         print("Password is valid.")
#     else:
#         print("Password is invalid.")
#
# validate_password()
