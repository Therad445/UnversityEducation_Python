# Exersice 1
# s = input("Введите с клавиатуры строку s (разрешаются только латинские символы без пробелов): ")
# s = s.casefold()
# n = int(input("Введите целое число n – количество индексов i таких, что после удаления символа si из исходной строки s новая строка s’ становится палиндромом: "))
# for i in range(len(s)):
#     x = s.replace(s[i], "", 1)
#     if list(x) == list(reversed(x)) and len(x) + 1 == len(s):
#         print(x + " - палиндром")

# Exersice 2
# while (True):
#     numbers = input(" Введите с клавиатуры целые неотрицательные числа (через пробел): ").split(" ")
#     for k in range(len(numbers)):
#         for i in range(len(numbers)):
#             if (i+1) > len(numbers) - 1:
#                 break
#             if bin(int(numbers[i])).count("1") > bin(int(numbers[i+1])).count("1"):
#                 a = numbers[i]
#                 numbers[i] = numbers[i+1]
#                 numbers[i + 1] = a
#             elif bin(int(numbers[i])).count("1") == bin(int(numbers[i+1])).count("1"):
#                 if numbers[i] > numbers[i + 1]:
#                     a = numbers[i]
#                     numbers[i] = numbers[i + 1]
#                     numbers[i + 1] = a
#     print(numbers)

# Exersice 3
#
# n = int(input("Введите целое положительное число n – количество строк. \nЗатем введите n строк формата: \n{логин} {дата} {IP} \nLogin – набор латинский букв без пробелов (например, Admin). \nДата – дата формата dd.mm.YYYY (например, 31.12.2021). \nIP – IP адрес формата IPv4 (например, 10.0.0.2). \n"))
# try:
#     data = [0] * n
#     for i in range(n):
#         data[i] = input().split(" ")
#
#     dictData = {}
#     for k in range(n):
#         v = (data[k][1], data[k][2])
#         dictData[v] = data[k][0]
#
#     dictUsers = {}
#     for w in range(n):
#         r = data[w][0]
#         dictUsers[r] = (data[w][1], data[w][2])
#
#     colUsers = []
#     for x in dictUsers:
#         colUsers.append(x)
#
#     answers = []
#     for z in colUsers:
#         ans = 0
#         for i in dictData:
#             if dictData[i] == z:
#                 ans += 1
#         answers.append([str(z), ans, str(dictUsers[z][0])])
#
#     strAns = 0
#     for h in range(len(answers) - 1):
#         if answers[h][1] > strAns:
#             strAns = answers[h]
#     print(str('Ответ: ' + strAns[2]) + ' пользователь с логином ' + str(strAns[0]) + ' авторизовался с ' + str(strAns[1]) + ' различных адресов.')
# except:
#     print("Неправильно введены данные")

# Exercise 4
# dictData = []
# try:
#     k = int(input("Введите целое число k: "))
#     if k <= 0:
#         exit()
#     x = 0
#     for i in range(10000):
#         num = str(i)
#         n = 0
#         for p in range(len(num)):
#             n += int(num[p])
#         if n == 10:
#             dictData.append(i)
#     print(dictData[k - 1])
# except:
#     print("Неправльно введены данные")

# Exercise 2.1
# with open("mask.log", "w") as file:
#     for a in range(0, 256):
#         for b in range(0, 256):
#             for c in range(0, 256):
#                 for d in range(0, 256):
#                     x = str(a) + "." + str(b) + "." + str(c) + "." + str(d)
#                     file.write("\n" + x)
#                     print("Записана маска " + x)
# print("Задача выполнена")
#
# Exercise 2.2
# with open("mask.log", "r") as file:
#     x = ""
# print("Задача выполнена")
#
# Exercise 2.3
# with open("store.csv", "r") as file:
#     x = ""
# print("Задача выполнена")