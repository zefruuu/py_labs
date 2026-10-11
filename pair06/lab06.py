# import math
import statistics
import random
import datetime
#
# def calculate_circle_area(radius):
#     radius = float(radius)
#     round(math.pi * pow(radius, 2), 2)
# def caclulate_triandle_area(cathetus1, cathetus2):
#     cathetus1 = float(cathetus1)
#     cathetus2 = float(cathetus2)
#     return (round(math.sqrt(cathetus1**2 + cathetus2**2),2))
# def calcuate_packages(N, K):
#     N = int(N)
#     K = int(K)
#     return round(math.ceil(N / K),2)
#
#
#
# user_radius = input("Enter the radius of the circle: ")
# print(calculate_circle_area(user_radius))
# user_cathetus1 = input("Enter the first cathetus of the triangle: ")
# user_cathetus2 = input("Enter the second cathetus of the triangle: ")
# triangle_area = caclulate_triandle_area(user_cathetus1, user_cathetus2)
# print(triangle_area)
# user_N = input("Enter the number of items: ")
# user_K = input("Enter the number of packages: ")
# packages = calcuate_packages(user_N, user_K)
# print(packages)

#2

# numberOfGrades = int(input("Enter the number of grades: "))
# grades = []
# for i in range(numberOfGrades):
#     grades.append(random.randint(1, 12))
# print(grades)
# print("Minimum grade:", min(grades))
# print("Maximum grade:", max(grades))
# print("Average grade:", statistics.mean(grades))
# print("Median grade:", statistics.median(grades))
# count = 0
# for grade in grades:
#     if 10 <= grade <= 12:
#         count += 1
# print("Number of grades between 10 and 12:", count)

#3


# data = input("Enter the date of the event (YYYY-MM-DD): ")
# event_date = datetime.datetime.strptime(data, "%Y-%m-%d").date()
# today = datetime.date.today()
#
# if event_date > today:
#     days_left = (event_date - today).days
#     print(f"The event is in {days_left} days.")
# elif event_date < today:
#     days_passed = (today - event_date).days
#     print(f"The event was {days_passed} days ago.")
# else:
#     print("The event is today!")

#4

