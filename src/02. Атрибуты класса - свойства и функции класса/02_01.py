class Person:
    """класс Person"""


class_type = type(Person)

print(class_type)  # <class 'type'>

# У класса есть атрибуты, которые мы явно не создавали
print(Person.__name__)  # Person
print(Person.__class__.__name__)  # type
print(Person.__doc__)  # класс Person

# Добавляем новый атрибут класса
Person.biological_species = "Homo sapiens"

# Другой вариант добавления атрибута
setattr(Person, "planet", "Earth")

print(Person.__dict__)
# {
#   '__module__': '__main__',
#   '__doc__': 'класс Person',
#   '__dict__': <attribute '__dict__' of 'Person' objects>,
#   '__weakref__': <attribute '__weakref__' of 'Person' objects>,
#   'biological_species': 'Homo sapiens',
#   'planet': 'Earth'
# }

dict_type = type(Person.__dict__)
print(dict_type)  # <class 'mappingproxy'>

print(dir(Person))
# [
#   '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
#   '__eq__', '__format__', '__ge__', '__getattribute__',
#   '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#   '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
#   '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
#   '__subclasshook__', '__weakref__',
#   'biological_species', 'planet'
# ]


# Обращение к атрибуту
print(Person.planet)
print(Person.__dict__["planet"])
print(getattr(Person, "planet"))
