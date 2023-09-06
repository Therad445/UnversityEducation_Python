import unittest
from Student import Student


def input_str():
    is_inputted = False
    nums = ""
    while not is_inputted:
        nums = input()
        try:
            nums = str(nums)
            is_inputted = True
        except ValueError:
            print("Wrong input. Enter again: ", end='')
    return nums


def input_int():
    is_inputted = False
    nums = 0
    while not is_inputted:
        nums = input()
        try:
            nums = int(nums)
            is_inputted = True
        except ValueError:
            print("Wrong input. Enter again: ", end='')
    return nums


class WrongDateException(Exception):
    def __init__(self, text):
        self.txt = text


lst1, lst2, lst3 = [], [], []

try:
    with open("students.txt", "br") as file:
        data = file.readlines()
        i = 0
        for line in data:
            line.replace(b'\n', b'')
            a, b, c = map(str, line.split())
            lst1.append(a)
            lst2.append(b)
            lst3.append(c)
            i += 1
except IOError:
    print("Database doesn't exist")
    print("Enter number of students you want to add: ", end='')
    num = 0
    while num <= 0:
        num = input_int()
        if num <= 0:
            print("Len of array can't be negative")
    assert num > 0, "Len of array can't be negative"

    cur = 0
    while cur < num:
        try:
            print('Input name: ', end='')
            name = input_str()

            print('Input age: ', end='')
            age = input_int()

            print('Input university: ', end='')
            university = input_str()

            lst1.append(name)
            lst2.append(age)
            lst3.append(university)
            cur += 1


        except WrongDateException as e:
            print(e.txt)

assert len(lst1) > 0, "Database can't be empty"

with open("students.txt", 'bw') as fOut:
    for elem in range(len(lst1)):
        fOut.write(bytearray("{} {} {}\n".format(lst1[elem], lst2[elem], lst3[elem]), 'utf8'))

