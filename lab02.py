#1

# n = int(input("Введіть число: "))
#
# total_sum = 0
# count = 0
#
# for i in range(1, n+1):
#     if i % 3 == 0 or i % 5 == 0:
#         total_sum += i
#         count += 1
# if count > 0:
#     average = total_sum/count
# else:
#     average = 0;
# print(count, total_sum, average)

#2

# n = int(input("Введіть число: "))
# suma = 0
# count = 0
# max = 0
# min = 0
# while n > 0:
#     digit = n % 10
#     suma += digit
#     count += 1
#     if digit > max:
#         max = digit
#     if min == 0 or digit < min:
#         min = digit
#     n //= 10
# print(f"Сума: {suma}")
# print(f"Кількість: {count}")
# print(f"Max: {max}")
# print(f"Min: {min}")

#3

# n = int(input("Введіть число: "))
#
# for i in range(1, n + 1):
#     a = i
#     state = True
#
#     while a > 0:
#         digit = a % 10
#
#         if digit == 0 or i % digit != 0:
#             state = False
#             break
#         a //= 10
#
#     if state:
#         print(i, end=" ")

#4

# height = int(input("Введіть висоту: "))
# width = int(input("Введіть ширину: "))
# outline_char = input("Введіть символ контуру: ")
# fill_char = input("Введіть символ середини: ")
#
# if width < 3 or height < 3:
#     print("error")
# else:
#     for i in range(height):
#         for j in range(width):
#
#             if i == 0 or i == height - 1 or j == 0 or j == width - 1:
#                 print(outline_char, end="")
#             else:
#                 print(fill_char, end="")
#         print()