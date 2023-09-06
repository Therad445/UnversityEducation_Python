def q(i):
    if i == 1 or i == 2:
        return 1
    else:
        return q(i - q(i - 1)) + q(i - q(i - 2))


def hofstadter_q(n):
    mas_out = []
    if n < 1:
        return "Число меньше 1, операция не может быть выполнена"
    else:
        for iterator in range(1, n + 1):
            mas_out.append(q(iterator))
        return mas_out


nInput = int(input("Ввведите какое число n, членов последовательности Хофштадтера будет выведено: "))
print(hofstadter_q(nInput))
