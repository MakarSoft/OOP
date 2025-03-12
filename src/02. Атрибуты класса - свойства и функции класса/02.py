from pprint import pprint

class Person:
    name = 'Ivan'

print(Person.name)

# dir() — встроенная функция в Python, которая возвращает список атрибутов и
# методов любого объекта (скажем, функций, модулей, строк, списков, словарей и т. д.).
# Возвращает:
# dir() пытается вернуть действительный список атрибутов объекта,
# к которому он вызывается. Кроме того, функция dir() ведет себя по-разному
# с разными типами объектов, поскольку она нацелена на получение наиболее
# релевантного, а не полной информации. 
# Для объектов класса он возвращает список имен всех допустимых атрибутов и базовых атрибутов. 
# Для объектов Modules/Library он пытается вернуть список имен всех атрибутов, содержащихся в этом модуле. 
# Если никакие параметры не переданы, он возвращает список имен в текущей локальной области.

lst = dir(Person)
pprint(lst)

pprint(Person.__dict__, sort_dicts=False)
pprint(Person.__dict__, sort_dicts=True)

# __dict__ - это и есть пространство имен класса или экземпляров класса
# Хранит состояние всех объектов...

# mappingproxy - можно трактовать как read-only словарь
# почему __dict__ класса — это mappingproxy, а __dict__ экземпляра — это просто dict

# Это помогает интерпретатору гарантировать, что ключи для атрибутов и методов уровня класса могут быть только строками.
# В другом месте Python является «согласным языком для взрослых», что означает, что dict для объектов доступны и могут быть изменены пользователем.
# Однако в случае атрибутов и методов уровня класса для классов, если мы можем гарантировать, что ключи являются строками,
# мы можем упростить и ускорить общий код для поиска атрибутов и методов на уровне класса.
# В частности, логика поиска __mro__ для классов упрощается и ускоряется за счет предположения, что ключи словаря класса являются строками.

# This helps the interpreter assure that the keys for class-level attributes and methods can only be strings.
# Elsewhere, Python is a "consenting adults language", meaning that dicts for objects are exposed and mutable by the user.
# However, in the case of class-level attributes and methods for classes, if we can guarantee that the keys are strings,
# we can simplify and speed-up the common case code for attribute and method lookup at the class-level. In particular,
# the __mro__ search logic for new-style classes is simplified and sped-up by assuming the class dict keys are strings.

# Mappingproxy — это просто словарь без __setattr__метода.

from types import MappingProxyType
d={'key': "value"}
m = MappingProxyType(d)
print(type(m)) # <class 'mappingproxy'>

# m['key']='new' #TypeError: 'mappingproxy' object does not support item assignment

# mapproxy существует с версии Python 3.3. Следующий код показывает типы dict:

class C:pass
ci=C()
print(type(C.__dict__)) #<class 'mappingproxy'>
print(type(ci.__dict__)) #<class 'dict'>



##############


Person.age = 100

print(getattr(Person, 'name'))
print(getattr(Person, 'age'))
setattr(Person, 'dob', '02.02.64')
setattr(Person, 'age',101)
print(Person.age)


class Person:
    name = 'Ivan'

    def hello():
        print('Hello')


pprint(Person.__dict__)
print(Person.hello)
print(type(Person.hello))

pass