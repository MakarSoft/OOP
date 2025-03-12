# 00-simple-class.py
# ------------------------------------------------

# Объявление пустого класса MyClass
class MyClass:
    pass


print(MyClass)
# <class '__main__.MyClass'>

print(type(MyClass))
# <class 'type'>

print(dir(MyClass))
# [
#   '__class__', '__delattr__', '__dict__', '__dir__',
#   '__doc__', '__eq__', '__format__', '__ge__',
#   '__getattribute__', '__getstate__', '__gt__', '__hash__',
#   '__init__', '__init_subclass__', '__le__', '__lt__',
#   '__module__', '__ne__', '__new__', '__reduce__',
#   '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#   '__str__', '__subclasshook__', '__weakref__'
# ]

print(hex(id(MyClass)))
# 0x556bcac591a0

print(MyClass.__dict__)
# {
#   '__module__': '__main__',
#   '__dict__': <attribute '__dict__' of 'MyClass' objects>,
#   '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
#   '__doc__': None
# }

# Создание экземпляра класса
instance = MyClass()

print(hex(id(instance)))
# 0x7f7bba3d2000

print(instance)
# <__main__.MyClass object at 0x7f07139d6fc0>

# Вывод типа instance
print(type(instance))
# <class '__main__.MyClass'>

print(instance.__dict__)
# {}
