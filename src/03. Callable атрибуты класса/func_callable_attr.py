import sys

from typing import Callable
from types import FunctionType, MethodType

from pprint import pprint


class Person:
    '''Супер-класс'''

    def say_hello() -> None:
        print('Hello')


def func() -> None:
    '''
    Пример фунции, определенной
    в глобальном пространстве имён
    '''

    print("Global Func")


print(repr(Person.say_hello))

#  Что находится в пространстве имен модуля
current_module = sys.modules[__name__]
pprint({
    name: value
    for name, value
    in current_module.__dict__.items()
    if name != '__builtins__'
})

pprint({
    name: value
    for name, value
    in current_module.__dict__.items()
})
# Получить коллекцию callable-объектов, определенных
# в глобальном пространстве имен
# ... множество разнообразных объектов и типов
pprint({
    name: value
    for name, value
    in current_module.__dict__.items()
    if callable(value)
})
# {'Callable': typing.Callable,
#  'FunctionType': <class 'function'>,
#  'MethodType': <class 'method'>,
#  'Person': <class '__main__.Person'>,
#  'func': <function func at 0x7fa52cf439c0>,
#  'pprint': <function pprint at 0x7fa52cf43600>}


# Получить коллекцию "чистых" ф-ций, определенных
# в глобальном пространстве имен
pprint({
    name: value
    for name, value
    in current_module.__dict__.items()
    if isinstance(value, FunctionType)
})
# {
#   'func': <function func at 0x7f6a41d377e0>,
#   'pprint': <function pprint at 0x7f6a41d37560>
# }

# Протестируем функцию func определенную в пространстве имен модуля
# (глобальное пространство имен)
# Смоделируем такую же строку ...
print(
    f"<{type(func).__name__} "
    f"{func.__name__} "
    f"at {hex(id(func))}>"
)


# Вызов функции, объявленной в пространстве имён класс Person
Person.say_hello()

# Связывание объекта-функции определенной в пространстве имен класса
# с глобальной переменной
f = Person.say_hello
pprint({
    name: value
    for name, value
    in globals().items()
    if not callable(value) and not name.startswith("__")
})
print(hex(id(func)))
f()

print(f'type(Person.say_hello) = {type(Person.say_hello)}')
print(f'type(f) = {type(f)}')

print(f'id(Person.say_hello) = {hex(id(Person.say_hello))}')
print(f'id(f) = {hex(id(f))}')
