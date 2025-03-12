#  Callable атрибуты класса


class Person:
    def say_hello() -> None:
        print("Hello!")


print(Person.say_hello)
print(type(Person.say_hello))
print()

Person.say_hello()

Person.__dict__["say_hello"]()
getattr(Person, "say_hello")()
print()

# Мы знаем, что можем получить доступ к атрибутам класса через экземпляр,
# поэтому мы также должны иметь возможность получить доступ к атрибуту-функции
# таким же образом:
p = Person()
print(id(p))
print(p.say_hello)
print(type(p.say_hello))
print()

# тип изменился с function на method, а repr представление функции гласит,
# что это связанный метод конкретного объекта p, который мы создали
# (обратите внимание на адрес памяти).

try:
    p.say_hello()
except Exception as ex:
    print(type(ex).__name__, ex)
# TypeError Person.say_hello() takes 0 positional arguments but 1 was given

# method является фактическим типом в Python, и, как и функции, они
# являются вызываемыми, но у них есть одна отличительная черта.
# Их необходимо привязать к объекту, и эта ссылка на объект передается
# базовой функции.
# Часто, когда мы определяем функции в классе и вызываем их из экземпляра,
# нам нужно знать, какой конкретный экземпляр использовался для вызова функции.
# Это позволяет нам взаимодействовать с переменными экземпляра.
# Для этого Python автоматически преобразует обычную функцию, определенную
# в классе, в метод, когда она вызывается из экземпляра класса.
# Кроме того, он «привязывает» метод к экземпляру, то есть экземпляр
# будет передан как первый аргумент вызываемой функции.
# Он делает это с помощью дескрипторов ...


class Person:
    def say_hello(*args):
        print("say_hello args:", args)


Person.say_hello()
p = Person()
print(hex(id(p)))
p.say_hello()
print()
# объект p был передан как аргумент функции класса say_hello.

# преимуществом является то, что теперь мы можем легко взаимодействовать
# с атрибутами экземпляра


class Person:
    def set_name(instance_obj, new_name):
        instance_obj.name = new_name
        # setattr(instance_obj, 'name', new_name)


p = Person()
p.set_name("Alex")
print(p.__dict__)

# методы — это объекты, создаваемые Python при вызове функций
# класса из экземпляра.

# -------------------------------


class Person:
    def say_hello(self):
        print(f"{self} says hello")


p = Person()
print(p.say_hello)
# <bound method Person.say_hello of <__main__.Person object at 0x7efc1202d4c0>>

m_hello = p.say_hello
print(type(m_hello))
# <class 'method'>

# У метода есть  атрибут `__func__`:
# функцией класса, используемой для создания метода (базовая функция)
print(m_hello.__func__)
# <function Person.say_hello at 0x7efc1201e980>

print(hex(id(p)))
# 0x7efc1202d4c0
print(m_hello.__self__)
# <__main__.Person object at 0x7efc1202d4c0>

# думайте о методах как о функциях, которые были привязаны к
# определенному объекту, и этот объект передается в качестве
# первого аргумента вызова функции.
# Остальные аргументы затем передаются после этого.
