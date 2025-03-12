from _lib import print_line


class Person:
    biological_species = 'Homo sapiens'
    
class Employee(Person):
    ...
    
class Student(Person):
    ...
# ---------------------------------------
            
    
person = Person()

print(f'Тип класса Person = {type(Person)}') # <class 'type'>
print(f'Тип экземпляра класса Person = {type(person)}') # <class '__main__.Person'>
print_line()
# ---------------------------------------

employee = Employee()

print(f'Тип класса Employee = {type(Employee)}') # <class 'type'>
print(f'Тип экземпляра класса Employee = {type(employee)}') # <class '__main__.Person'>    
print_line()
# ---------------------------------------

student = Student()

print(f'Тип класса Student = {type(Student)}') # <class 'type'>
print(f'Тип экземпляра класса Student = {type(employee)}') # <class '__main__.Person'>    
print_line()

