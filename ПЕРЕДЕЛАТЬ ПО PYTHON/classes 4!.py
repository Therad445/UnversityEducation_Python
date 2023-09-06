def remember(self):
        def inner(man):
            if man.name not in Person.memory:
                Person.memory[man.name] = man.age
            else:
                print('returning result from saved memory')
            return Person.memory[man.name]

        return inner

@remember
class Person:
    def __init__(self, name, age):
        self.__name = name  # устанавливаем имя
        self.__age = age  # устанавливаем возраст

    memory = {}

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Недопустимый возраст")

    

    def display_remember_info(self):
        for elem in self.memory:
            print("Вывод информации из памяти")
            print("Имя:", elem, "\tВозраст:", self.memory[elem])

    def display_info(self):
        print("Вывод информации из буфера")
        print("Имя:", self.__name, "\tВозраст:", self.__age)


class Employee(Person):
    # определение конструктора
    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company

    # переопределение метода display_info
    def display_info(self):
        Person.display_info(self)
        print("Компания:", self.company)


class Student(Person):
    # определение конструктора
    def __init__(self, name, age, university):
        Person.__init__(self, name, age)
        self.university = university

    # переопределение метода display_info
    def display_info(self):
        print("Студент", self.name, "учится в университете", self.university)



ВЫНЕСТИ REMEMBER ! МОЖЕТ УЖЕ НАЧАЛ РАБОТАТЬ ! НО МОЖЕТ И НЕ СДАВАТЬ ТАК КАК 4 ИЗ 5 БАЛЛА УЖЕ СТОЯТ