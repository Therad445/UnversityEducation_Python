# Exersice 3
n = int(input("Введите целое положительное число n – количество строк. \nЗатем введите n строк формата: \n{логин} {дата} {IP} \nLogin – набор латинский букв без пробелов (например, Admin). \nДата – дата формата dd.mm.YYYY (например, 31.12.2021). \nIP – IP адрес формата IPv4 (например, 10.0.0.2). \n"))
try:
    data = [0] * n
    for i in range(n):
        data[i] = input().split(" ")

    dictData = {}
    for k in range(n):
        v = (data[k][1], data[k][2])
        dictData[v] = data[k][0]

    dictUsers = {}
    for w in range(n):
        r = data[w][0]
        dictUsers[r] = (data[w][1], data[w][2])

    colUsers = []
    for x in dictUsers:
        colUsers.append(x)

    answers = []
    for z in colUsers:
        ans = 0
        for i in dictData:
            if dictData[i] == z:
                ans += 1
        answers.append([str(z), ans, str(dictUsers[z][0])])

    strAns = 0
    for h in range(len(answers) - 1):
        if answers[h][1] > strAns:
            strAns = answers[h]
    print(str('Ответ: ' + strAns[2]) + ' пользователь с логином ' + str(strAns[0]) + ' авторизовался с ' + str(strAns[1]) + ' различных адресов.')
except:
    print("Неправильно введены данные")