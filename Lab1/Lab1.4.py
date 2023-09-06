# Exercise 4
dictData = []
try:
    k = int(input("Введите целое число k: "))
    if k <= 0:
        exit()
    x = 0
    for i in range(10000):
        num = str(i)
        n = 0
        for p in range(len(num)):
            n += int(num[p])
        if n == 10:
            dictData.append(i)
    print(dictData[k - 1])
except:
    print("Неправльно введены данные")