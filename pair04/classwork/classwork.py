#list - список - впорядкована змінна колекція
# grades = [10,8,9]
# numbers = []
#
# grades[1] = 12
# print(grades)
# numbers.append(10)
# numbers.append([11,4])
# numbers.insert(100, [5,6])
# numbers.extend([7,8,9,7])
# numbers.remove (7)
# numbers.pop(1)
# #del numbers[1]
# numbers.clear()
# print(numbers.count(8))
# print(numbers.index(8))
#
# if 8 in numbers:
#     print("True")
#
# len()
# min()
# max()
# sum()
# print(numbers)

# numbers = [1, 2, 3]
# numbers.sort(reverse = True)
#
# numbers = [1, 2, 3]
# positive = []
# for number in numbers:
#     positive.append(number)
# print(positive)

#turple - кортежі - не можна змінювати значення
# point = (-10, 22)
# rgb = (255, 0 ,0)
# data = ()
# student = "Ivan", "Vorobiov"
# a=(10,)
# b = a + (23,)
# print(b)
# point = point[:1] = point[:-1]
# point = (-12,6)
# x,y = point
# print(x)
# print(y)



#set - множини - немає дублікатів - немає індексного доступа - порядок немає значення - можна додавати/видаляти
# subjects = {"Python", "HTML", "C++"}
# data = {}
# print(type(data))
# subjects.add("C++")
# subjects.update(["Java", "Python"])
# subjects.remove("Java")
# subjects.discard("C#")
# print(subjects)
# if "Python" in subjects:
#     print("Python")

# names = ["Ivan", "Oleg", "Olha", "Ivan", "Maria", "Oleg"]
# unique_names = set(names)
# print(unique_names)
#
# group1 = {"Ivan", "Oleg", "Olha"}
# group2 = {"Ivan", "Mykola", "Ann"}
#
# peretyn =  group1 & group2
# obiednanya =  group1 | group2
# riznitsya =  group1 - group2
# print(obiednanya)
# print(peretyn)
# print(riznitsya)

#dict - словники
# student = {
#     "name": "Ivan",
#     "grade": 11
# }
# student2 = {}
# student3 = dict()
#
# print (student["name"])
#
# student["age"] = 18
# print(student)
# student["age"] = 19
# print(student)
# student_update = student.pop("age")
# print(student_update)
# popitem = student.popitem()

# student = {
#     "name": "Ivan",
#     "grade": 11
# }
#
# print(student.get("age", "Is not exist"))
# if "grade" in student:
#     print(student.get("grade"))
# if "Ivan" in student.values():
#     print(student.get("Ivan"))
# if "Ivan" in student.keys:
#     print(student.get("Ivan"))
#
# print(student.items())

# for key, value in student.items():
#     print(key)
#     print(value)

# prices = {
#     'apple': 45,
#     'orange': 80,
#     'mango': 150
# }
# print("Усі товари: ")
# for name, price in prices.items():
#     print(f"{name}: {price}грн")
#
# for name, price in prices.items():
#     if price > 50:
#         print(f"{name}: {price}грн")