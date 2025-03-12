from _lib import print_line


class Person:
    biological_species: str = 'Homo sapiens'
    
class Student(Person):
    ...    
    
class Employee(Person):
    ...
    
class Developer(Employee):
    ...


print(issubclass(Developer, Employee))  # True
print(issubclass(Employee, Person))     # True
print(issubclass(Developer, Person))    # True


dev = Developer()
print(isinstance(dev, Developer))   # True
print(isinstance(dev, Employee))    # True
print(isinstance(dev, Person))      # True