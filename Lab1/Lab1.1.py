# Exersice 1
s = input("Введите с клавиатуры строку s (разрешаются только латинские символы без пробелов): ")
s = s.casefold()
n = int(input("Введите целое число n – количество индексов i таких, что после удаления символа si из исходной строки s новая строка s’ становится палиндромом: "))
for i in range(len(s)):
    x = s.replace(s[i], "", 1)
    if list(x) == list(reversed(x)) and len(x) + 1 == len(s):
        print(x + " - палиндром")