from classes import Person, Employee, Student

people = [Person("Tom", 23), Student("Bob", 19, "Harvard"), Employee("Sam", 35, "Google")]
for person in people:
    person.display_info()
    person.remember_info()
    person.remember_info()
    person.display_remember_info()
    person.display_info()
    print("----------------------")

