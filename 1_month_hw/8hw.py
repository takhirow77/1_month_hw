#1
# # file = open("aslan.txt", encoding="utf-8")
# # print(file.read())


# #2

# # def count(file_path):
# #     with open(file_path, 'r') as file:
# #         a = sum(1 for line in file)
# #     print (f'количествро строк в файле {file_path} {a}')
# # file_path = "eliza.txt"
# # count(file_path)


# 3
# def words(word):
#     with open('file_path.txt', "r") as file:
#         count = file.read()
#         if word in count:
#             print("Слово найдено")
#         else:
#             print("Слово не найдено")
# words('test')

# 4  
# file_path = 'about.txt'                                      
# i = "hjljchc"
# words(file_path)

# i = "about.txt"
# a = input("Введите текст:")
# with open("about.txt",'w') as file:
#     file.write(a)
# print("успешно сохранено")




# #5
# def main(about_path, example_path):
#     with open(about_path, 'r')as a:
#         count = a.read()
#     with open(example_path,'w')as b:
#         b.write(count)

#     print(f"ваш файл успешно сохранено из '{about_path}' в '{example_path}'.")
# a_path = "about.txt"
# b_path = "example.txt"


# main(a_path,b_path)

# #6
# def count_words(file_path):
#     with open(file_path,'r')as file:
#         count = file.read()
#         word = count.split()
#         word_count = len(word)
#         print(f"количество слов в файле {file_path}: {word_count}")
          

# file_path = "about.txt"
# count_words(file_path)

# #7

# def main(file_path,new_content):
#     with open(file_path, 'w')as file:
#         file.write(new_content)
#     print(f'содержимое файла "{file_path}" успешно перезаписано. ')


# file_path = 'about.txt'
# new_content ="dfdfdth"
# main(file_path, new_content)

