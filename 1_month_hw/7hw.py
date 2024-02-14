#1
# try:
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     result = num1 / num2
#     print(f"Результат деления: {result}")
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль!")

#2
# name = input("Введите ваше имя: ")

# if name:
#       print("Привет,", name + "!")
# else:
#     print("Вы не ввели имя.")


#3
# password = input("Введите пароль")
# if len(password) < 6:
#     print("Пароль слишком короткий")
# elif len(password) <=  8: 
#     print("Хорошо, но можно еше лучше")
# else: 
#     print("Пароль подходит")

#4
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))

# print(a+b)

#5
# def sum_of_arguments(*args):
#     total = sum(args)
#     print(f"Сумма аргументов: {total}")

# sum_of_arguments(23, 22, 31, 234, 73)
# sum_of_arguments(1021, 23430, 6530)
# sum_of_arguments(213, 3453, 43425, 3232)




#6
# double = lambda x: x*2
# print(double(10))

#7
# def even_fn(x):
#   if x % 2 == 0:
#     return True
#   return False

# print(list(filter(even_fn, [1, 3, 2, 5, 20, 21])))




#8
# lambda_func = lambda x: x**4
# print(lambda_func(3))

#9
# my = ['apple', 'banana', 'cherry', 'date']
# a = sorted(my, key=lambda x: len(x))
# print(a)

#10
# x = lambda string, char: char in string

# print(x("hello", "a"))  
# print(x("world", "w"))


#11
# x = lambda slovo, slovo2: slovo + slovo2

# result = x("Hello", "World")
# print(result)

#12
# numbers_list = [-2021, -22023, 23123123, 2312312, 100000]
# x = list(filter(lambda x: x > 0, numbers_list))
# print(x)

#1
# def user(): 
#     while True:
#         user = input("Можете задать вопрос: ")
#         if '?' in user:
#             print("Конечно!")
#         elif '!' in user:
#             print("Успокойся")
#         elif user == "":
#             print("Как классно, когда ты молчишь. Продолжай в том же духе!")
#         else:
#             print("ну и что")
# user()

#2
# def country():
#     user = "Кыргызская Республика"
#     words = user.split()
#     pon = ''.join(word[0].upper() for word in words)
#     print(pon)

# country()

#3
# def count_words():
#     wordss = "money, money, money, it’s always sunny, in the richmen’s world"
#     words = wordss.split()
#     word_counts = {}

#     for word in words:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     print(word_counts)

# count_words()

#4
# def isogram(word):
#     word = word.lower()
#     unique_letters = set()
#     for letter in word:
#         if letter in unique_letters:
#             return False
#         unique_letters.add(letter)
#     return True
# word1 = "hello"
# word2 = "world"
# word3 = "algorithm"
# print(isogram(word1))
# print(isogram(word2))
# print(isogram(word3))

#5
# def num():
#      n = 21
#      num_1 = ""
#      for i in str(n):
#          num_1 = i + num_1
#      num_1 = int(num_1)
#      print(num_1)
# num()