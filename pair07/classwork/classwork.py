import os
#
# with open('hello.txt', 'w', encoding='utf-8') as file:
#     file.write('Комаров Іван Юрійович гарний мужчіна\n')
#
# # r - режим читання, файл вже має бути створений
# # w - режим запису, якщо файл існує, то він буде перезаписаний
# # a - режим додавання, якщо файл існує, то нові дані будуть додані в кінець файла
# # x - режим створення нового файла, якщо файл існує, то буде помилка

if not os.path.exists('text.txt'):
    with open('text.txt', 'x', encoding='utf-8') as file:
        file.write('Комаров Іван Юрійович  дуже сильно гарний мужчіна\n')
        file.write('Комаров Іван Юрійович  прекрасний мужчіна\n')
        file.write('Комаров Іван Юрійович - мужчіна, мабуть\n')
        file.write('Сьогодні ми працюємо з Комаровим Іваном Юрійовичем\n')

if not os.path.exists('numbers.txt'):
    with open('numbers.txt', 'x', encoding='utf-8') as file:
        file.write ("12\n8\n5\n3\n7\n9\n")

if not os.path.exists('student.txt'):
    with open('student.txt', 'x', encoding='utf-8') as file:
        file.write('Ivan Komarov;91\n')
        file.write('Illya Koroliuk;13\n')
        file.write('Ivan Vorobiov;99\n')

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'x', encoding='utf-8') as file:
        file.write('Ivan K;IT;10\n')
        file.write('Ivan K;Math;11\n')
        file.write('Illya;IT;2\n')
        file.write('Illya;Math;1\n')
        file.write('Ivan V;IT;12\n')
        file.write('Ivan V;Math;12\n')



with open('text.txt', 'r', encoding='utf-8') as file: # with автоматично закриває файл після завершення блоку коду
    text = file.read()
print(text)

with open('log.txt', 'w', encoding='utf-8') as file:
    file.write("Log file created\n")

with open('log.txt', 'w', encoding='utf-8') as file:
    file.write("Log file updated\n")

with open('log.txt', 'a', encoding='utf-8') as file:
    file.write("Log file updated again\n")

# Способи читання файлів
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()
print(f'read -> {type(text)}, count of characters: {len(text)}')

with open('text.txt', 'r', encoding='utf-8') as file:
    line1 = file.readline() # читаємо перший рядок
    line2 = file.readline() # читаємо другий рядок
    other_lines = file.readlines() # читаємо всі інші рядки у вигляді списку
print(line1)
print(line2)
print(other_lines)

with open('text.txt', 'r', encoding='utf-8') as file:
   lines = file.readlines()
print(other_lines[0]) if lines else 'File is empty'

# перебір файлів
with open('text.txt', 'r', encoding='utf-8') as file:
    for number, line in enumerate(file, start=1):
        clean_line = line.strip()
        print(f'Line {number}: {clean_line}') # strip() видаляє пробіли та символи переносу рядка з початку та кінця рядка

line = "Komarov;Ivan"
clean_line = line.strip()
name, surname = clean_line.split(';')
print(f'{surname} {name}')

numbers = []
with open('numbers.txt', 'r', encoding='utf-8') as file:
    for line in file:
        clean_line = line.strip()
        number = int(clean_line)
        numbers.append(number)
print(numbers)

students = []
with open('student.txt', 'r', encoding='utf-8') as file:
    for line in file:
        clean_line = line.strip()
        name, score = clean_line.split(';')
        student = {'name': name, 'score': int(score)}
        students.append(student)
print(students)

grades = []
with open('grades.csv', 'r', encoding='utf-8') as file:
    for line in file:
        name, subject , score = line.strip().split(';')
        grade = {'name': name, 'subject': subject, 'score': int(score)}
        grades.append(grade)
print(grades)