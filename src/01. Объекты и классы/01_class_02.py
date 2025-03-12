from _lib import print_line


class Person:
    biological_species: str = 'Homo sapiens'
    
class Employee(Person):
    ...
    
class Student(Person):
    ...


cls_list = [Person, Employee, Student]
for cls in cls_list:
    print(f'Тип класса {cls.__name__} = {type(cls)}')
    print(f'Тип экземпляра класса {cls.__name__} = {type(cls())}')
    print_line()

