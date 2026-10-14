import os

#1

# if not os.path.exists('text.txt'):
#     with open('text.txt', 'w', encoding='utf-8') as f:
#         f.write('Привіт, Світ!')
#         f.write('Привіт, Іван!')
#         f.write('Привіт, КПІ!')
#         f.write('Привіт, Ілля Королюк!')
# with open('text.txt', 'r', encoding='utf-8') as f:
#     text = f.read()
#     lineCount = text.count('\n') + 1
#     wordCount = len(text.split())
#     charCount = len(text)
# print(f'Count of lines: {lineCount}')
# print(f'Count of words: {wordCount}')
# print(f'Count of characters: {charCount}')

#2

# word = input('Введіть слово для пошуку: ')
#
# if not os.path.exists('documentation.txt'):
#      with open('documentation.txt', 'w', encoding='utf-8') as f:
#             f.write('Тут може бути ваша реклама\n')
#             f.write('Якісь текст\n')
#             f.write('Python зручно використовувати для обробки даних.\n')
#             f.write('Петро Порошенко любить програмувати на С++.\n')
#             f.write('Вивчення Python потребує практики.\n')
# def searching_word_in_file(word, line_with_word):
#     with open('documentation.txt', 'r', encoding='utf-8') as f:
#         text = f.read()
#         if word in text:
#             line_with_word = [line for line in text.split('\n') if word in line]
#             print(f'Рядки з словом "{word}":')
#             for line in line_with_word:
#                 print(line)
#         else:
#             print(f'Слово "{word}" не знайдено у файлі.')
# searching_word_in_file(word, [])

#3

# if not os.path.exists('students.txt'):
#       with open('students.txt', 'w', encoding='utf-8') as f:
#             f.write('Ivanenko Anna;91\n')
#             f.write('Petrenko Ivan;76\n')
#             f.write('Komarova Olha;97\n')
#
# def sort_students_by_score():
#     students = []
#     with open('students.txt', 'r', encoding='utf-8') as f:
#         for line in f:
#             clean_line = line.strip()
#             if not clean_line:
#                 continue
#
#             name, score_str = clean_line.split(';')
#             score = int(score_str)
#
#             if score > 80:
#                 students.append({'name': name, 'score': score})
#
#     return sorted(students, key=lambda x: x['score'], reverse=False)
#
# with open('result.txt', 'w', encoding='utf-8') as f:
#     for student in sort_students_by_score():
#         f.result = f.write(f"{student['name']};{student['score']}\n")

#4
# grades = {}
# if not os.path.exists('grades.csv'):
#     with open('grades.csv', 'x', encoding='utf-8') as file:
#         file.write('Anna;IT;11\n')
#         file.write('Anna;Math;10\n')
#         file.write('Illya;IT;2\n')
#         file.write('Illya;Math;1\n')
#         file.write('Ivan;IT;9\n')
#         file.write('Ivan;Math;12\n')
#
# def count_grades():
#     with open('grades.csv', 'r', encoding='utf-8') as file:
#         for line in file:
#             clean_line = line.strip()
#             if not clean_line:
#                 continue
#             name, subject, grade_str = clean_line.split(';')
#             grade = int(grade_str)
#             if name not in grades:
#                 grades[name] = []
#             grades[name].append(grade)
#     return grades
# def average_grades():
#     with open('grades.csv', 'r', encoding='utf-8') as file:
#         for line in file:
#             clean_line = line.strip()
#             if not clean_line:
#                 continue
#             name, subject, grade_str = clean_line.split(';')
#             grade = int(grade_str)
#             if name not in grades:
#                 grades[name] = []
#             grades[name].append(grade)
#     average_grades = {name: sum(grades_list) / len(grades_list) for name, grades_list in grades.items()}
#     return average_grades
# def best_average_grade():
#     average_grades_dict = average_grades()
#     best_student = max(average_grades_dict, key=average_grades_dict.get)
#     best_average = average_grades_dict[best_student]
#     return best_student, best_average
# if not os.path.exists('studentReport.txt'):
#     with open('studentReport.txt', 'w', encoding='utf-8') as file:
#         file.write('Average grades:\n')
#         for name, average in average_grades().items():
#             file.write(f'{name}: {average:.2f}\n')
#         best_student, best_average = best_average_grade()
#         file.write(f'\nBest student: {best_student} with average grade: {best_average:.2f}\n')
