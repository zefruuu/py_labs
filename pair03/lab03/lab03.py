# #1
#
# text = input("Введіть текст: ")
#
#
# total_chars = len(text)
# letters = 0
# digits = 0
# spaces = 0
# vowels_count = 0
#
#
# vowels = "аaэeуyuoеіїаоя"
#
#
# for char in text:
#     if char.isalpha():
#         letters += 1
#
#         if char.lower() in vowels:
#             vowels_count += 1
#     elif char.isdigit():
#         digits += 1
#     elif char.isspace():
#         spaces += 1
#
#
# words_count = len(text.split())
#
#
# print(total_chars)
# print(letters)
# print(digits)
# print(spaces)
# print(vowels_count)
# print(words_count)

#2
# name = input("Введіть ПІБ: ")
# parts = name.split()
#
# if len(parts) == 3:
#     lastname = parts[0]
#     firstname = parts[1]
#     pobatykovi = parts[2]
#     print(f"{lastname.title()} {firstname[0].upper()}.{pobatykovi[0].upper()}.")

#3
# text1 = input("Enter your text1: ").lower().replace(" ", "")
# text2 = input("Enter your text2: ").lower().replace(" ", "")
# tempText2 = text2
# if len(text1) != len(text2):
#     print("no anagram")
# else:
#     for i in text1:
#         if i in tempText2:
#             tempText2 = tempText2.replace(i, "", 1)
#             if len(tempText2) == 0:
#                 print("anagram")
#                 break
#         else:
#             print("no anagram")
#             break

#4
# text = input("Enter your text: ")

# text_list = text.lower().split()
# letter_count = 0
# unique_words = 0
# biggest_word = ""
# smallest_word = ""
# for word in text_list:
#     letter_count += len(word)
#     if len(word) > len(biggest_word):
#         biggest_word = word
#     if len(word) < len(smallest_word) or smallest_word == "":
#         smallest_word = word
#     if text_list.count(word) == 1:
#         unique_words += 1
# print("Biggest word: ", biggest_word)
# print("Smallest word: ", smallest_word)
# print("Unique words: ", unique_words)
# textReplace = input("Enter the word to replace: ")
# textReplaceWith = input("Enter the word to replace with: ")
# text = text.replace(textReplace, textReplaceWith)
# print("Modified text:", text)
