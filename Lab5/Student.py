import re


class Student:

    def __init__(self, name=None, age=None, university=None):
        OK = True
        try:
            name = str(name)
            age = int(age)
            university = str(university)
        except (ValueError, TypeError):
            OK = False

        if OK:
            self.__name = name
            self.__age = age
            self.__university = university
            print('Object created with certain value')
        else:
            self.__name = "Radmir"
            self.__age = 19
            self.__university = "MIET"
            print("Value error: default value was set")

    def __del__(self):
        pass

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def university(self):
        return self.__university

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    def display_info(self):
        print("Вывод информации из буфера")
        print("Студент:", self.__name, "\tВозраст:", self.__age, "\tУчится в университете: ", self.__university)


    @university.setter
    def university(self, value):
        self.__university = value
