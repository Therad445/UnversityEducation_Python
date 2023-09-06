import os

x = input("Введите нужное расширение: ")
i = 0
for file in os.listdir("example"):
    if file.endswith(x):
        i += 1
print(i)
