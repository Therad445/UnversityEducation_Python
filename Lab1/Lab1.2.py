# Exersice 2
numbers = input(" Введите с клавиатуры целые неотрицательные числа (через пробел): ").split(" ")
for k in range(len(numbers)):
    for i in range(len(numbers)):
        if (i+1) > len(numbers) - 1:
            break
        if bin(int(numbers[i])).count("1") > bin(int(numbers[i+1])).count("1"):
            a = numbers[i]
            numbers[i] = numbers[i+1]
            numbers[i + 1] = a
        elif bin(int(numbers[i])).count("1") == bin(int(numbers[i+1])).count("1"):
            if numbers[i] > numbers[i + 1]:
                a = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = a
print(numbers)