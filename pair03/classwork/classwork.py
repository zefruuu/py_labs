# mess = "Okak"
#
# print(len(mess)) #повертає кі-сть символів
# print(mess[0]) # - перший символ
# print(mess[-1]) # - останній символ

# text = input()
# print(text[:2])
# print(text[2:])
# print(text[::2])
# print(text[2:5])
# print(text[::-1])



# text = input()
# print(text.upper()) # - робить CapsLock
# print(text.capitalize()) # - робить з великою літери перший символ
# print(text.title()) # - робить кожне слово з великої

# text = "              PL      NTUU   "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())

# login = 'admin'
# user_login = input("Enter your login: ")
# if user_login.strip().lower() == login:
#     print("Welcome admin!")

# text = 'Porohobot'
# for char in text:
#     print(char)

# password = input()
# digits = 0
# letters = 0
# for i in password:
#
#     if i.isdigit(): # - метод який перевіряє чи складається  строка тільки  з цифр
#         digits += 1
#     if i.isalpha(): # - метод який перевіряє чи складається  строка тільки  з цифр
#         letters += 1
# print(digits, letters)
#
#
# print(password.isalpha()) # - метод який перевіряє чи складається  строка тільки  з літер
# print(password.isdigit()) # - метод який перевіряє чи складається  строка тільки  з цифр
# print(password.isalnum()) # - метод який перевіряє чи складається  строка тільки  з цифр і літер

# text = input("Введи речення: ")
# vowels = 'аеєиіїуоюя'
# counter_vowels = 0
# for i in text:
#     if i in vowels:
#         counter_vowels += 1
# print(counter_vowels)

# text = "Порошенко Петро Олексійович"
# words = text.split()
# print(words)

# text = "C++ is easy"
# text_new = text.replace("C++", "Python")
# print(text_new)

# word = 'Дід'
# word_norm = word.strip().lower()
# if word_norm == word_norm[::1]:
#     print("Паліндром")
# if word_norm == word_norm[::1]:
#     print("Не паліндром")

# email = 'poroshenko.p.o@gmail.com'
# if email.lower().endswith('@gmail.com'): #.startswith
#     print('you have gmail')