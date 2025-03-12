class MyProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        if self.fget is not None:
            return self.fget(instance)
        return None

    def __set__(self, instance, value):
        if self.fset is not None:
            return self.fset(instance, value)
        raise AttributeError("can't set attribute")

    def setter(self, fset):
        self.fset = fset
        return self

# Пример использования
class Person:
    def __init__(self, name):
        self._name = name

    @MyProperty
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Имя должно быть строкой")
        self._name = value

# Использование
p = Person("Alice")
print(p.name)  # Вывод: Alice
p.name = "Bob"
print(p.name)  # Вывод: Bob

try:
    p.name = 123  # Это вызовет ValueError
except ValueError as e:
    print(e)  # Вывод: Имя должно быть строкой
