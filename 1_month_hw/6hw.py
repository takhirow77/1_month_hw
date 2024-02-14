# dictionary_1 = {'a': 300, 'b': 400}
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)


#2
# numbers = {"num_1" : 1, "num_2" : 2, "num_3" : 3, "num_100": 100}
# num1 = numbers["num_1"]
# n1 = num1 * 5
# print(n1)
# num1 = numbers["num_2"]
# n2 = num1 * 5
# print(n2)
# num1 = numbers["num_3"]
# n3 = num1 * 5
# print(n3)
# num1 = numbers["num_100"]
# n100 = num1 * 5
# print(n100)

#3
# d = {'name' : 'Askhat','‘age' : 17}

# a = d['age']
# b = a * 2
# print(b)

#4
# student = {"name" : "Askhat", "age" : 17, "color" : "White"}
# print(student)
# student["age"] = 16
# print(student)

#5
# student = {"name" : "Askhat", "age" : 17}
# print(student)
# student.pop("age")
# print(student.values())

#6
# student = {"name" : "Askhat"}
# student["adders"] = "Западный анар"
# print(student)

#7
# def chatbot():
#     while True:
#         chat = input("Введите приложения:")
#         if '?' in chat:
#             print('конечно')
#         elif '!'in chat:
#             print('успакойся')
#         elif '' in chat:
#             print('как класно когда ты молчишь.продолжай в том же духе!')
#         else:
#             print('ну и что')
            
# chatbot()

#8
# def numbers(num):
#     num_dict = num.split()
#     for a in range (len(num_dict)):
#         print(num_dict[a][0],end = '')
# numbers('пока нока дока')

#9
# def count_words(string):
#     word_counts = {}
#     for word in string.split():
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts
# string = ("money, money, money, its always sunny, in the richmens world").lower()
# print(count_words(string))

#10
# def is_isogram(word):
#     word = word.lower()

#     unique_letters = set(word)

#     return len(unique_letters) == len(word)

# input_word = input("Введите слово: ")
# result = is_isogram(input_word)

# if result:
#     print("Слово является изограммой.")
# else:
#     print("Слово не является изограммой.")

#11
# def number(num):
#     a = n[::-1]
#     print(a)

# n = input('Введите число:')
# number(n)

